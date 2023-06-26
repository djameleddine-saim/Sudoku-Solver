from solver import Solver

class BacktrackingSolver(Solver):
    def solve_sudoku(self):
        # Fonction pour résoudre le Sudoku en utilisant la méthode du backtracking
        find = self.find_empty_location()
        if not find:
            return True
        else:
            row, col = find

        for num in range(1, 10):
            if self.is_valid(str(num), row, col):
                self.grid[row][col] = str(num)
                if self.solve_sudoku():
                    return True
                self.grid[row][col] = '_'

        return False