import random

def ruleta(usuario):
    usuario = usuario.title()
    print(f"¡Hola, {usuario}! Bienvenido/a al juego de la ruleta.")
    print("Adiviná el número que salió en la ruleta.")
    print("Tenés 6 intentos para adivinar el número.")
    # Definir el número secreto
    numero_secreto = random.randint(0, 36)
    intentos = 6
    # Bucle principal del juego
    while intentos > 0:
        try:
            numero_adivinado = int(input("Ingresá un número entre 0 y 36: "))
            if numero_adivinado < 0 or numero_adivinado > 36:
                print("Número inválido. Debe estar enatre 0 y 36.")
                continue
            if numero_adivinado == numero_secreto:
                print(f"¡Felicidades, {usuario}! Adivinaste el número: {numero_secreto}.")
                break
            else:
                intentos -= 1
                if numero_adivinado < numero_secreto:
                    print(f"El número secreto es mayor. Te quedan {intentos} intentos.\n")
                else:
                    print(f"El número secreto es menor. Te quedan {intentos} intentos.\n")
        except ValueError:
            print("Entrada inválida. Por favor, ingresá un número.")
    if intentos == 0:   
        print(f"Se acabaron los intentos :( El número secreto era: {numero_secreto}.")
    print("¡Gracias por jugar a la ruleta!")

if __name__ == "__main__":
    ruleta("jugador anónimo")
```