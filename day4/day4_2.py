import re

def valid_sub(matrix):
    if matrix[0][0] == 'M' and matrix[0][2] == 'M' and matrix[2][0] == 'S' and matrix[2][2] == 'S':
        return True
    if matrix[0][0] == 'M' and matrix[0][2] == 'S' and matrix[2][0] == 'M' and matrix[2][2] == 'S':
        return True
    if matrix[0][0] == 'S' and matrix[0][2] == 'M' and matrix[2][0] == 'S' and matrix[2][2] == 'M':
        return True
    if matrix[0][0] == 'S' and matrix[0][2] == 'S' and matrix[2][0] == 'M' and matrix[2][2] == 'M':
        return True
    
    return False

filename = "./day4/inp.txt"
strings = []
with open(filename) as f:
    for line in f:
        strings.append(line)

count = 0
for i in range(1, len(strings) - 1):
    for j in range(1, len(strings[0]) - 1):
        if strings[i][j] == 'A' and valid_sub([strings[i-1][j-1:j+2], strings[i][j-1:j+2], strings[i+1][j-1:j+2],]):
            count += 1

print(count)
