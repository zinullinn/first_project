# Practice 7: Python & PostgreSQL PhoneBook

Console PhoneBook application demonstrating PostgreSQL CRUD operations through `psycopg2`.

## Setup

1. Install PostgreSQL and create a database named `phonebook` (or choose another database).
2. Install Python dependency: `python -m pip install -r requirements.txt`.
3. Set connection environment variables as needed:

   - `PGHOST` (default `localhost`)
   - `PGPORT` (default `5432`)
   - `PGDATABASE` (default `phonebook`)
   - `PGUSER` (default `postgres`)
   - `PGPASSWORD` (default empty)

The app creates the `contacts` table and indexes automatically. To create them explicitly, run `python phonebook.py init`.

## Commands

```text
python phonebook.py add "Alice Johnson" "+1-555-0101"
python phonebook.py add
python phonebook.py import contacts.csv
python phonebook.py search --name Alice
python phonebook.py search --phone-prefix +1-555
python phonebook.py search --name Alice --phone-prefix +1
python phonebook.py update 1 --username "Alice J."
python phonebook.py update 1 --phone +1-555-0199
python phonebook.py delete --username "Alice J."
python phonebook.py delete --phone +1-555-0199
```

CSV files must have `username` and `phone` column headers. Imports skip duplicate username/phone pairs. Search filters can be combined; no filters lists every contact. Update targets a contact's numeric `id`, which is shown in search results. Deleting by username or phone removes every exact match.

Run `python phonebook.py add` without arguments to enter the name and phone interactively.

Each write runs in a transaction and is committed on success or rolled back on error. SQL values are parameterized; the update column list is built only from the two fixed, supported fields.
