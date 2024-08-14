def fizz_buzz():
    # Get input from the user
    fizz_num = int(input("Enter the number for Fizz: "))
    buzz_num = int(input("Enter the number for Buzz: "))
    max_num = int(input("Enter the maximum number to count up to: "))

    # Iterate through the numbers from 1 to max_num
    for i in range(1, max_num + 1):
        if i % fizz_num == 0 and i % buzz_num == 0:
            print("FizzBuzz")
        elif i % fizz_num == 0:
            print("Fizz")
        elif i % buzz_num == 0:
            print("Buzz")
        else:
            print(i)

# Call the function to run the game
fizz_buzz()
