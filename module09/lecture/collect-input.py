# %%
## Command-line input
    # When you start a program by using python3, you give it the name of the file to start. 
    # You can also give it a set of arguments: data that the program will have access to when running. 
    # Here's how that can look (in a console): 
    # python3 backup.py 2023-01-01

# %%
## Command-line arguments
    # How are these commands captured on the coding side of things? 
    # By using the sys module, you can retrieve the command-line arguments and use them in your program. 
    # Look at the following code:

import sys

print(sys.argv)
print(sys.argv[0])  # program name
print(sys.argv[1])  # first arg

    # sys.argv is an array or a data structure that contains many items. 
    # The first position, denoted as 0 in the array, contains the program name. 
    # The second position, 1, contains your first argument. 
    # Assume that the program collect-input.py contains the sample code and you run it like this:
        # python collect-input.py 2023-01-01
    # The program then yields the following result:
        # ['collect-input.py', '2023-01-01']
        # collect-input.py
        # 2023-01-01

# %%
## User input
    # Another way to pass data to the program is having the user enter the data. 
    # You can code it so the program tells the user to enter information. 
    # You save that entered data in the program and then act on it.
    
    # To capture information from the user, you'll use the input() function. 
    # Here's an example:

print("Welcome to the greeter program")
name = input("Enter your name: ")
print("Greetings " + name)

    # After you enter a value and press Enter, the greeting is returned:
        # Welcome to the greeter program
        # Enter your name: Picard
        # Greetings Picard

# %%
## Working with numbers
    # The input() function stores a result as a string, so the following code might not do what you want it to:

print("calculator program")
first_number = input("first number: ")
second_number = input("second number: ")
print(first_number + second_number)

    # Running this program invites you to input the first number, let's say 3:
        # calculator program
        # first number: 3

    # After you press Enter, you can enter the second number, let's say 4:
        # calculator program
        # first number: 3
        # second number: 4

    # Pressing Enter give you the following result:
        # calculator program
        # first number: 3
        # second number: 4
        # 34

    # You probably meant for this program to answer you with 7 instead of 34. 
    # So what went wrong?

# %%
    # The explanation is that first_number and second_number are strings. 
    # For the calculation to work correctly, you need to change those strings to numbers by using the int() function. 
    # By modifying the last line of the program to use int(), you can resolve the problem:  

print(int(first_number) + int(second_number))

    # calculator program
    # first number: 3
    # second number: 4
    # 7
