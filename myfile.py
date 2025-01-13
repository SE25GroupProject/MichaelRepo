def analyze_array(array):
    total = 0

    for i in array:
        print(f"The current element to be added is: {i}")  # Corrected to use i directly
        total += i  # Corrected to use i directly

    if total % 2 == 0:
        print("The sum is even!")
    else:
        print("The sum is odd!")

    average = total / len(array)
    print(f"The average of the array elements is: {average}")

    if average > 2:
        print("The average is greater than 2")
    else:
        print("The average is 2 or less")

    return total, average