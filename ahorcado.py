def ahorcado(usuario):
    usuario = usuario.title()
    print(f"¡Hola, {usuario}! Bienvenido/a al juego del ahorcado.")
    print("Adiviná la palabra secreta letra por letra.")
    print("Tenés 6 intentos para adivinar la palabra.")
    # Definir la palabra secreta
    palabra_secreta = "algoritmo"
    letras_adivinadas = []
    intentos = 6
    palabra_oculta = "_" * len(palabra_secreta)
    print(f"La palabra tiene {len(palabra_secreta)} letras: {palabra_oculta}")
    # Bucle principal del juego
    while intentos > 0 and "_" in palabra_oculta:
        letra = input("Ingresá una letra: ").lower()
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresá solo una letra.")
            continue
        if letra in letras_adivinadas:
            print("Ya adivinaste esa letra. Intentá con otra.")
            continue
        letras_adivinadas.append(letra)
        # Verificar si la letra está en la palabra secreta
        if letra in palabra_secreta:
            print(f"¡Bien! La letra '{letra}' está en la palabra.")
            palabra_oculta = "".join([letra if letra in letras_adivinadas else "_" for letra in palabra_secreta])
        else:
            intentos -= 1
            print(f"La letra '{letra}' no está en la palabra. Te quedan {intentos} intentos.")
        print(f"Palabra: {palabra_oculta}")

if __name__ == "__main__":
    ahorcado("jugador anónimo")