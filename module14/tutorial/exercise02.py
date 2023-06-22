# Use slices to retrieve portions of a list
    # You might need to work different sections of a list. In this notebook, you will create a project to display planets closer to and farther away from the sun than a planet that the user enters.

    # This exercise is broken into a series of steps. For each step you will be presented with the goal for the step, followed by an empty cell. Enter your Python into the cell and run it. The solution for each step will follow each cell.

#%%
## Create the list of planets
    # First, create a variable named planets. Add the eight planets (without Pluto) to the list. The planets are:
    # Mercury
    # Venus
    # Earth
    # Mars
    # Jupiter
    # Saturn
    # Uranus
    # Neptune

# Enter your code below


#%%
## Prompt the user for the reference planet
    # Next you will add the code to prompt the user for the name of a planet. You will do this by using input. Because strings are case sensitive in Python, ask the user to use a capital letter to start the name of the planet.

# Enter your code below


#%%
## Find the location of the selected planet
    # Now it's time to determine which planets are closer than the one that the user entered. To do this, you need to find where he planet is in the list. You can use the index method to perform this operation. Add the code to find the index of the planet, and store it in a variable named planet_index.

# Enter your code below


#%%
## Display planets closer to the sun
    # With the index determined, you can now add the code to display planets closer to the sun than the one selected. Use the slicing abilities of a list to display all planets up to the one selected.

# Enter your code below


#%%
## Display planets further
    # You can use the same index to display planets farther from the sun. However, remember that the starting index is included when you're using a slice. As a result, you'll have to add 1 to the value. Add the code to display the planets farther from the sun.

# Enter your code below

