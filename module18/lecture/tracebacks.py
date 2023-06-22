# Use tracebacks to find errors
    # Exceptions in Python are a core feature of the language. You might be surprised to read that something that produces errors is highlighted as a feature. This surprise can be because robust software tools don't seem to crash with a traceback (several lines of text that indicate how the error started and ended).

    # But exceptions are useful because they help in decision-making by producing descriptive error messages. They can help you handle both expected and unexpected problems.

#%%
## Tracebacks
    # A traceback is the body of text that can point to the origin (and ending) of an unhandled error. Understanding the components of a traceback will make you more effective when you're fixing errors or debugging a program that's not working well.

    # The first time you encounter exceptions in Python, you might be tempted to avoid the error by suppressing it. When a program suffers an unhandled error, a traceback appears as the output. As you'll see in this module, tracebacks are useful. There are ways to properly handle the errors so that they don't appear or they only show helpful information.

    # Open a Python interactive session and try opening a nonexistent file:

open("/path/to/mars.jpg")

    # Output
    # Traceback (most recent call last):
    # File "<stdin>", line 1, in <module>
    # FileNotFoundError: [Errno 2] No such file or directory: '/path/to/mars.jpg'

    # That output has several key parts. First, the traceback mentions the order of the output. Then it informs you that the file is stdin (input in the interactive terminal) on the first line of the input. The error is FileNotFoundError (the exception name), which means that the file doesn't exist or perhaps the directory to it doesn't exist.

    # That's a lot of information. It can be hard to understand why line 1 is meaningful or what Errno 2 means.

    # Tracebacks almost always include the following information:
        # All file paths involved, for every call to every function.
        # Line numbers associated with every file path.
        # The names of functions, methods, or classes involved in producing an exception.
        # The name of the exception that was raised.
        