#nested list, create a linear list from nested, also find the second largest number in the list, bubble sort use
nest_example = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [1, 2],
]
linear_list = []
for number_list in nest_example:
    for number in number_list:
        linear_list.append(number)
linear_list
n=2
for index in range(n):
    for idx, element in enumerate(linear_list[index + 1:]): #idx and enumerate chai iterate garna ko lagi ho
        print('Indexes: ',index, idx +index + 1)
        print("Element: ", linear_list[index], linear_list[index + idx + 1])
        
        if linear_list[index] < element:
            linear_list[index], linear_list[index + idx + 1]= linear_list[index + idx + 1], linear_list[index]
            print(f"Swapping: {linear_list}")
    print('-'*100)
