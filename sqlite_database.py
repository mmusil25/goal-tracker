#https://towardsdatascience.com/do-you-know-python-has-a-built-in-database-d553989c87bd#:~:text=In%20your%20case%2C%20if%20you%20run%20Python%20on,is%20nothing%20different%20from%20other%20regular%20relational%20databases.

import sqlite3 as sl
con = sl.connect('ledger.db')
import datetime as dt

# with con:
#     con.execute("""
#         CREATE TABLE LEDGER (
#             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#             tags TEXT,
#             price FLOAT,
#             merchant TEXT,
#             item TEXT,
#             purpose TEXT,
#             date DATE,
#             needfulness TEXT,
#             alternatives TEXT
#         );
#     """)


sql = 'INSERT INTO LEDGER (id, tags, price, merchant, item, purpose, date, needfulness, alternatives)\
                    values( ?,    ?,     ?,        ?,    ?,       ?,    ?,           ?,             ?)'
data = [
    (1, 'selfcare', 15.89, 'Homegoods', 'Candle', 'self care', dt.datetime.now(), 'Needed', 'Essential Oils'),
]

# with con:
#     con.executemany(sql, data)
#

with con:
    data = con.execute("SELECT * FROM LEDGER WHERE price >= 0.0")
    for row in data:
        print(row)