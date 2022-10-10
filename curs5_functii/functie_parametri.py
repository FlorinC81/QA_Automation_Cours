"""
Parametrii (input - datele de intrare) sunt niste nume pe care noi le folosim pentru variabilele
pe care le putem transmite functiei!
"""

def say_hello_to(nume):    #variabila nume se numeste PARAMETRU al functiei
    print("Hello eu sunt functia!")
    print(f"tu esti {nume}")
say_hello_to("Marcela")
say_hello_to("Flo")

def say_goodbye(nume, varsta):
    print(f"salut {nume} care ai {varsta} ani!")
    print("Goodbye")

say_goodbye("Ionel", 52)
say_goodbye("Maria", 28)
"""
Parametri sunt pozitionali, adica atunci cand apelam functia, 
prima valoare va merge la prima variabila,
 a doua valoare va merge la a 2 a variabila samd
 
"""
print("-"*80)

say_goodbye(52, "Ionel")
say_goodbye(varsta=52, nume="Ionel")
# say_goodbye("honolulu")  #TypeError: say_goodbye() missing 1 required positional argument: 'varsta'
# say_goodbye("ionel", "popescu",24)  #TypeError: say_goodbye() takes 2 positional arguments but 3 were given


"""
Atunci cand pt anumiti parametri dorim sa avem valori prestabilite (default)
putem face asta, punand o valoare direct atunci cand definim functia 

def nume_functie(parametru = valoare):
    etc
    
Daca oferim o valoare prestabilita, atunci parametrul nostru zicem ca este optional.
nume_functie() SAU 
nume_functie(alta valoare) 
"""
def say_hi(nume, mesaj = "Acesta este un mesaj standard"):
    print(f"{mesaj}")
    print(f"I-am zis hi lui {nume}")
print()

say_hi("Mihai")
say_hi("Mihai", "Alt mesaj!!")

"""
Parametrii "traiesc" doar in interiorul functiei
La fel si orice variabila definita in interiorul functiei
"""
#print(nume)  #NameError: name 'nume' is not defined

"""
IMPORTANT: desi putem avea oricati parametri vrem noi la o functie, 
nu este recomandat sa avem mai mult de 6
"""
