from typing import List, Tuple, Iterator

class Board:
    def __init__(self, n: int = 8):
        self.n = n
        self.queens: List[Tuple[int, int]] = []

    def place(self, row: int, col: int):
        if (row, col) not in self.queens:
            self.queens.append((row, col))

    def remove(self, row: int, col: int):
        if (row, col) in self.queens:
            self.queens.remove((row, col))

    def is_safe(self, row: int, col: int) -> bool:
        for q_row, q_col in self.queens:
            if q_col == col:
                return False
            if abs(q_row - row) == abs(q_col - col):
                return False
        return True

    def solve(self) -> int:
        self.queens = []
        count = 0

        def backtrack(current_row: int):
            nonlocal count
            if current_row == self.n:
                count += 1
                return

            for col in range(self.n):
                if self.is_safe(current_row, col):
                    self.place(current_row, col)
                    backtrack(current_row + 1)
                    self.remove(current_row, col)

        backtrack(0)
        return count

    def __len__(self) -> int:
        return len(self.queens)

    def __iter__(self) -> Iterator[Tuple[int, int]]:
        yield from self.queens

    def __contains__(self, pos: Tuple[int, int]) -> bool:
        return pos in self.queens

    def __repr__(self) -> str:
        return f"Board(n={self.n}, queens={self.queens})"

    def __str__(self) -> str:
        res = []
        res.append("  " + " ".join([chr(97+i) for i in range(self.n)]))
        for r in range(self.n - 1, -1, -1):
            line = [f"{r+1}"]
            for c in range(self.n):
                if (r, c) in self.queens:
                    line.append("Q")
                else:
                    line.append("□" if (r + c) % 2 == 0 else "■")
            res.append(" ".join(line))
        return "\n".join(res)

def solve(n: int = 8) -> int:
    return Board(n).solve()

if __name__ == "__main__":
    assert solve(1) == 1
    assert solve(2) == 0
    assert solve(3) == 0
    assert solve(4) == 2
    assert solve(8) == 92

    viz_board = Board(8)

    def find_one_solution(board, row):
        if row == board.n:
            return True
        for col in range(board.n):
            if board.is_safe(row, col):
                board.place(row, col)
                if find_one_solution(board, row + 1):
                    return True
                board.remove(row, col)
        return False

    if find_one_solution(viz_board, 0):
        print(viz_board)
    else:
        print("Nie udało się wygenerować podglądu.")