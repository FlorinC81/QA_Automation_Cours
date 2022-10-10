# Tupla = este o lista care nu poate fi modificata in nici un fel
# Tupla este imutabile( adica nu poate fi modificata)
tuple1 = (5,7,12,-3,8)
tuple2 =("Ana","are","mere")
tuple3 = (True,False,True, False, False)

print(tuple1[1])
# tuple1[1]= 4 # daca vrem sa modificam un element din tupla va da eroare

print(len(tuple1))
print(max(tuple1))
print(min(tuple1))
print(tuple1.count(12))
