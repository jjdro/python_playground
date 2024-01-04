import time

while True:
    print("lets count!")

    # Wait for user input
    countTo = int(input("What number should I count to? "))

    # Count from 11 to countTo
    for i in range(1, countTo+1):
        print(i)
        time.sleep(.1)

    # Ask if the user wants to count more or quit
    choice = input("Do you want to count more? (yes/no) ")
    if choice.lower() == 'no' or choice.lower() == 'n':
        print("Ok, goodbye!")
        break


print("Goodbye!")

