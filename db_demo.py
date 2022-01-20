import psycopg2
from pip._vendor.distlib import database

#connect to the db
con = psycopg2.connect(
            host = "192.168.1.101",
            database = 'demo',
            user = 'postgres',
            password = 'password')

#cursor
cur = con.cursor()

#A sample query commented out.
#cur.execute("insert into orders (date,type) values (%s,%s)",('2022-01-08','sell'))

#execute query
cur.execute("select ID, date, type from orders")

#Fetches results from select query
rows = cur.fetchall()

#Will iterate through all rows, and only prints the first 3 columns
for r in rows:
    print(f"ID {r[0]} Date {r[1]} Type {r[2]}")

#commit the transaction
con.commit()

#close the cursor
cur.close()
#close the connection
con.close()