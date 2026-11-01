"""Console PhoneBook backed by PostgreSQL."""

import argparse
import csv
import sys

import psycopg2
from psycopg2.extras import execute_values

from connect import connect, initialize_database


def add_contact(username, phone):
    with connect() as connection, connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO contacts (username, phone) VALUES (%s, %s) "
            "ON CONFLICT (username, phone) DO NOTHING RETURNING id",
            (username.strip(), phone.strip()),
        )
        return cursor.fetchone() is not None


def import_csv(path):
    """Import CSV with username,phone headers; duplicate pairs are skipped."""
    with open(path, newline="", encoding="utf-8-sig") as csv_file:
        reader = csv.DictReader(csv_file)
        if not reader.fieldnames or not {"username", "phone"}.issubset(
            {header.strip().lower() for header in reader.fieldnames}
        ):
            raise ValueError("CSV must contain 'username' and 'phone' headers")
        headers = {header.strip().lower(): header for header in reader.fieldnames}
        rows = []
        for line_number, row in enumerate(reader, start=2):
            username = (row.get(headers["username"]) or "").strip()
            phone = (row.get(headers["phone"]) or "").strip()
            if not username or not phone:
                raise ValueError(f"CSV line {line_number}: username and phone are required")
            rows.append((username, phone))

    if not rows:
        return 0
    with connect() as connection, connection.cursor() as cursor:
        execute_values(
            cursor,
            "INSERT INTO contacts (username, phone) VALUES %s "
            "ON CONFLICT (username, phone) DO NOTHING",
            rows,
        )
        return cursor.rowcount


def update_contact(contact_id, username=None, phone=None):
    fields, values = [], []
    if username is not None:
        fields.append("username = %s")
        values.append(username.strip())
    if phone is not None:
        fields.append("phone = %s")
        values.append(phone.strip())
    if not fields:
        raise ValueError("Provide a new username and/or phone number")
    values.append(contact_id)
    with connect() as connection, connection.cursor() as cursor:
        cursor.execute(
            f"UPDATE contacts SET {', '.join(fields)} WHERE id = %s RETURNING id",
            values,
        )
        return cursor.fetchone() is not None


def find_contacts(name=None, phone_prefix=None):
    clauses, values = [], []
    if name:
        clauses.append("username ILIKE %s")
        values.append(f"%{name}%")
    if phone_prefix:
        clauses.append("phone LIKE %s")
        values.append(f"{phone_prefix}%")
    query = "SELECT id, username, phone FROM contacts"
    if clauses:
        query += " WHERE " + " AND ".join(clauses)
    query += " ORDER BY username, id"
    with connect() as connection, connection.cursor() as cursor:
        cursor.execute(query, values)
        return cursor.fetchall()


def delete_contact(username=None, phone=None):
    if (username is None) == (phone is None):
        raise ValueError("Specify exactly one of username or phone")
    column, value = ("username", username) if username is not None else ("phone", phone)
    with connect() as connection, connection.cursor() as cursor:
        cursor.execute(f"DELETE FROM contacts WHERE {column} = %s", (value,))
        return cursor.rowcount


def build_parser():
    parser = argparse.ArgumentParser(description="Manage a PostgreSQL PhoneBook")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("init", help="create the contacts table")
    add = commands.add_parser("add", help="add one contact")
    add.add_argument("username", nargs="?", help="omit to enter it interactively")
    add.add_argument("phone", nargs="?", help="omit to enter it interactively")
    imported = commands.add_parser("import", help="import username,phone CSV")
    imported.add_argument("csv_file")
    update = commands.add_parser("update", help="update a contact by ID")
    update.add_argument("id", type=int)
    update.add_argument("--username")
    update.add_argument("--phone")
    search = commands.add_parser("search", help="search by name and/or phone prefix")
    search.add_argument("--name")
    search.add_argument("--phone-prefix")
    delete = commands.add_parser("delete", help="delete contacts by exact username or phone")
    selector = delete.add_mutually_exclusive_group(required=True)
    selector.add_argument("--username")
    selector.add_argument("--phone")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        initialize_database()
        if args.command == "init":
            print("PhoneBook table is ready.")
        elif args.command == "add":
            username = args.username or input("Name: ").strip()
            phone = args.phone or input("Phone: ").strip()
            if not username or not phone:
                raise ValueError("Name and phone are required")
            created = add_contact(username, phone)
            print("Contact added." if created else "That contact already exists.")
        elif args.command == "import":
            print(f"Imported {import_csv(args.csv_file)} contact(s).")
        elif args.command == "update":
            changed = update_contact(args.id, args.username, args.phone)
            print("Contact updated." if changed else "No contact found with that ID.")
        elif args.command == "search":
            for contact_id, username, phone in find_contacts(args.name, args.phone_prefix):
                print(f"{contact_id}\t{username}\t{phone}")
        elif args.command == "delete":
            count = delete_contact(args.username, args.phone)
            print(f"Deleted {count} contact(s).")
    except (OSError, ValueError, psycopg2.Error) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
