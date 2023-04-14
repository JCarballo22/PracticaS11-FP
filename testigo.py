'''#Ejemplo testigo
import random

print("Comienza el ejemplo")
sacarCinco = False

for i in range(3):
    dado = random.randrange(1,7)
    print(f"Tiro {i+1}:{dado}")
    if dado ==5:
        sacarCinco = True

if sacarCinco:
    print("Ha salido al menos una vez 5")
else:
    print("No ha salido ningun 5")

print("Fin")

print("Otro ejemplo")
sacastesCinco = 0
for i in range(20):
    dado2 = random.randrange(1,7)
    print(f"Tiro {i+1}: {dado2}")
    if dado2 == 5:
        sacastesCinco += 1

print(f"En total ha(n) salido {sacastesCinco} cinco(s).")
print("Fin")'''

#Ejemplo acumulador
import random
print("comienza el ejemplo acumulador")
total = 0
for i in range(10):
    dado3 = random.randrange(1,7)
    print(f"Tiro {i+1}: {dado3}")
    total += dado3

print(f"En total obtenido {total} punto(s).")
print("Fin")