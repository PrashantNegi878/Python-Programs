def spirallyTraverse(self, matrix, r, c):
    arr = []
    top = 0
    down = r - 1
    left = 0
    right = c - 1
    dirr = 0
    while (left <= right and top <= down):
        if (dirr == 0):
            for i in range(left, right + 1):
                arr.append(matrix[top][i])
            top += 1
        if (dirr == 1):
            for i in range(top, down + 1):
                arr.append(matrix[i][right])
            right -= 1
        if (dirr == 2):
            i = right
            while (i >= left):
                arr.append(matrix[down][i])
                i -= 1
            down -= 1
        if (dirr == 3):
            i = down
            while (i >= top):
                arr.append(matrix[i][left])
                i -= 1
            left += 1
        dirr = (dirr + 1) % 4
    return arr