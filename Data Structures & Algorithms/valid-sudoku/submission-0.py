class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cells = {}
        rows = {}
        columns = {}

        for row in range(len(board)):
            for column in range(len(board[0])):
                key = (row // 3, column // 3)
                value = board[row][column]
                if value == ".":
                    continue

                if value in cells.get(key, set()):
                    return False

                if value in rows.get(row, set()):
                    return False

                if value in columns.get(column, set()):
                    return False

                cells.setdefault(key, set()).add(value)
                rows.setdefault(row, set()).add(value)
                columns.setdefault(column, set()).add(value)

        return True