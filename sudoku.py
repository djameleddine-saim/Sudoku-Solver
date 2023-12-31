import time
from sudokuGrid import SudokuGrid
from BacktrackingSolver import BacktrackingSolver


def read_grid_from_file(filename):
    # Fonction pour lire la grille Sudoku à partir d'un fichier texte
    grid = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            row = list(line.strip())
            grid.append(row)
    return grid



# Lecture de la grille Sudoku à partir du fichier
grid = read_grid_from_file("grid/sudoku.txt")

# Création d'une instance de SudokuGrid
sudoku_grid = SudokuGrid(grid)

print("Grille de Sudoku initiale :")
sudoku_grid.print_grid()
print("\nRésolution en cours...\n")

# Création d'une instance de BacktrackingSolver
backtracking_solver = BacktrackingSolver(grid)

start_time = time.time()
backtracking_solver.solve_sudoku()
end_time = time.time()
execution_time_backtracking = end_time - start_time

# Affichage du temps d'exécution
print("Temps d'exécution de la méthode du backtracking : ", execution_time_backtracking, " secondes")


print("Grille de Sudoku résolue avec la méthode du backtracking :")
sudoku_grid.print_grid()
