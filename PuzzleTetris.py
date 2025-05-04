import copy

# Tablero objetivo (0: vacío, 1: espacio a llenar)
# Puedes adaptar este tablero con la forma que necesites
# board = [
#     [1, 1, 1, 1, 0, 1, 0],
#     [1, 1, 1, 1, 1, 1, 0],
#     [1, 1, 0, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 0, 0, 0, 0]
# ]

board = [
    [1, 1, 1, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 0],
    [1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0]
]

# Piezas tipo Tetris (puedes agregar más)
# pieces = [
#     [[0, 1, 1, 1],[1, 1, 0, 0]],  # rojo
#     [[1, 1, 1], [1, 1, 0]],  # verde
#     [[1, 1, 1], [1, 1, 1]],  # amarillo
#     [[0, 0, 1, 0], [1, 1, 1, 1]],  # azul oscuro
#     [[1, 1, 1], [1, 0, 1]],  # azul claro
#     [[1, 0, 0, 0], [1, 1, 1, 1]],  # blanco
#     [[1, 0, 0], [1, 0, 0], [1, 1, 1]],  # morado oscuro
#     [[1, 1, 0], [0, 1, 0], [0, 1, 1]]  # morado claro
# ]

pieces = [
    [[1, 1, 1],      # Pieza tipo L
     [1, 0, 0],
     [1, 0, 0]],
    
    [[1, 1, 1, 1],      # Pieza tipo L
     [1, 0, 0, 0]],
    
    [[1, 1, 1, 1],      # Pieza tipo 
     [0, 1, 0, 0]],
    
    [[1, 0, 1],      # Pieza tipo C
     [1, 1, 1]],
    
    [[1, 1, 1],      # Pieza tipo 
     [1, 1, 1]],
    
    [[0, 0, 1],      # Pieza tipo S
     [1, 1, 1],
     [1, 0, 0]],
    
    [[1, 0],      # Pieza tipo S
     [1, 1],
     [0, 1],
     [0, 1]],
    
    [[1, 1, 0],      # Pieza tipo S
     [1, 1, 1]]
]

def rotate(piece):
    return [list(row) for row in zip(*piece[::-1])]

def get_all_rotations(piece):
    rotations = []
    for _ in range(4):
        piece = rotate(piece)
        if piece not in rotations:
            rotations.append(copy.deepcopy(piece))
    return rotations

def can_place(board, piece, r, c):
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            if piece[i][j] == 1:
                if r + i >= len(board) or c + j >= len(board[0]) or board[r + i][c + j] != 1:
                    return False
    return True

def place_piece(board, piece, r, c, mark):
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            if piece[i][j] == 1:
                board[r + i][c + j] = mark

# ✅ Imprime el tablero con emojis
def print_board(board):
    symbol_map = {
        0: '⬛',  # Bloque vacío
        1: '⬜',  # Espacio libre aún no ocupado
        2: '🟥',  # Pieza 1
        3: '🟦',  # Pieza 2
        4: '🟩',  # Pieza 3
        5: '🟨',  # Pieza 4
        6: '🟪',  # Pieza 5
        7: '🟧',  # Pieza 6
        8: '🟫',  # Pieza 7
        9: '🟩',  # Pieza 8
        10: '🟡', # Pieza 9
        11: '🟠', # Pieza 10
        12: '🟢', # Pieza 11
    }
    for row in board:
        print(''.join(symbol_map.get(cell, '?') for cell in row))
    print()

def solve(board, pieces, idx=0):
    if idx == len(pieces):
        print("✅ Solución encontrada:")
        print_board(board)
        return True

    for rotation in get_all_rotations(pieces[idx]):
        for r in range(len(board)):
            for c in range(len(board[0])):
                if can_place(board, rotation, r, c):
                    place_piece(board, rotation, r, c, idx + 2)
                    if solve(board, pieces, idx + 1):
                        return True
                    place_piece(board, rotation, r, c, 1)
    return False

# Ejecutar el solver
if not solve(copy.deepcopy(board), pieces):
    print("❌ No se encontró solución.")
