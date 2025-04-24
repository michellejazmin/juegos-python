from ahorcado import ahorcado
from tateti import tateti
from ruleta import ruleta
from ruleta_rusa import ruleta_rusa

def bienvenida():
    global usuario
    print("¡Hola!")
    usuario = input("¿Cómo te llamás?: ").title()
    print(f"¡Bienvenido/a, {usuario}! :)")

def elegir_juego():
    global juego
    juego = input("¿Qué juego querés jugar?\n1: tateti\n2: ahorcado\n3: ruleta\n4: ruleta rusa\nElija el número del juego: ")
    if juego.isdigit() and 1 <= int(juego) <= 4:
        juego = juegos_disponibles[int(juego) - 1][1]
    else:
        print("Opción inválida. Debe elegir un número entre 1 y 4.")
        elegir_juego()
    comenzar_juego(juego)

def comenzar_juego(juego):
    print(f"Iniciando el juego de {juego}...")
    if juego == "tateti":
        tateti(usuario)
    elif juego == "ahorcado":
        ahorcado(usuario)
    elif juego == "ruleta":
        ruleta(usuario)
    elif juego == "ruleta rusa":
        ruleta_rusa(usuario)

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

juegos_disponibles = [
    [1, "tateti"],
    [2, "ahorcado"],
    [3, "ruleta"],
    [4, "ruleta rusa"]
]

juego = ""

bienvenida()
elegir_juego()
