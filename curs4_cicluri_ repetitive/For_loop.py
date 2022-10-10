#For - ciclu repetitiv in care eu stiu exact numarul de pasi efectuati de la inceput
#for index in range(nr):
#   fa ceva de nr ori
#Functia range(x) ne ofera pe rand toate numerele de la 0 la x-1 inclusiv

# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
print(list(range(10)))
for index in range(10):
    print(f"index are acum valoarea {index}")
print("Am terminat prima bucla repetitiva ")
# 3,4,5,6,
for idx in range(3, 7):
    print(f"Acum invat sa numar de la 3 la 7")
    print(f"    am ajuns la {idx}")
print("Am terminat a 2 a bucla repetitiva ")
#1,3,5,7,9
# pt i de la 1 la 9 din 2 in 2
for i in range(1, 10, 2):
    print("acum invat sa numar din 2 in 2")
    print(f"Am ajuns la {i}")
print("Am terminat a 3 a bucla repetitiva ")


nr_zile_saptamana = 7
for i in range(1, nr_zile_saptamana+1):
    if i == 1:
        print(f"Este prima zi din saptamana!")
    else:
        print(f"Este a {i} a zi din saptamana!")