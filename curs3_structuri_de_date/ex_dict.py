from pprint import pprint #aici se importa o librarie
# Dictionar: o structura de date care stocheaza informatii in perechi key-value
# unde key actioneaza ca si indicii din lista, adica ne permit sa ne referim la value bazat pe key.


dict_gol = {}

dict1 = {
    "str":12,
    3:45,
    3.14: "un alt string",
    True:5,
    "x": False
}
tren = ["grau","orz","orez","hrisca","quinoua","porumb"]
tren_colorat= {
    "rosu": "grau",
    "verde": "orz",
    "albastru": "orez",
    "galben": "hrisca",
    "alb": "quinoua",
    "negru": "porumb"
}
# Cheile din dictionar trebuie sa fie unice
#Cheile trebuie sa fie tipuri de date simple (int, float, bool, str)
print(f"In vagonul rosu avem {tren_colorat['rosu']}")

# Exemplu: vreau sa vad de cate ori apare o litera anume intr-un text
cuvant = "abracadabra"

# Daca facem asa vom avea nevoie de 26 variabile ... cam multe
litera_a_cnt = cuvant.count("a")
litera_b_cnt = cuvant.count("b")

# Facem un dictionar in care key este litera cautata,iar value este de cate ori apare in text
dict_litere_cnt = {
    "a": cuvant.count("a"),
    "b": cuvant.count("b"),
    "r": cuvant.count("r")
}
print(dict_litere_cnt)

# Exemplu: grupare date in mod logic

student = {
    "name": "Popescu",
    "firtsname": "Ion",
    "age": 21,
    "weight": 76.5,
    "birthdate":{
        "day": 24,
        "month": "October",
        "Year": 1981
    }
}
print(f"Ma cheama {student['name']} {student['firtsname']}. Am {student['age']} ani si {student['weight']} kg.")

print(f"M-am nascut pe {student['birthdate']['Year']} {student['birthdate']['month']} {student['birthdate']['day']}")

birthdate =student['birthdate']
print(f"M-am nascut pe {birthdate['day']} {birthdate['month']} {birthdate['Year']}")

# Operatii pe dictionare
tren_colorat= {
    "rosu": "grau",
    "verde": "orz",
    "albastru": "orez",
    "galben": "hrisca",
    "alb": "quinoua",
    "negru": "porumb"
}

# Adaugare element: folosim un key car nu mai exista si elementel este adaugat
tren_colorat['roz'] ="naut"
print(tren_colorat)

# Stergere element
del tren_colorat['roz']
print(tren_colorat)

# Modificare element
tren_colorat['rosu'] = "pietre"
print(tren_colorat)

# pt a 'schimba' key, trebuie de fapt sa adaugam un nou element cu noua cheie si sa o stergem pe cea veche.
pietre = tren_colorat['rosu']
del tren_colorat['rosu'] #va sterge cheia cu tot cu valoare
tren_colorat ['turcoaz'] = "pietre"
print(tren_colorat)

# Values se pot repeta, nu trebuie sa fie unice
tren_colorat['maro']= "orz"
tren_colorat['magenta'] = "orz"
print(tren_colorat)

# Daca key nu este in dictionar, vom primi eroare
#print(tren_colorat['portocaliu']) #Eroare, nu este niciun vagon portocaliu
if 'portocaliu' in tren_colorat:
    print(tren_colorat['portocaliu'])
else:
    print("Nu este nici un vagon portocaliu")

#pprint = pretty print
pprint(tren_colorat)