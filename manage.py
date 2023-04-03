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
        # adding a new entry. (CREATE)
        # manage.py ch01 contents.txt references.txt
        if len(argv) == 4 and argv[1][0] != '-': #i.e.: has 4 arguments AND no flags

            CHAPTER = argv[1]
            CONTENT = argv[2]
            REFERENCES = argv[3]

            with open(CONTENT, 'r') as cont, open(REFERENCES, 'r') as refe:
                content = cont.read()
                references = refe.read()

            con.execute("INSERT INTO library (chapter, content, footer) VALUES (?, ?, ?)", (CHAPTER, content, references))

        # adding a new entry that has no references. (CREATE)
        # manage.py ch00 contents.txt
        if len(argv) == 3: 
            CHAPTER = argv[1]
            CONTENT = argv[2]
            references = ''

            with open(CONTENT, 'r') as cont:
                content = cont.read()
            
            con.execute("INSERT INTO library (chapter, content, footer) VALUES (?, ?, ?)", (CHAPTER, content, references))

        # updating an existing entry (UPDATE)
        # manage.py -u ch11 contents.txt references.txt
        if len(argv) == 5 and argv[1].lower() == '-u':
            CHAPTER = argv[2]
            CONTENT = argv[3]
            REFERENCES = argv[4]

            with open(CONTENT, 'r') as cont, open(REFERENCES, 'r') as refe:
                content = cont.read()
                references = refe.read()
        
            con.execute("UPDATE library SET content = ?, footer = ?  WHERE chapter = ?", (content, references, CHAPTER))
        
        # updating only the contents of an existing entry (UPDATE CONTENTS)
        # manage.py -uc ch33 contents.txt

        if len(argv) == 4 and argv[1].lower() == '-uc':
            CHAPTER = argv[2]
            CONTENT = argv[3]
            
            with open(CONTENT, 'r') as cont:
                content = cont.read()
                
            con.execute("UPDATE library SET content = ?  WHERE chapter = ?", (content, CHAPTER))


        # updating only the references of an existing entry (UPDATE CONTENTS)
        # manage.py -ur ch47 references.txt
        if len(argv) == 4 and argv[1].lower() == '-ur':
            CHAPTER = argv[2]
            REFERENCES = argv[3]

            with open(REFERENCES, 'r') as refe:
                references = refe.read()

            con.execute("UPDATE library SET footer = ?  WHERE chapter = ?", (references, CHAPTER))

        # deleting specified entry! (DELETE)
        # manage.py -d ch72
        if len(argv) == 3 and argv[1].lower() == '-ur':
            CHAPTER = argv[2]

            # con.execute("UPDATE library SET footer = ?  WHERE chapter = ?", (references, CHAPTER))
            con.execute("DELETE FROM library WHERE chapter = ?", (CHAPTER))

        


        # con.execute("UPDATE library SET footer = ?  WHERE chapter = ?"), (references, CHAPTER)






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


    
