numbers=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

numbers_2 = [
    [4, 2, 6],
    [7, 2, 1],
    [3, 5, 4]
]

result=[
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


for i in range(3):
    for j in range(3):
        result[i][j]=numbers[i][j]+numbers_2[i][j]
print(result)


'''for i in range(3):
    print(numbers[i][i])'''



'''print(numbers[2][1])
print("\n")
for i in range(3):
    for j in range(3):
        print(numbers[i][j])'''



'''user_list=[]

rows=int(input("How many rows do you want? "))
cols=int(input("How many columns do you want? "))

for i in range(rows):
    row = []
    for j in range(cols):
        col=input("Enter your number: ")
        row.append(col)
    user_list.append(row)

print(user_list)'''