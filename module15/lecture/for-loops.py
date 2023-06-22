#%%
# Use 'for' loops with lists
    # In Python, lists can store any type of value, such as strings or numbers:

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

#%%
    # You can access any item in a list by enclosing the index in brackets ([]) after the variable name. Indexes start from 0:

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

print("The first planet is ", planets[0])
print("The second planet is ", planets[1])
print("The third planet is ", planets[2])

    # You can also determine the number of items in a list by using len. So you could use a while loop and a counter to loop or iterate over each item in the list. Because this operation is so common, Python provides for loops, which you can use to iterate over lists.

#%%
## About for loops
    # Here's an example for loop that counts down from 4 to 0:

countdown = [4, 3, 2, 1, 0]
for number in countdown:
    print(number)
print("Blast off!! 🚀")

    # The for loop is a statement with five important parts:
        # The word for, followed by a space.
        # The variable name you want to create for each value in the sequence (number).
        # The word in, surrounded by spaces.
        # The name of the list (countdown, in the preceding example), or iterable that you want to loop over, followed by a colon (:).
        # The code you want to run for each item in the iterable, separated by nested whitespace.

#%%
    # Let's change that code to wait for one second between each number by using the sleep() function:

from time import sleep

countdown = [4, 3, 2, 1, 0]

for number in countdown:
    print(number)
    sleep(1)  # Wait 1 second
print("Blast off!! 🚀")
