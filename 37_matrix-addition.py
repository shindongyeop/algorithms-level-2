def solution(arr1, arr2):
    answer = []  # Initialize an empty list

    for i in range(len(arr1)):  # Loop over each row
        row = [0] * len(arr1[0])  # Create a row of zeros
        answer.append(row)  # Add the row to the answer

    print(answer)
    for i in range(len(arr1)): # going through each row
        for j in range(len(arr1[i])): # going through each column of each row
            print(f'i(row): {i}, j(col): {j}, arr1[i][j]: arr1[{i}][{j}], arr2[i][j]: arr2[{i}[{j}]') 
            answer[i][j] = arr1[i][j] + arr2[i][j]
    
    return answer

print(solution([[1, 2, 3], [2, 3, 4]], [[3, 4, 5], [5, 6, 7]])) # [[4, 6], [7, 9]]

def solution2(arr1, arr2):
    answer = []  # Initialize an empty list

    for i in range(len(arr1)):  # Loop over each row.
        row = []  # Create an empty row
        for j in range(len(arr1[i])):  # Loop over columns
            row.append(arr1[i][j] + arr2[i][j])  # Sum elements and append
        answer.append(row)  # Append the computed row to answer

    return answer

arr1 = [[1, 2, 3], [2, 3, 4]]
arr2 = [[3, 4, 5], [5, 6, 7]]

print(solution2(arr1, arr2))

# 
# answer = [] # initialize answer
# 
# for i in range(len(arr1)) means:
# for i in range(2) means:
# for i in range(0, 2):
# 
#   row = [] # initialize row
# 
#   for j in range(len(arr1[i])) means:
#   for j in range(len([1, 2, 3])) means:
#   for j in range((3)) means:
#   for j in range(0, 3):

#   when i = 0 and j = 0
#       row.append(arr1[i][j] + arr2[i][j]) means
#       row.append(arr1[0][0] + arr2[0][0]) means
# 
#       [].append(1 + 3) which is [4]

#   when i = 0 and j = 1
#       row.append(arr1[i][j] + arr2[i][j]) means
#       row.append(arr1[0][1] + arr2[0][1]) means
#       
#       [4].append(2 + 4) which is [4, 6]

# 
#   when i = 0 and j = 2
#       row.append(arr1[i][j] + arr2[i][j]) means
#       row.append(arr1[0][2] + arr2[0][2]) means
#   
#       [4, 6].append(3 + 5) which is [4, 6, 8]
#   
#   answer.append(row) means:
#   [].append[4, 6, 8] which means: [[4, 6, 8]], now do the same with i = 1
# 

def solution3(arr1, arr2):
    answer = arr1
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            answer[i][j] += arr2[i][j]
    return answer


print(solution3([[1, 2], [2, 3]], [[3, 4], [5, 6]]))

print(len([[1, 2, 3], [2, 3, 4]]))  # 

matrix = [[1, 2, 3], [2, 3, 4]]
print(f'length of the rows: {len(matrix)}')  # 2
print(f'length of the cols: {len(matrix[0])}')  # 3