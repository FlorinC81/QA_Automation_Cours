"""
Return - valoarea returnata =>o valoare pe care o funtie o da inapoi la apelare

def func_name(ceva):
    ...
    cod
    ...
    return altceva

"""

# Functie contor
# Primeste ca si parametri:o lista in care sa caute si elementul cautat
#  Returneaza: De cate ori apare elementul cautat in lista

def contor(lista_nr, element_cautat):
    contor_element = 0
    # Pentru fiecare numar "nr" din lista noastra
    for nr in lista_nr:
        # Dca numarul curent "nr" este egal cu numarul cautat
        if element_cautat == nr:
            # incrementam contorul
            contor_element += 1
    print(f"Am terminat de cautat, am gasit ca {element_cautat} apare de {contor_element} ori in lista!")
    return contor_element
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
conto_3 = contor(numere, 3)
print(f"Am primit rezultatul de la functie, este {conto_3}.")

"""
Return (rezultatul) este optional.
dar putem avea si mai multe instructiuni  de tip return, 
insa doar una dintre ele va fi activa la o apelare,
deoarece atunci cand python gaseste un return, OPRESTE functia.
"""

def functie_cu_multireturn(varsta):
    if varsta<18:
        return "minor"
    if varsta<65:
        return "adult angajat"
    else:
        return "pensionar"

ionel= functie_cu_multireturn(54)
print(ionel)
maria= functie_cu_multireturn(15)
print(maria)
