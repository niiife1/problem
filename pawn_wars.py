def positionrow(row):
    if row == 0: return 8
    if row == 1: return 7
    if row == 2: return 6
    if row == 3: return 5
    if row == 4: return 4
    if row == 5: return 3
    if row == 6: return 2
    if row == 7: return 1
def position(col):
    if col == 0: return "a"
    if col == 1: return "b"
    if col == 2: return "c"
    if col == 3: return "d"
    if col == 4: return "e"
    if col == 5: return "f"
    if col == 6: return "g"
    if col == 7: return "h"

withe_row = 0
withe_col = 0
black_row = 0
black_col = 0
matrix = []
for row in range(8):
    row_elements = list(input().split())
    for col in range(8):
        if row_elements[col] == "w":
            withe_row = row
            withe_col = col
        if row_elements[col] == "b":
            black_row = row
            black_col = col
        matrix.append(row_elements)

for col in range(8):
    if [withe_row - 1, withe_col - 1] == [black_row, black_col]:
        [withe_row,withe_col] = [black_row, black_col]
        withe_col = position(withe_col)
        withe_row = positionrow(withe_row)
        print(f"Game over! White win, capture on {withe_col}{withe_row}.")
        break

    if [withe_row - 1, withe_col + 1] == [black_row, black_col]:
        [withe_row, withe_col] = [black_row, black_col]
        withe_col = position(withe_col)
        withe_row = positionrow(withe_row)
        print(f"Game over! White win, capture on {withe_col}{withe_row}.")
        break
    withe_row -= 1
    if [black_row + 1 , black_col -1] == [withe_row,withe_col]:
        [black_row, black_col] = [withe_row,withe_col]
        black_col = position(black_col)
        black_row =positionrow(black_row)
        print(f"Game over! Black win, capture on {black_col}{black_row}.")
        break

    if [black_row + 1 , black_col + 1] == [withe_row, withe_col]:
        [black_row, black_col] = [withe_row, withe_col]
        black_col = position(black_col)
        black_row = positionrow(black_row)
        print(f"Game over! Black win, capture on {black_col}{black_row}.")
        break
    black_row += 1
    if withe_row == 0:
        withe_col = position(withe_col)
        print(f"Game over! White pawn is promoted to a queen at {withe_col}{abs(withe_row-8)}.")
        break

    if black_row == 8:
        black_col = position(black_col)
        print(f"Game over! Black pawn is promoted to a queen at {black_col}{abs(black_row - 7)}.")
        break