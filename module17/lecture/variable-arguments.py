# Use variable arguments in Python
    # In Python, you can use any number of arguments and keyword arguments without declaring each one of them. This ability is useful when a function might get an unknown number of inputs.

#%%
## Variable arguments
    # Arguments in functions are required. But when you're using variable arguments, the function allows any number of arguments (including 0) to be passed in. The syntax for using variable arguments is prefixing a single asterisk (*) before the argument's name.

    # The following function prints the received arguments:

def variable_length(*args):
    print(args)

    # In this case, *args is instructing the function to accept any number of arguments (including 0). Within the function, args is now available as the variable that holds all arguments as a tuple. Try out the function by passing any number or type of arguments:

variable_length()
()
variable_length("one", "two")
('one', 'two')
variable_length(None)
(None,)

    # As you can see, there's no restriction on the number or type of arguments passed in.

#%%
    # A rocket ship goes through several steps before a launch. Depending on tasks or delays, these steps might take longer than planned. Let's create a variable-length function that can calculate how many minutes until launch, given how much time each step is going to take:

def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"

    # Try out the function by passing any number of minutes:

sequence_time(4, 14, 18)

    # Output
    # Total time to launch is 36 minutes.

#%%
sequence_time(4, 14, 48)

    # Output
    # Total time to launch is 1.1 hours.

#%%
## Variable keyword arguments
    # For a function to accept any number of keyword arguments, you use a similar syntax. In this case, a double asterisk is required:

def variable_length(**kwargs):
    print(kwargs)

    # Try the example function, which prints the names and values passed in as kwargs:

variable_length(tanks=1, day="Wednesday", pilots=3)
{'tanks': 1, 'day': 'Wednesday', 'pilots': 3}

    # If you're already familiar with Python dictionaries, you'll notice that variable-length keyword arguments are assigned as a dictionary. To interact with the variables and values, use the same operations as a dictionary.

#%%
    # In this function, let's use variable keyword arguments to report the astronauts assigned to the mission. Because this function allows any number of keyword arguments, it can be reused regardless of the number of astronauts assigned:

def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")

    # Try it out with the crew of the Apollo 11:

crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins")

    # Output
    # 3 astronauts assigned for this mission:
    # captain: Neil Armstrong
    # pilot: Buzz Aldrin
    # command_pilot: Michael Collins

#%%
    # Because you can pass any combination of keyword arguments, make sure to avoid repeated keywords. Repeated keywords result in an error:

crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", pilot="Michael Collins")

    # OutPut
    #   File "<stdin>", line 1
    # SyntaxError: keyword argument repeated: pilot
    