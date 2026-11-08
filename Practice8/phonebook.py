"""PhoneBook console demonstrating PostgreSQL functions and procedures."""

import argparse
import json

import psycopg2

from connect import connect, initialize_database


def search(pattern):
    with connect() as connection, connection.cursor() as cursor:
        cursor.execute("SELECT * FROM search_contacts(%s)", (pattern,))
        return cursor.fetchall()


def upsert(username, phone):
    with connect() as connection, connection.cursor() as cursor:
        cursor.execute("CALL upsert_contact(%s, %s)", (username, phone))


def bulk_upsert(usernames, phones):
    with connect() as connection, connection.cursor() as cursor:
        cursor.execute("CALL bulk_upsert_contacts(%s, %s, NULL)", (usernames, phones))
        result = cursor.fetchone()
        return result[0] if result else []


def page(limit, offset):
    with connect() as connection, connection.cursor() as cursor:
        cursor.execute("SELECT * FROM get_contacts_page(%s, %s)", (limit, offset))
        return cursor.fetchall()


def delete(username=None, phone=None):
    if (username is None) == (phone is None):
        raise ValueError("Specify exactly one of username or phone")
    with connect() as connection, connection.cursor() as cursor:
        cursor.execute("CALL delete_contacts(%s, %s)", (username, phone))


def show(rows):
    for contact_id, username, phone in rows:
        print(f"{contact_id}\t{username}\t{phone}")
    if not rows:
        print("No contacts found.")


def build_parser():
    parser = argparse.ArgumentParser(description="Practice 8 PostgreSQL PhoneBook")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("init", help="create the table and install SQL routines")
    item = commands.add_parser("upsert", help="insert or update one username")
    item.add_argument("username")
    item.add_argument("phone")
    query = commands.add_parser("search", help="find a name or phone pattern")
    query.add_argument("pattern")
    bulk = commands.add_parser("bulk", help="upsert rows from a JSON file")
    bulk.add_argument("json_file", help="JSON array of {username, phone} objects")
    listing = commands.add_parser("page", help="list contacts by page")
    listing.add_argument("page", type=int, help="page number, starting at 1")
    listing.add_argument("--size", type=int, default=10)
    removal = commands.add_parser("delete", help="delete by exact username or phone")
    selector = removal.add_mutually_exclusive_group(required=True)
    selector.add_argument("--username")
    selector.add_argument("--phone")
    return parser


def main():
    args = build_parser().parse_args()
    try:
        initialize_database()
        if args.command == "init":
            print("PhoneBook table and routines are ready.")
        elif args.command == "upsert":
            upsert(args.username, args.phone)
            print("Contact inserted or updated.")
        elif args.command == "search":
            show(search(args.pattern))
        elif args.command == "bulk":
            with open(args.json_file, encoding="utf-8") as source:
                records = json.load(source)
            if not isinstance(records, list) or any(
                not isinstance(row, dict) or "username" not in row or "phone" not in row
                for row in records
            ):
                raise ValueError("JSON must be a list of objects with username and phone")
            invalid = bulk_upsert(
                [row["username"] for row in records],
                [row["phone"] for row in records],
            )
            print(f"Processed {len(records)} row(s); {len(invalid)} invalid row(s).")
            if invalid:
                print(json.dumps(invalid, ensure_ascii=False, indent=2))
        elif args.command == "page":
            if args.page < 1:
                raise ValueError("Page number must be at least 1")
            show(page(args.size, (args.page - 1) * args.size))
        elif args.command == "delete":
            delete(args.username, args.phone)
            print("Matching contacts deleted.")
    except (OSError, ValueError, json.JSONDecodeError, psycopg2.Error) as error:
        raise SystemExit(f"Error: {error}") from error


if __name__ == "__main__":
    main()
