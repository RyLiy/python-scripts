import psycopg2
from pip._vendor.distlib import database

# Connect to the DB. Fill in with own credentials.
con = psycopg2.connect(
            host = "192.168.1.101",
            database = 'demo',
            user = 'postgres',
            password = 'password')

# Connection cursor for SQL statements
cur = con.cursor()

# A sample query commented out. Pls ignore
#cur.execute("insert into orders (date,type) values (%s,%s)",('2022-01-08','sell'))

# Execute query
cur.execute("select ID, date, type from orders")

# Fetches results from select query
rows = cur.fetchall()

# Will iterate through all rows in result, and only prints the first 3 columns
for r in rows:
    print(f"ID {r[0]} Date {r[1]} Type {r[2]}")

# commit the transaction. ACID principles!
con.commit()

# close the cursor
cur.close()
# close the connection
con.close()

