# Exercise: Transform strings
    # There are several operations you can perform on strings when you manipulate them. In this exercise, you'll use string methods to modify text with facts about the Moon and then extract information to create a short summary.

    # This exercise is broken into a series of steps. For each step you will be presented with the goal for the step, followed by an empty cell. Enter your Python into the cell and run it. The solution for each step will follow each cell.

#%%
## Parsing interesting facts about the moon
    # Start by storing the following paragraph in a variable named text:

    # Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
    # On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C.

# Enter code below
text = ""

#%%
## Separate the paragraph into sentences
    # In English each sentence ends with a period. You will use this to break the paragraph into difference sentences. Using the split method to split the text into sentences by looking for the string .  (a period followed by a space). Store the result in a variable named sentences. Print the result.

# Enter code below


# Desired output
# Console
# ['Interesting facts about the Moon', "The Moon is Earth's only satellite", 'There are several interesting facts about the Moon and how it affects life here on Earth', '\nOn average, the Moon moves 4cm away from the Earth every year', 'This yearly drift is not significant enough to cause immediate effects on Earth', 'The highest daylight temperature of the Moon is 127 C.']

#%%
## Find keywords
    # You will finish your program by adding the code to find any sentences which mention temperature. Add code to loop through the sentences variable. For each sentence, search for the word temperature. If the word is found, print the sentence.

# Enter code below


# Desired output
# Console
# The highest daylight temperature of the Moon is 127 C.