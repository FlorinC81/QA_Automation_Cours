# if conditie1:
#     fa ceva daca conditie1 esre adevarat
# elif conditie2:
#     fa ceva daca conditie2 este adevarat
# elif conditie3:
#     fa ceva daca conditie3 este adevarat
# else:
#     fa ceva daca nicio conditie de paa acum nu a fost adevarata

varsta = int(input("Varsta:\n"))
if varsta <= 2:
    print("esti bebelus")
elif varsta <= 12:
    print("esti copil mic")
elif varsta <= 18:
    print("esti adolescent")
elif varsta <= 65:
    print("esti adult")
else:
    print("esti pensionar")

# alt exemplu
if varsta > 18:
    print("esti major")
    if varsta > 65:
        print("esti pensionar")
    else:
        print("esti adult")
else:
    print("esti minor")
    if varsta <= 2:
        print("bebelus")
    elif varsta <= 12:
        print("copil")
    else: # aici stim ca varsta e mai mare ca 12 si mai mica decat 18
        print("adolescent")

