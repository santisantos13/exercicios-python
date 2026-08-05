'''for x in range(1,11):
    for y in range(1,6):
        print(x,'-',y)'''

lines_and_columns = [ # "for" seguido de "for" em list comprehention sempre é aninhado
    (x, y)
    if y != 2 else (x, y * 100)
    for x in range(1, 11)
    for y in range(1, 6) 
    if x != 2
]

print(lines_and_columns)