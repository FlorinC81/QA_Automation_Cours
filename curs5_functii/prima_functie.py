"""
Functii - bucati de cod reutilizabilepe care oricine le poate folosi
adica noi definim o functie o data si apoi o putem folosi in mai multe locuri

Sintaxa
def nume_functie(optional, aici putem avea parametri ):
    aici, indentat
    a fi
    corpul functiei,
     adica tot ceea ce se
     executa in functie

Cat timp dor definim o functie, nu se intampla nimic. Trebuie sa o APELAM pentru ca codul din interio sa se execute
"""

def say_hello():
    print("1. Hello!")
    print("2. Aceasta este prima mea functie")

print("3. Azi vom invata despre functii!")
say_hello()