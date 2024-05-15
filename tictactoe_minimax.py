import math

# Función que implementa el algoritmo Minimax
def minimax(board, depth, is_maximizing):
    # Comprobar si el juego ha terminado y devolver el valor de la posición
    if check_winner(board, 'X'):  # Si el jugador 'X' gana, devolver -1
        return -1
    elif check_winner(board, 'O'):  # Si el jugador 'O' gana, devolver 1
        return 1
    elif check_draw(board):  # Si es un empate, devolver 0
        return 0

    if is_maximizing:  # Si es el turno de maximizar (jugador 'O')
        best_score = -math.inf  # Inicializar el mejor puntaje como menos infinito
        # Recorrer todas las celdas del tablero
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':  # Si la celda está vacía
                    board[i][j] = 'O'  # Colocar la ficha 'O' en la celda
                    # Llamar recursivamente a minimax para evaluar la posición después de este movimiento
                    score = minimax(board, depth+1, False)
                    board[i][j] = ''  # Deshacer el movimiento
                    best_score = max(score, best_score)  # Actualizar el mejor puntaje
        return best_score  # Devolver el mejor puntaje encontrado
    else:  # Si es el turno de minimizar (jugador 'X')
        best_score = math.inf  # Inicializar el mejor puntaje como infinito
        # Recorrer todas las celdas del tablero
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':  # Si la celda está vacía
                    board[i][j] = 'X'  # Colocar la ficha 'X' en la celda
                    # Llamar recursivamente a minimax para evaluar la posición después de este movimiento
                    score = minimax(board, depth+1, True)
                    board[i][j] = ''  # Deshacer el movimiento
                    best_score = min(score, best_score)  # Actualizar el mejor puntaje
        return best_score  # Devolver el mejor puntaje encontrado

# Función para obtener el mejor movimiento utilizando Minimax
def get_best_move(board):
    best_score = -math.inf  # Inicializar el mejor puntaje como menos infinito
    best_move = ()  # Inicializar el mejor movimiento como una tupla vacía
    # Recorrer todas las celdas del tablero
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':  # Si la celda está vacía
                board[i][j] = 'O'  # Colocar la ficha 'O' en la celda
                # Llamar a la función minimax para evaluar la posición después de este movimiento
                score = minimax(board, 0, False)
                board[i][j] = ''  # Deshacer el movimiento
                if score > best_score:  # Si el puntaje es mejor que el mejor puntaje actual
                    best_score = score  # Actualizar el mejor puntaje
                    best_move = (i, j)  # Actualizar el mejor movimiento
    return best_move  # Devolver el mejor movimiento encontrado


# Función para comprobar si un jugador ha ganado
def check_winner(board, player):
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]):  # Comprobar filas
            return True
        if all([board[j][i] == player for j in range(3)]):  # Comprobar columnas
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):  # Comprobar diagonales
        return True
    return False

# Función para comprobar si el juego ha terminado en empate
def check_draw(board):
    return all([all([cell != '' for cell in row]) for row in board])

# Función para imprimir el tablero
def print_board(board):
    for row in board:
        print(row)


# Inicializar el tablero
board = [['', '', ''],
         ['', '', ''],
         ['', '', '']]
print("Welcome to Tic-Tac-Toe!")
print("You are playing as 'X'. Enter your moves by specifying the row and column numbers (0-2).")
print_board(board)  # Imprimir el tablero vacío

# Loop principal del juego
while not check_winner(board, 'X') and not check_winner(board, 'O') and not check_draw(board):
    x, y = map(int, input("Enter your move (row and column): ").split())  # Leer la jugada del jugador
    if board[x][y] == '':  # Verificar si la celda está vacía
        board[x][y] = 'X'  # Colocar la ficha 'X' en la celda
        print_board(board)  # Imprimir el tablero después de la jugada del jugador
        if check_winner(board, 'X'):  # Verificar si el jugador 'X' ha ganado
            print("You win!")
            break
        elif check_draw(board):  # Verificar si el juego ha terminado en empate
            print("It's a draw!")
            break
        best_move = get_best_move(board)  # Obtener el mejor movimiento para la AI
        board[best_move[0]][best_move[1]] = 'O'  # Colocar la ficha 'O' en el mejor movimiento
        print("Computer's move:")
        print_board(board)  # Imprimir el tablero después del movimiento de la AI
        if check_winner(board, 'O'):  # Verificar si la AI ha ganado
            print("You lose!")
            break
        elif check_draw(board):  # Verificar si el juego ha terminado en empate
            print("It's a draw!")
            break
    else:
        print("Invalid move. Try again.")  # Mensaje de error si la celda no está vacía
