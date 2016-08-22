numbers = [0,0,0,0,0]
for i in range(5):
    try:
        numbers[i] = int(input("Number: "))
    except ValueError:
        print("Invalid Number")
print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The largest number is {}".format(sum(numbers) / len(numbers)))