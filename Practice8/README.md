# Practice 8: PhoneBook with PostgreSQL Functions and Procedures

This extends Practice 7's `contacts(id, username, phone, created_at)` table. SQL search, pagination, upsert, bulk validation, and deletion run in PostgreSQL. The table remains compatible with Practice 7.

## Setup

1. Install PostgreSQL and create the `phonebook` database (or set `PGDATABASE`).
2. Install the Python dependency: `python -m pip install -r requirements.txt`.
3. Set `PGHOST`, `PGPORT`, `PGDATABASE`, `PGUSER`, and `PGPASSWORD` for your server. Defaults are `localhost:5432`, database `phonebook`, and user `postgres`; password defaults to empty.
4. Run `python phonebook.py init`. The app creates the compatible table, indexes, and routines from `functions.sql` and `procedures.sql`.

## Examples

```text
python phonebook.py upsert "Alice Johnson" "+1-555-0101"
python phonebook.py search "Alice"
python phonebook.py page 1 --size 10
python phonebook.py delete --username "Alice Johnson"
python phonebook.py delete --phone "+1-555-0101"
```

Bulk input is a JSON array, for example `contacts.json`:

```json
[
  {"username": "Alice Johnson", "phone": "+1-555-0101"},
  {"username": "Invalid example", "phone": "not-a-phone"}
]
```

Run `python phonebook.py bulk contacts.json`. The procedure loops through the parallel arrays, uses conditional validation, upserts valid entries, and returns rejected entries with their one-based index and reason. A valid phone has 6–20 digits and may include `+`, spaces, parentheses, periods, or hyphens. A username identifies one logical user; if Practice 7 has multiple records with that username, an upsert updates each matching row.

## SQL routines

| Routine | Call | Purpose |
| --- | --- | --- |
| `search_contacts(pattern)` | `SELECT * FROM search_contacts('ali')` | Finds a partial username or phone match |
| `get_contacts_page(limit, offset)` | `SELECT * FROM get_contacts_page(10, 0)` | Returns a stable, ordered page |
| `upsert_contact(username, phone)` | `CALL upsert_contact('Alice', '555-0101')` | Inserts a username or updates its phone |
| `bulk_upsert_contacts(usernames, phones, invalid)` | `CALL bulk_upsert_contacts(ARRAY['Alice'], ARRAY['555-0101'], NULL)` | Upserts valid values and returns invalid rows as JSONB |
| `delete_contacts(username, phone)` | `CALL delete_contacts('Alice', NULL)` | Deletes by exactly one selector |

Functions are called with `SELECT`; procedures are called with `CALL`. The SQL examples also show PL/pgSQL variables, `IF/ELSE`-style branching, loops, table results, input checks, and exceptions.
