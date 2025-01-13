total = 0
array = [1, 2, 3, 3, 4, 3, 2, 1]

for i in array:
    print(f"the current element to be added is: {array[i]}") 
    total += array[i]  

if total % 2 == 0:
    print("the sum is even!")
else:
    print("the sum is odd!")

average = total / len(array)
print(f"The average of the array elements is: {average}"

if average > 2:
    print("The average is greater than 2")
else:
    print("The average is 2 or less")