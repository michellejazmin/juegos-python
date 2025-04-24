import random

def ruleta_rusa(usuario):
    jugador1 = usuario.title()
    print(f"¡Hola, {jugador1}! Bienvenido/a al juego de la ruleta rusa.")
    jugador2 = input("¿Cómo se llama tu oponente? ").title()
    print(f"¡Hola, {jugador2}! Bienvenido/a al juego de la ruleta rusa.")
    print("El juego consiste en disparar un revólver con una sola bala en el tambor.")
    print("Hay 5 turnos para disparar.")
    print("Si el tambor está vacío, el jugador no se muere.")
    print("Si el tambor tiene una bala, el jugador se muere.")
    
    tambor = [0, 0, 0, 0]  # 0 representa que no hay bala, 1 representa la bala
    # Colocar la bala en una posición aleatoria
    tambor.insert(random.randint(0, 4), 1)
    print("El tambor ha sido cargado. ¡Que comience el juego!")

    # Bucle principal del juego
    for turno in range(5):
        print(f"\nTurno {turno + 1}:")
        if turno % 2 == 0:
            jugador_actual = jugador1
        else:
            jugador_actual = jugador2
        
        print(f"Es el turno de {jugador_actual}.")
        disparo = input("¿Disparar? (s/n): ").lower()
        
        if disparo == "s":
            if tambor[turno % 5] == 1:
                print(f"¡Bang! {jugador_actual} ha muerto :(")
                break
            else:
                print(f"{jugador_actual} sobrevive.")
        elif disparo == "n":
            print(f"{jugador_actual} decide no disparar.")
        else:
            print("Opción inválida. Debe responder 's' o 'n'.")
            continue
    else:
        print("El juego ha terminado. Ambos jugadores han sobrevivido.")
    print("¡Gracias por jugar a la ruleta rusa!")
    
if __name__ == "__main__":
    ruleta_rusa("jugador anónimo")