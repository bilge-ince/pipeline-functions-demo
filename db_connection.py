import psycopg2
import os

def _create_db_connection():
    """Create and return a database connection."""
    conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
)
    return conn