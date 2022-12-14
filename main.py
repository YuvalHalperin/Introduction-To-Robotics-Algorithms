import numpy as np


def BFS_func(matx, x_start, y_start):
    queue = [(x_start, y_start)]
    matx[x_start, y_start] = 0
    rows, cols = np.shape(matx)
    rows, cols = rows - 1, cols - 1

    while queue:
        x, y = queue.pop(0)
        val = matx[x, y]
        if x < rows and matx[x + 1, y] == -2:
            matx[x + 1, y] = val + 1
            queue.append((x + 1, y))
        if x > 0 and matx[x - 1, y] == -2:
            matx[x - 1, y] = val + 1
            queue.append((x - 1, y))
        if y < cols and matx[x, y + 1] == -2:
            matx[x, y + 1] = val + 1
            queue.append((x, y + 1))
        if y > 0 and matx[x, y - 1] == -2:
            matx[x, y - 1] = val + 1
            queue.append((x, y - 1))


mat = np.matrix([[-2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
                 [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
                 [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
                 [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
                 [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
                 [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
                 [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
                 [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
                 [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
                 [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2]])
print(mat)
BFS_func(mat, 1, 4)
print("************* after BFS *************")
print(mat)
print()
print()
mat = np.matrix([[-2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
                 [-2, -2, -2, -2, -2, -2, -2, -1, -1, -1],
                 [-2, -1, -1, -2, -2, -2, -2, -2, -2, -2],
                 [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
                 [-2, -2, -2, -2, -2, -2, -2, -1, -1, -2],
                 [-2, -2, -2, -2, -2, -2, -1, -1, -2, -2],
                 [-2, -2, -1, -1, -1, -2, -1, -2, -2, -2],
                 [-2, -2, -1, -1, -1, -2, -2, -2, -2, -2],
                 [-2, -2, -1, -1, -1, -2, -2, -2, -2, -2],
                 [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2]])
print(mat)
BFS_func(mat, 5, 5)
print("************* after BFS *************")
print(mat)
