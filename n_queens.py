def n_queens(n):
    res = []

    def backtrack(row, cols, diag1, diag2, path):
        if row == n:
            res.append(path[:])
            return
        for col in range(n):
            if col in cols or (row + col) in diag1 or (row - col) in diag2:
                continue
            # Place queen
            cols.add(col)
            diag1.add(row + col)
            diag2.add(row - col)
            path.append(col)

            backtrack(row + 1, cols, diag1, diag2, path)

            # Remove queen (backtrack)
            cols.remove(col)
            diag1.remove(row + col)
            diag2.remove(row - col)
            path.pop()

    backtrack(0, set(), set(), set(), [])
    return res

# Example: print solutions for 4-queens
print(n_queens(4))
