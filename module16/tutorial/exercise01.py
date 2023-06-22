# Exercise: Create and modify a Python dictionary
    # Python dictionaries allow you to model more complex data. Dictionaries are a collection of key/value pairs, and are very common in Python programs. Their flexibility allows you to dynamically work with related values without having to create classes or objects.

    # This exercise is broken into a series of steps. For each step you will be presented with the goal for the step, followed by an empty cell. Enter your Python into the cell and run it. The solution for each step will follow each cell.

#%%
## Managing planet data
    # You want to create a program which will store and display information about planets. To start you will use one planet. Create a variable named planet. Store the following values as a dictionary:
        # name: Mars
        # moons: 2

# Enter code below


#%%
## Display planet data
    # With the variable created, you will now display information. You can retrieve information by either using get or square brackets ([ ]) and the key name. Add the code to display the planet information in the following format:

    # __ has __ moon(s)

    # If you were working with Earth, the output would be Earth has 1 moon(s)

# Enter code below


# Desired output
# When you run the cell you should see the following result:
# Console
# Mars has 2 moon(s)

#%%
## Add circumference information
    # You can update existing keys or create new ones by either using the update method or using square brackets ([ ]). When you're using update, you pass in a new dictionary object with the updated or new values. When using square brackets, you specify the key name and assign a new value.

    # Add a new value to planet with a key of 'circumference (km)'. This new value should store a dictionary with the planet's two circumferences:
    # polar: 6752
    # equatorial: 6792

    # Finally, add the code to print the polar circumference of the planet. You can use whatever sentence formatting you wish.

# Enter code below


# Desired output
# When you run the cell you should see the following result:
# Console
# Mars has a polar circumference of 6752
