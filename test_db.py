import os
import pytest
import psycopg2

@pytest.fixture(scope="module")
def test_db():
    conn = psycopg2.connect(os.environ.get('DATABASE_URL'))
    yield conn
    conn.close()

# define a test function to test the database content
def test_database_content(test_db):
    # create a cursor object to interact with the database
    cur = test_db.cursor()

    # create table
    cur.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL)");

    # ensure that the users table is empty
    cur.execute("SELECT COUNT(*) FROM users")
    assert cur.fetchone()[0] == 0

    # insert a new user
    cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", ("John Doe", "johndoe@example.com"))
    test_db.commit()

    # retrieve all users and validate that the new user is in the table
    cur.execute("SELECT COUNT(*) FROM users WHERE name = %s AND email = %s", ("John Doe", "johndoe@example.com"))
    assert cur.fetchone()[0] == 1

    # delete the user and ensure that the users table is empty again
    cur.execute("DELETE FROM users WHERE name = %s", ("John Doe",))
    test_db.commit()
    cur.execute("SELECT COUNT(*) FROM users")
    assert cur.fetchone()[0] == 0

    # force failure so we can test stoat functionality of reading the dumped db
    assert false

    # close the cursor
    cur.close()
