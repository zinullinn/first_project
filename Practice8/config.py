"""PostgreSQL connection settings loaded from environment variables."""

import os


def get_database_config():
    """Return psycopg2 connection kwargs; set PG* variables for your server."""
    return {
        "host": os.getenv("PGHOST", "localhost"),
        "port": os.getenv("PGPORT", "5432"),
        "dbname": os.getenv("PGDATABASE", "phonebook"),
        "user": os.getenv("PGUSER", "postgres"),
        "password": os.getenv("PGPASSWORD", ""),
    }
