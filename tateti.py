import random

tablero = [
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "."]
    ]

estado = "jugando"
turnos_jugados = 0

def imprimir_tablero():
    global tablero
    ancho = len(tablero[0]) * 3 + 4
    for i in range(ancho):
        print("-", end="")
    print()   
    for fila in range(len(tablero)):
        print("|", end="  ")
        for columna in range(len(tablero[fila])):
            print(tablero[fila][columna], end="  ")
        print("|")
    for i in range(ancho):
        print("-", end="")
    print()

def posicion(pos):
    indice = int(input(f"{pos.title()}: ")) - 1
    return indice

def jugar_turno_jugador(usuario):
    global turnos_jugados

    print(f"Turno de {usuario}...")
    fila = posicion("fila")
    columna = posicion("columna")

    if tablero[fila][columna] not in ["X", "O"]:
        tablero[fila][columna] = "X"
        turnos_jugados += 1
        imprimir_tablero()
    else:
        print("La posición está ocupada.")
        jugar_turno_jugador(usuario)

def jugar_turno_maquina():
    global tablero
    global turnos_jugados
    fila = random.randint(0, len(tablero)-1)
    columna = random.randint(0, len(tablero[0])-1)
    if tablero[fila][columna] not in ["X", "O"]:
        tablero[fila][columna] = "O"
        turnos_jugados += 1
        print("Turno de la computadora...")
        imprimir_tablero()
    else:
        jugar_turno_maquina()

def evaluar_resultado():
    global tablero
    global estado
    # evaluar filas
    for fila in tablero:
        if fila == ["X", "X", "X"]:
            estado = "ganado"
            return
        elif fila == ["O", "O", "O"]:
            estado = "perdido"
            return
        
    # evaluar columnas
    col0= [tablero[0][0], tablero[1][0], tablero[2][0]]
    if col0 == ["X", "X", "X"]:
        estado = "ganado"
        return
    elif col0 == ["O", "O", "O"]:
        estado = "perdido"
        return
    
    col1 = [tablero[0][1], tablero[1][1], tablero[2][1]]
    if col1 == ["X", "X", "X"]:
        estado = "ganado"
        return
    elif col1 == ["O", "O", "O"]:
        estado = "perdido"
        return
    
    col2 = [tablero[0][2], tablero[1][2], tablero[2][2]]
    if col2 == ["X", "X", "X"]:
        estado = "ganado"
        return
    elif col2 == ["O", "O", "O"]:
        estado = "perdido"
        return
    
    # evaluar diagonales
    diag1 = [tablero[0][0], tablero[1][1], tablero[2][2]]
    if diag1 == ["X", "X", "X"]:
        estado = "ganado"
        return
    elif diag1 == ["O", "O", "O"]:
        estado = "perdido"
        return

    diag2 = [tablero[0][2], tablero[1][1], tablero[2][0]]
    if diag2 == ["X", "X", "X"]:
        estado = "ganado"
        return
    elif diag2 == ["O", "O", "O"]:
        estado = "perdido"
        return

def tateti(usuario):
    global tablero
    global estado
    global turnos_jugados
    usuario = usuario.title()

    while estado == "jugando":
        jugar_turno_jugador(usuario)
        if turnos_jugados > 4:
            evaluar_resultado()
        if turnos_jugados == 9:
            break
        jugar_turno_maquina()
        if turnos_jugados > 4:
            evaluar_resultado()
    
    if estado == "ganado":
        print(f"¡Felicitaciones, {usuario}! Ganaste el juego :)")
    elif estado == "perdido":
        print("Seguí participando :(")
    else:
        print("Es un empate :/")

if __name__ == "__main__":
    tateti("usuario")