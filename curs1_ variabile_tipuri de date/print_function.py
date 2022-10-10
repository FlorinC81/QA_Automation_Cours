varsta = 30
prenume = "Florin"
nume = "Chetves"

# Print este o functie care " scrie" in consola, dar care asteapta stringuri
print("pe mine ma cheama " +prenume +" "+nume)
print("eu am " +str(varsta)+ "ani")   # NU putem concatena int cu str,deci trebuie sa facem type casting
# F-strings (formatted strings)
print(f'Pe mine ma cheama {prenume} {nume} si am varsta de {varsta}')

print(f"Am mai creScut un an, acum am {varsta+1} ani")


var_str = f"aici voi scrie un text foarte lung  autor{nume} {prenume}"
var_str = f"am scris si voi mai scrie  {varsta}"
var_str = "si atat"

print(var_str)