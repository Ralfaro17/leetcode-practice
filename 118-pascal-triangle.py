# numRows is the argument LeetCode uses
numRows = 5

result = []

for row in range(1, numRows + 1, 1):
    temp = []
    for column in range(row):
        if row <= 2:
            temp.append(1)
        else:
            if column - 1 < 0 or column > row - 2:
                temp.append(1)
            else:
                temp.append(result[row - 2][column - 1] + result[row - 2][column])
    result.append(temp)

print(result)
# return result
