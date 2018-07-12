# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
#matrix = [[1,2],[3,4]]
matrix = []

l = len(matrix)

i = j = 0
arr = []

while i < l:
    j = 0
    while j < l:
        arr.append(matrix[i][j])
        j += 1
    i += 1

i = l-1
while i >= 0:
    j = 0
    while j < l:
        matrix[j][i] = arr.pop(0)
        j += 1
    i -= 1
print(matrix)


