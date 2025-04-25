import random

tablero = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

estado = "jugando"
turnos_jugados = 0

def imprimir_tablero():
    global tablero
    ancho = 9
   
    for fila in range(len(tablero)):
        for columna in range(len(tablero[fila])):
            if columna < 2:
                print("",tablero[fila][columna], end=" |")
            else:
                print("", tablero[fila][columna], end="\n")
        if fila < 2:
            for i in range(2):
                print("---", end="")
                print("+", end="")
            print("---")

def posicion(pos):
    indice = int(input(f"{pos.title()}: ")) - 1
    return indice

def jugar_turno_jugador(usuario):
    global turnos_jugados

    print(f"\nTurno de {usuario}...")
    fila = posicion("fila")
    while fila < 0 or fila > 2:
        print("La fila debe ser 1, 2 o 3.")
        fila = posicion("fila")
    columna = posicion("columna")
    while columna < 0 or columna > 2:
        print("La columna debe ser 1, 2 o 3.")
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
        print("\nTurno de la computadora...")
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
    print(f"¡Hola, {usuario}! Bienvenido/a al juego de tateti.")
    print("El tablero es de 3x3. Ingresá la fila y la columna (1, 2 o 3) donde querés jugar.")

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
        print(f"\n¡Felicitaciones, {usuario}! Ganaste el juego :)")
    elif estado == "perdido":
        print("\nSeguí participando :(")
    else:
        print("\nEs un empate :/")

if __name__ == "__main__":
    tateti("jugador anónimo")