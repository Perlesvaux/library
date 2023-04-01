#!/usr/bin/env python3
from flask import Flask, render_template
import sqlite3
from re import findall

app = Flask(__name__)

@app.route('/')
def index():
    #connect to db
    with sqlite3.connect("./library.db") as con:
        cur = con.cursor()

        cur.execute("SELECT * from library WHERE chapter='ch03';")
        # data = cur.fetchall()

        cap, cont, ref = cur.fetchone()

        # print(tup[0], tup[1], tup[2])


        # print(ref)

        #Copies for cont & ref... just in case
        # NEW_TEXT = cont
        # NEW_REF = ref


        # data = cap

        #define regex to pick notes & footnotes
        foo = "\[\d+\]"
        num = "\d+"

        #list all notes (must be equal in number to footnotes)
        notas = findall(foo, ref)


        for i, val in enumerate(notas):
            # print(val, findall(num, val)[0])
            number = findall(num, val)[0]
        

            cont=cont.replace(val, f"<a id='note-{number}' href='#foot-{number}'> {val} </a>")
            ref=ref.replace(val, f"<a id='foot-{number}' href='#note-{number}'> {val} </a>")

        



        chapter = """
        
        
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>📚{name}</title>
            {style}
        </head>
        <body>
        <p>
        {libro}
        </p>


        <script defer>
        {scroll_script}
        </script>

        <hr>

        <footer> <p>{footer}</p> </footer>

        </body>
        </html>
        """.format(
            libro=cont.replace('\n', '</p><p>'),
            name = cap,
            style="<style>p{font-size: 1.5rem; font-family: 'Lucida Console', 'Courier New', monospace;} body{background-color: antiquewhite;}</style>",
            scroll_script="""  if (typeof(Storage) !== "undefined") {
                // Code for localStorage/sessionStorage.

                //YOS stands for Y-offset. Defaults to 0 
                //on first-time use. Then, it retrieves the stored
                // y-offset to adjust srolling accordingly

                if (localStorage.getItem("YOS") != null) window.scrollTo(0, localStorage.getItem("YOS") )
                
                window.addEventListener('scroll', ()=>{localStorage.setItem("YOS", window.pageYOffset);})

            } else {
                // Sorry! No Web Storage support..
                console.log('No Web Storage Support! :(')
            }""",
            footer = ref.replace('\n', '</p><p>'),
            )


    return render_template('./index.html', data=chapter)


if __name__ == "__main__":
    app.run(debug=True)   