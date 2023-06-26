class SudokuGrid:
    def __init__(self, grid):
        self.grid = grid

    def print_grid(self):
        # Fonction pour afficher la grille du Sudoku
        for i in range(9):
            for j in range(9):
                print(self.grid[i][j], end=" ")
            print()