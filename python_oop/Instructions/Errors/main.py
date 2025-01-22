# Created for BAIL repository 01/21
# FileNotFound
# with open("a_file.txt") as file:
# file.read()

# KeyError
# a_dictionary = {"key":"value"}
# value = a_dictionary["non_existent_key"]

# And various other errors
"""
! Try-Catch-Except-Finally Pattern

Following Murphy's Law. Anything that can go wrong will go wrong. The above pattern tries to catch the errors and fail gracefully

Try: Used when trying to execute something that may not always work 10 out of 10 times (Something that might cause an exception)
Except: Used when there is an exception, and the block of code under the Except is what should run in that scenario
Else: Used when there are no exceptions, and all is good without any issues
Finally: Used when something doesn't care about the above, and should run no matter what happens. Useful for tidying up files and cleaning them up

Example below:
"""
try:
    file = open("a_file.txt")  # This will result in a FileNotFound error

# This specifies on what type of error the except block should run. Always good to identiy an error block
except FileNotFoundError:
    print("There was an error")  # This will print instead of the error
    """
    In this block, it's better to ensure some code will run if the try block doesn't run.
    It's not a good place to just rename the error message without invoking a back up of some kind
    """
    file = open("a_file.txt", "w")
    file.write("something")
except KeyError:
    print("That key does not exist")
else:
    content = file.read()
    print(content)
