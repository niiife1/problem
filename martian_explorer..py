def get_next_pos(row, col, command):
    if command == "up":
        return row - 1, col
    if command == "right":
        return  row ,col + 1
    if command == "down":
        return row + 1, col
    if command == "left":
        return row , col - 1

rows = 6
cols = 6
player_row = 0
player_col = 0
metal = 0
concrete = 0
water = 0
matrix = []
for row in range(rows):
    row_elements = list(input().split())
    for col in range(cols):
        if row_elements[col] == "E":
            player_row = row
            player_col = col
    matrix.append(row_elements)
comands = input().split(", ")

for comand in comands:
        next_row, next_col = get_next_pos(player_row, player_col, comand)
        player_row, player_col = next_row, next_col

        if matrix[next_row][next_col] == "W":
            water += 1
            print(f'Water deposit found at ({next_row},{next_col})')

        if matrix[next_row][next_col] == "C":
            concrete += 1
            print(f"Concrete deposit found at ({next_row},{next_col})")

        if matrix[next_row][next_col] == "M":
            metal += 1
            print(f"Metal deposit found at ({next_row},{next_col})")

        if matrix[next_row][next_col] == "R":
            print(f'Rover got broken at{next_row},{next_col}')
            break


if water >=1 and  concrete >= 1 and  metal >= 1:
    print("Area suitable to start the colony.")

else:
    print("Area not suitable to start the colony.")
