def clear_plus(matrix, x=0, y=0):
    if x == len(matrix):
        return
    
    if y == len(matrix[x]):
        clear_plus(matrix, x+1, 0)
        return

    if matrix[x][y] == '+':
        matrix[x][y] = '.'

    clear_plus(matrix, x, y + 1)


def shi_maze(matrix, x, y):
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < len(matrix) and 0 <= ny < len(matrix[nx])): continue
        if matrix[nx][ny] == 'E':
            if matrix[x][y] != 'S':
                matrix[x][y] = '*'
            clear_plus(matrix)
            print('Solution found:')
            for row in matrix:
                print(''.join(row))
            return True

        if matrix[nx][ny] == '.':
            if matrix[x][y] != 'S':
                matrix[x][y] = '*'
            if shi_maze(matrix, nx, ny):
                return True

    if matrix[x][y] != 'S':
        matrix[x][y] = '+'
    return False

def find_S(matrix, x=0, y=0):
    if x == len(matrix):
            return
        
    if y == len(matrix[x]):
        find_S(matrix, x+1, 0)
        return

    if matrix[x][y] == 'S':
        return x, y

    find_S(matrix, x, y + 1)


ip = input("Enter the entire maze in one line. Use '.' for open cells, '#' for walls, 'S' for start, and 'E' for end.\nSeparate each row with a comma (,).\nEnter the maze: ").strip().split(',')
matrix = [list(x) for x in ip]
print('Your maze:')
for row in matrix:
    print(''.join(row))
sx, sy = find_S(matrix)
if not shi_maze(matrix, sx, sy):
    print("No solution found")