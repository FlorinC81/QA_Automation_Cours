#Aceste 2 variabule sunt de tip string
sir1 = "42"
sir2 = "True"

print(type(sir1))  # va afisa <class 'str'>, adica sir1 este string
print(type(sir2))  # la fel ca la sir1

# Type casting - fortam conversia unei variabile de la un tip la altul
#sir1 =>il convertm de la str la integer (putem si la float daca vrem)
# my_int este creat din valoarea pe care o avem in sir1, dar sir1 nu se modifica si nici nu isi modifica tipul
my_int = int(sir1)
print(sir1,type(sir1))
print(my_int, type(my_int))


sir1 = int(sir1)  #Acum am modificat sir1 prin suprascriere (sir1 este acum  int)
# str- bool
my_bool = bool(sir2)
print(sir2, type(sir2))
print(my_bool, type(my_bool))

# str-> float
sir3 = "42"
my_float = float(sir3)
print(sir3,type(sir3))
print(my_float,type(my_float))

# int-> float
another_float = float(my_int)
print(another_float, type(another_float))