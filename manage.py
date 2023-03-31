#!/usr/bin/env python3
import sqlite3
from sys import argv

"""
Over-engineered book manager! I'm planning on using it together with FLASK.

Uodate from REPL!
$python3
import sqlite3
cur = sqlite3.connect("library.db").cursor()

>To delete table:
    cur.execute("DROP TABLE library")
    cur.commit() 

>To update row:
    cur.execute("UPDATE library SET footer = ' ' WHERE id = ch00")
    cur.commit() 

>To retrieve:
    for x in sqlite3.connect("./library.db").execute("select * from library where chapter='ch00'"): print(x


"""


print(len(argv))

with sqlite3.connect("./library.db") as con:
    
    try:
        con.execute("""CREATE TABLE IF NOT EXISTS library
                        (chapter TEXT PRIMARY KEY, content TEXT, footer TEXT)""")
    finally:
        if len(argv) == 4: 

            CHAPTER = argv[1]
            CONTENT = argv[2]
            REFERENCES = argv[3]

            with open(CONTENT, 'r') as cont, open(REFERENCES, 'r') as refe:
                content = cont.read()
                references = refe.read()
        
        if len(argv) == 3: 
            CHAPTER = argv[1]
            CONTENT = argv[2]
            references = ''

            with open(CONTENT, 'r') as cont:
                content = cont.read()
            
        con.execute("INSERT INTO library (chapter, content, footer) VALUES (?, ?, ?)", (CHAPTER, content, references))


with sqlite3.connect("./library.db") as con:
    cursor = con.execute("SELECT chapter FROM library")
    for row in cursor:
        print(row)


# with sqlite3.connect("./library.db") as con:
#     con.execute("""CREATE TABLE IF NOT EXISTS library
#                     (chapter TEXT PRIMARY KEY, content TEXT)""")

#     # con.execute("INSERT INTO library (chapter, title, content) VALUES ('100', 'test 01', 'contents: none :v')")
#     # con.execute("INSERT INTO library (chapter, title, content) VALUES ('100', 'test 01', 'contents: none :v')")

#     # con.execute("INSERT INTO library (chapter, title, content) VALUES ('100', 'test 01', 'contents: none :v')")
#     pass


    
