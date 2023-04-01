#!/usr/bin/env python3
from re import findall
ref = "\[\d+\]"
num = "\d+"



contenido="""
esto es un[9]intento honesto,
esto es un[8]intento honesto,
esto es un[5]intento honesto,
esto es un[89]intento honesto,
esto es un[118]intento honesto,
esto es un[15948]intento honesto,
esto es un[1589]intento honesto,
esto es un[1236]intento honesto,
esto es un[222]intento honesto,
"""


referencias="""
[9] ref 1
[8] ref 2
[5] ref 3
[89] ref 4 
[118] ref 5
[15948] ref 6
[1589] ref 7
[1236] ref 8
[222] ref 9
"""


# print(findall(ref, contenido))
# print(findall(ref, referencias))


notas = findall(ref, contenido)
curated_notas = []

pie = findall(ref, referencias)
curated_pie = []


NEW_TEXT = contenido
NEW_REF = referencias


for i, val in enumerate(notas):
    # print(val, findall(num, val)[0])
    number = findall(num, val)[0]
    

    NEW_TEXT=NEW_TEXT.replace(val, f"<a id='note-{number}' href='#foot-{number}'> {val} </a>")
    NEW_REF=NEW_REF.replace(val, f"<a id='foot-{number}' href='#note-{number}'> {val} </a>")

#for item in enumerate()

# print(curated_notas[0])


print(NEW_TEXT)
print(NEW_REF)

# print(curated_pie[0])


"""
<p>more info at the footer :v <a id="note-1" href='#foot-1'> [1] </a></p>

<p> <a id='foot-1' href='#note-1'>[1]</a> :v el pepe </p>
"""
