"""
Listele sunt structuri de date(numite si colectii in python) care pot tine mai multe valori
Valorile respective se pot accesa prin indice (adica pozitia valorii in lista).
"""

list1 = [5,7,12,-3,8]
list2 =["Ana","are","mere"]
list3 = [True,False,True, False, False]

#         0      1      2       3       4          5
tren = ["grau","orz","orez","hrisca","quinoua","porumb"]
print(f"In vagonul 1 avem {tren[1]}")
print(tren[1:4]) #slicing functioneaza la Liste la fel ca la stringuri
print(f"In ultimul vgon avem {tren[-1]}")  # indexare negativa
print(f"Trenul are in total {len(tren)} vagoane")  #lungimea Listei se determina cu funtia len


#Pentru a adauga elemente noi in lista , folsim o functie numita append
print(tren)
tren.append("ovaz")
print(tren, len(tren))

# Listele nu trebuie obligatoriu sa aiba elemente de acelasi tip
lista_complexa = ["un string",True, 12,"alt string", 3.14, "alt string"]
print(lista_complexa)
lista_complexa.remove("alt string") #stergere un element din lista, bazat pe valoare
print(lista_complexa)

var_pop = lista_complexa.pop(1)
print(f"Am scos din lista de la indexul 1, valoarea {var_pop}")
print(lista_complexa)

lista_complexa.clear()  #sterge toate elementele din lista
print(lista_complexa)

del lista_complexa  # sterge VARIABILA lista_complexa
# print(lista_complexa)  # va da eroare, deoarece am sters lista de tot
print("-"*50)
l = ["a","b","c","a","b","x","y","z","d","u","b"]
index_primul_b = l.index("b")  # returneaza indexul la care gasim valoarea din paranteze
print(index_primul_b)
print(f"Cautam acum cu slicing in sub-lista {l[index_primul_b+1:]}")
# ca sa gasim al doilea b, trebuie sa facem slicing  si sa incepem cautarea de la pozitia primului b + 1
index_al_doilea_b = l[index_primul_b+1:].index("b") + index_primul_b+1
print(index_al_doilea_b)
print(f"Cautam acum cu slicing in sub-lista {l[index_al_doilea_b+1:]}")
index_al_treilea_b = l[index_al_doilea_b+1:].index("b") + index_al_doilea_b+1
print(index_al_treilea_b)

# Deoarece putem modifica, adauga sau sterge elemente din lista, spunema ca lista este MUTABILA (adica modificabila)
l[0] = l[0].upper()
l[1] = l[1].upper()
print(l)


# Functii importante pe liste: max, min si sum

lx = [5,7,12,-3,8,5,6,3,7,8,9,5]
print(max(lx)) # returneaza elementul cu valoarea cea mai mare
print(min(lx))   # returneaza elementul cu valoarea cea mai mica
print(sum(lx)) # returneaza suma tuturor elementelor

#List membership - adica o valoare se gaseste intr-o lista
print(7 in lx)
print( 4 in lx)

# Concatenarea  (adunarea) a doua liste
ly = [78,33,25,34,99,88]
lz = lx+ly
print(f"Lx: {lx}\nLy: {ly}")
print(f"lz:{lz}")

# A doua modalitate este folosind metoda extend - se va mofica lista pe care facem extend
lx.extend(ly)
print(f"lx este acum:{lx}")
