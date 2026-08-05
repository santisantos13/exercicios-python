names = [
  'santhiago', 'Alice', "Celina","Lucas"
]
new_names = [
  f'{name[0:-1].lower()}{name[-1].upper()}' 
  for name in names
]
print(new_names)