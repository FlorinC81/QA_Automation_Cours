#Set= structura de date care are doar elemente unice

set_gol = set()
print(set_gol)
an = {'primavara','vara','toamna','iarna'}
print(an)

an.add('primavara')
print(an)

#Set membership
anotimp = "vara"
if anotimp in an:
    print("Gasit")
else:
    print(" Nu exista in acest set")


an.remove('vara')
if anotimp in an:
    print("Gasit")
else:
    print(" Nu exista in acest set")

print(f"Lungimea setului este {len(an)}")