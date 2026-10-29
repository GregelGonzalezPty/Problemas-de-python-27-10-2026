Palabra = input("Escribe una palabra: ") 

vocales = 0 

  

for letra in Palabra.lower(): 

    if letra in "aeiouáéíóú": 

        vocales += 1 

  

print("Tiene", vocales, "vocales") 