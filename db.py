import sqlite3 as lite
import sys
con = lite.connect('user.db')
username="'; UPDATE ORDER_HISTORY SET amount=0.0--"
password="123123"
with con: 
    cur = con.cursor() 
    # cur.execute("DROP TABLE IF EXISTS USER")
    # cur.execute("CREATE TABLE USER(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL)")
    # cur.execute("INSERT INTO USER (username, password) VALUES ('mark_cuban','password123')")
    cur.execute("DROP TABLE IF EXISTS ORDER_HISTORY")
    cur.execute("CREATE TABLE ORDER_HISTORY (id INTEGER PRIMARY KEY AUTOINCREMENT, amount REAL, cc_number TEXT, username TEXT NOT NULL, FOREIGN KEY (username) REFERENCES USER (username))")
    cur.execute("INSERT INTO ORDER_HISTORY (amount, cc_number, username) VALUES ('1000','763274621739817', 'minhdang241')")
    cur.execute("INSERT INTO ORDER_HISTORY (amount, cc_number, username) VALUES ('355.4','763274621739817', 'minhdang241')")
    cur.execute("INSERT INTO ORDER_HISTORY (amount, cc_number, username) VALUES ('260.5','763274621739817', 'minhdang241')")
    
    cur.execute("INSERT INTO ORDER_HISTORY (amount, cc_number, username) VALUES ('99.3','163987621123817', 'mark_cuban')")
    cur.execute("INSERT INTO ORDER_HISTORY (amount, cc_number, username) VALUES ('19.6','163987621123817', 'mark_cuban')")
    cur.execute("INSERT INTO ORDER_HISTORY (amount, cc_number, username) VALUES ('590','163987621123817', 'mark_cuban')")
    query = f"SELECT * FROM USER WHERE username='{username}' AND password='{password}'"
    # cur.executescript(query)
    # print(cur.fetchall())

    # cur.execute("SELECT * FROM ORDER_HISTORY WHERE USER_ID=1 OR 1=1")
    # print(len(cur.fetchall()))
    



