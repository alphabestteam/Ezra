if __name__ == "__main__":

    good_numbers = False
while not good_numbers:
    try:
        num1 = int(input('enter first number: '))
        num2 = int(input('enter second number: '))
        good_numbers = True
    except ValueError:
        print('please enter valid numbers')

print(num1, num2)
print("Finished running")
