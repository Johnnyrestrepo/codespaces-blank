import random
aciertos = 0
vidas = 6
letras_usadas = []
capitales = {
    'España': 'Madrid',
    'Francia': 'Paris',
    'Alemania': 'Berlin',
    'Italia': 'Roma',
    'Reino Unido': 'Londres',
    'Portugal': 'Lisboa',
    'Suecia': 'Estocolmo',
    'Suiza': 'Berna',
    'Noruega': 'Oslo',
    'Dinamarca': 'Copenhague',
}

def obtener_pais_capital():
    pais, capital = random.choice(list(capitales.items()))
    return pais, capital

def adivinar_capital():
    global vidas
    pais, capital = obtener_pais_capital()
    palabra_adivinar = "_" * len(capital)
    letras_capital = set(capital.lower())
    
    print(f"Adivina la capital del país {pais}.")
    print(f"Tienes {vidas} vidas.")
    print(" ".join(list(palabra_adivinar)))
    
    while vidas > 0:
        letra = input("Introduce una letra: ").lower()
        
      
        if letra in letras_capital:
            print("¡Letra correcta!")
            letras_usadas.append(letra)
            
            for i, c in enumerate(capital):
                if c.lower() == letra:
                    palabra_adivinar = palabra_adivinar[:i] + c + palabra_adivinar[i+1:]
                    
            print(" ".join(list(palabra_adivinar)))
            
            if "_" not in palabra_adivinar:
                print("¡Enhorabuena, has acertado la capital!")
                return
        else:
            print("Letra incorrecta.")
            vidas -= 1
            letras_usadas.append(letra)
            print(f"Te quedan {vidas} vidas.")
    
    print(f"Lo siento, has perdido. La capital era {capital}.")
            

while True:
  aciertos= +1
  adivinar_capital()
  respuesta = input("¿Quieres seguir jugando? (s/n)").lower()
  if respuesta != "s":
      break
        
print("¡Gracias por jugar!")
while aciertos == 10:
  print("¡Has acertado todas las capitales! El juego ha terminado")