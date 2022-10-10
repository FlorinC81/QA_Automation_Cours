print("   Exercitiul 9\n")
def nu_returneaza(x, y):
    if x > y:
        print(f"Primul număr {x} este mai mare decat al doilea nr {y}")
    elif x < y:
        print(f'Al doilea nr {y} este mai mare decat primul nr {x}')
    else:
       print('Numerele sunt egale')
x = int(input("Introduceti primul numar: "))
y = int(input("Introduceti al doilea numar: "))
nu_returneaza(x, y)