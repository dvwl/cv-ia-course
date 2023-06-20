# %%
## A Python program
    # To create a program in Python, you need to store it in a file.
    # The file extension .py
    # A program does something or carry out a task.
    # You'll need to add statements or instructions for a program to perform the task.

# working-with-output.py 
sum = 1 + 2 
print(sum)

## Run a program
    # You can run a program in a console.
    # A console is a command-line application that lets you interact with the operating system.
    # To run a program, the name of the Python executable program, followed by the name of your program.
    # Example, 
    # python working-with-output.py

# %%
## The print() function
    # One of the first things is print to a console.
    # To write information to the console, you can use the print() function.

print("show this in the console")
    # Note how the command calls print() by using parentheses

# %%
    # If you used square brackets [] instead of parentheses

print["show this in the console"] # will generate a compile time error

# %%
## Variables
    # To get anywhere with coding, you need to understand that you're operating on data. 
    # As your program is working on data, you might need to remember a certain value throughout the program's execution. 
    # For that, you use variables.

sum = 1 + 2 # 3 
product = sum * 2 
print(product)

# %%
## Data types
    # A variable assumes a data type. In the preceding program, sum gets the type int. 
    # However, there are many more data types. 
    # Here are a few that you're likely to encounter:
        # Numeric type, with or without decimals (int, float, complex), 
        # text type (str = “a string”), 
        # Boolean type (continue = True)

planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small 
distance_to_alpha_centauri = 4.367 # float, lightyears 
can_liftoff = True 
shuttle_landed_on_the_moon = "Apollo 11" #string 

# %%
    # How do you know what type something has? If you see the data being assigned to the variable as shown in the following code, you can spot it:

distance_to_alpha_centauri = 4.367 # looks like a float
type(distance_to_alpha_centauri) ## <class 'float’>

# %%
## Operators
    # Operators let you perform various operations on variables and their values. 
    # The general idea is that you have a left side and a right side and an operator in the middle:
    # <left side> <operator> <right side>

left_side = 10 
right_side = 5 
left_side / right_side # 2

    # This example uses a slash (/) to divide the left_side value by the right_side value.
    # There are many more operators. This unit describes some important ones you're likely to encounter.
    # Python uses two types of operators: arithmetic and assignment.

# %%
## Arithmetic operators
    # type  description
    # +     addition operator
    # -     subtraction operator
    # /     division operator
    # *     multiplication operator

# %%
## Assignment operators
    # operator  example
    # =         x = 2   # x now contains 2
    # +=        x += 2  # x incremented by 2
    # -=        x -= 2  # x decremented by 2
    # /=        x /= 2  # x divided by 2
    # *=        x *= 2  # x multiplied by 2

# %%
## Dates
    # When you're building programs, you're likely to interact with dates. 
    # A date in a program usually means both the calendar date and the time.
    # You can use a date in various applications, like these examples:
        # Backup file: Using a date as part of a backup file's name is a good way to indicate when a backup was made and when it needs to be made again.
        # Condition: You might want to carry a specific logic when there's a certain date.
        # Metric: Dates are used to check performance on code to (for example) measure the time it takes to execute a function.
    # To work with a date, you need to import the date module.
    
from datetime import date
date.today()
print(date.today())

# %%
## Data type conversion
    # You want to use a date with something, usually a string. 
    # If you, for example, want to show today's date on the console, you might run into a problem:

print("Today's date is: " + date.today()) # will generate a compile time error

# %%
    # You accomplish such a conversion by using the utility function str():

print("Today's date is: " + str(date.today()))
