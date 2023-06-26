class Solver:
    def __init__(self, grid):
        self.grid = grid

    def find_empty_location(self):
        # Fonction pour trouver une case vide dans la grille
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == '_':
                    return row, col
        return None

    def is_valid(self, num, row, col):
        # Fonction pour vérifier si un numéro est valide dans une position donnée
        # Vérification de la ligne
        for i in range(9):
            if self.grid[row][i] == num:
                return False
        # Vérification de la colonne
        for i in range(9):
            if self.grid[i][col] == num:
                return False
        # Vérification de la région 3x3
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if self.grid[i + start_row][j + start_col] == num:
                    return False
        return True