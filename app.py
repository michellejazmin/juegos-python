from ahorcado import ahorcado
from tateti import tateti

def bienvenida():
    global usuario
    print("¡Hola!")
    usuario = input("¿Cómo te llamás?: ").title()
    print(f"¡Bienvenido/a, {usuario}! :)")

def elegir_juego():
    global juego
    juego = input("¿Qué juego desea jugar? ")
    comenzar_juego(juego)

def comenzar_juego(juego):
    if juego == "tateti":
        print("Iniciando el juego de tateti...")
        tateti(usuario)
    elif juego == "ahorcado":
        print("Iniciando el juego de ahorcado...")
        ahorcado(usuario)
    else:
        print("El juego elegido no está disponible.")
        ofrecer_otro_juego()

def ofrecer_otro_juego():
    respuesta = input("Desea jugar otro juego? (si/No): ")
    if respuesta.lower() == "si":
        elegir_juego()
    elif respuesta.lower() == "no" or respuesta == "":
        print(f"¡Hasta la próxima, {usuario}!")
    else:
        print("Respuesta inválida. Debe responder \"si\" o \"no\".")
        ofrecer_otro_juego()

usuario = ""
juego = ""
bienvenida()
elegir_juego()