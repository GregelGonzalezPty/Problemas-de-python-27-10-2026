secleto = 7
numero = int(input("Adivina el numero(1,10): "))

while numero != secleto:
     if numero < secleto:
        print("muy bajo")
     else:
         print("Muy alto")
     numero = int(input("intenta de nuevo: "))

print ("ACERTASTE!")