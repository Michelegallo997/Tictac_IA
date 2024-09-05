
def crear_tablero():
    return [[" " for _ in range(3)] for _ in range(3)]

def mostrar_tablero(tablero):
    for fila in tablero:
        print("|".join(fila))
        print("-" * 5)
        
def hacer_movimiento(jugador, tablero, fila, columna):
    if tablero[fila][columna] == " ":
        tablero[fila][columna] = jugador
        return True
    else:
        return False



def verificar_ganador(tablero):
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] != " ":
            return fila[0]
    for col in range(3):
        if tablero[0][col] == tablero[1][col] == tablero[2][col] != " ":
            return tablero[0][col]
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
        return tablero[0][2]
    return None

def minimax(tablero, profundidad, jugador):
    if verificar_ganador(tablero) == 'X':
        return -10
    if verificar_ganador(tablero) == 'O':
        return 10
    if all(all(c != ' ' for c in fila) for fila in tablero):
        return 0

    if jugador == 'O':
        mejor_valor = -1000
        for fila in range(3):
            for columna in range(3):
                if tablero[fila][columna] == ' ':
                    tablero[fila][columna] = jugador
                    valor = minimax(tablero, profundidad + 1, 'X')
                    tablero[fila][columna] = ' '
                    mejor_valor = max(mejor_valor, valor)
        return mejor_valor
    else:
        mejor_valor = 1000
        for fila in range(3):
            for columna in range(3):
                if tablero[fila][columna] == ' ':
                    tablero[fila][columna] = jugador
                    valor = minimax(tablero, profundidad + 1, 'O')
                    tablero[fila][columna] = ' '
                    mejor_valor = min(mejor_valor, valor)
        return mejor_valor

def mejor_movimiento(tablero):
    mejor_valor = -1000
    mejor_movimiento = (-1, -1)
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == ' ':
                tablero[fila][columna] = 'O'
                valor_movimiento = minimax(tablero, 0, 'X')
                tablero[fila][columna] = ' '
                if valor_movimiento > mejor_valor:
                    mejor_valor = valor_movimiento
                    mejor_movimiento = (fila, columna)
    return mejor_movimiento

jugadores = ['X', 'O']
turno = 0
tablero = crear_tablero()

while True:
    jugador_actual = jugadores[turno % 2]
    print(f"Es turno del jugador {jugador_actual}")
    mostrar_tablero(tablero)

    if jugador_actual == 'X':
        fila = int(input("Ingrese el número de fila (0, 1, 2): "))
        columna = int(input("Ingrese el número de columna (0, 1, 2): "))
    else:
        fila, columna = mejor_movimiento(tablero)

    if hacer_movimiento(jugador_actual, tablero, fila, columna):
        ganador = verificar_ganador(tablero)
        if ganador is not None:
            print(f"El jugador {ganador} ha ganado!")
            break
        elif all(all(c != " " for c in fila) for fila in tablero):
            print("¡Empate!")
            break
        turno += 1
    else:
        print("Movimiento inválido. Inténtalo de nuevo")
11