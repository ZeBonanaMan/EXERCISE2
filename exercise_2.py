print("Printing current and previous number and their sum in a range(10)")
previous_num = 0
numbers = range(1,10)

for i in numbers:
    sum_equation = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", sum_equation)
    previous_num = i