import math

# Función que implementa el algoritmo Minimax con poda alfa-beta
def minimax_alpha_beta(board, depth, is_maximizing, alpha, beta):
    # Comprobar si el juego ha terminado y devolver el valor de la posición
    if check_winner(board, 'X'):  # Si el jugador 'X' ha ganado, devolver -1
        return -1
    elif check_winner(board, 'O'):  # Si el jugador 'O' ha ganado, devolver 1
        return 1
    elif check_draw(board):  # Si el juego ha terminado en empate, devolver 0
        return 0

    if is_maximizing:  # Si es el turno del maximizador (jugador 'O')
        best_score = -math.inf  # Inicializar el mejor puntaje como menos infinito
        # Recorrer todas las celdas del tablero
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':  # Si la celda está vacía
                    board[i][j] = 'O'  # Colocar la ficha 'O' en la celda
                    # Llamar recursivamente a minimax_alpha_beta para evaluar la posición después de este movimiento
                    score = minimax_alpha_beta(board, depth+1, False, alpha, beta)
                    board[i][j] = ''  # Deshacer el movimiento
                    best_score = max(score, best_score)  # Actualizar el mejor puntaje
                    alpha = max(alpha, best_score)  # Actualizar alfa
                    if beta <= alpha:  # Poda beta
                        break  # Salir del bucle si ya no es necesario evaluar más movimientos
        return best_score  # Devolver el mejor puntaje encontrado
    else:  # Si es el turno del minimizador (jugador 'X')
        best_score = math.inf  # Inicializar el mejor puntaje como infinito
        # Recorrer todas las celdas del tablero
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':  # Si la celda está vacía
                    board[i][j] = 'X'  # Colocar la ficha 'X' en la celda
                    # Llamar recursivamente a minimax_alpha_beta para evaluar la posición después de este movimiento
                    score = minimax_alpha_beta(board, depth+1, True, alpha, beta)
                    board[i][j] = ''  # Deshacer el movimiento
                    best_score = min(score, best_score)  # Actualizar el mejor puntaje
                    beta = min(beta, best_score)  # Actualizar beta
                    if beta <= alpha:  # Poda alfa
                        break  # Salir del bucle si ya no es necesario evaluar más movimientos
        return best_score  # Devolver el mejor puntaje encontrado


# Función para obtener el mejor movimiento utilizando Minimax con poda alfa-beta
def get_best_move(board):
    best_score = -math.inf
    best_move = ()
    alpha = -math.inf
    beta = math.inf
    # Recorrer todos los movimientos posibles y encontrar el mejor puntaje y movimiento
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                board[i][j] = 'O'
                score = minimax_alpha_beta(board, 0, False, alpha, beta)
                board[i][j] = ''
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

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
print_board(board)

# Loop principal del juego
while not check_winner(board, 'X') and not check_winner(board, 'O') and not check_draw(board):
    x, y = map(int, input("Enter your move (row and column): ").split())
    if board[x][y] == '':
        board[x][y] = 'X'
        print_board(board)
        if check_winner(board, 'X'):
            print("You win!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break
        best_move = get_best_move(board)
        board[best_move[0]][best_move[1]] = 'O'
        print("Computer's move:")
        print_board(board)
        if check_winner(board, 'O'):
            print("You lose!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break
    else:
        print("Invalid move. Try again.")
