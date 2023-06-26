from solver import Solver

class BruteForceSolver(Solver):
    def solve_with_brute_force(self):
        # Fonction pour résoudre le Sudoku en utilisant la méthode de force brute
        empty_locations = []
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == '_':
                    empty_locations.append((row, col))

        index = 0
        while index < len(empty_locations):
            row, col = empty_locations[index]
            if self.grid[row][col] == '_':
                num = 1
            else:
                num = int(self.grid[row][col]) + 1
            found = False

            while not found and num <= 9:
                if self.is_valid(str(num), row, col):
                    self.grid[row][col] = str(num)
                    found = True
                else:
                    num += 1

            if found:
                index += 1
            else:
                self.grid[row][col] = '_'
                index -= 1

                if index < 0:
                    # La grille n'est pas résoluble
                    return False

        return True
