string = 'Santhiago Lopes'
number_of_letters = 3
new_string = ".".join([
    string[indice:indice + number_of_letters] 
    for indice in range(0,len(string),number_of_letters)
])

print(new_string)