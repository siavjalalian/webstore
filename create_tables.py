import sqlite3
connection = sqlite3.connect('data.db')
cursor = connection.cursor()
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,username text ,password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY,name text,price real)"
cursor.execute(create_table)
cursor.execute("INSERT INTO users(username,password) VALUES ('jose','asdf')")
cursor.execute("INSERT INTO items(name,price) VALUES ('test',10.99)")
connection.commit()
connection.close()