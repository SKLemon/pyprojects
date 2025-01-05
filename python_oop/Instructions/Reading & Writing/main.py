# Created as a part of the BAIL Repository for instructional and reference purposes... Unsure when it was originally created, but final edits completed 01/04

"""

Using the standard file system in Python to read from and write to a file.

This script demonstrates how to open a file,
read its contents, print the contents to the console,
write new content to the file, and then close the file.

"""

try:
    # Open the file in read mode.
    # Opening a file is necessary to establish a connection between the file and the program.
    # This allows the program to read from or write to the file.
    file = open("my_text.txt", "r")

    # Read the contents of the file
    contents = file.read()

    # Print the contents to the console
    print(contents)

    # Close the file to free up system resources.
    # Closing the file is important because it ensures that all resources used by the file are released.
    # It also ensures that any changes made to the file are properly saved.
    file.close()

except FileNotFoundError:
    print("File not found. Creating a new file.")
    # Open the file in write mode to create it
    file = open("my_text.txt", "w")
    file.write("This is a newly created file.")
    file.close()

# Open the file in write mode.
# This will allow us to make changes to the file.
file = open("my_text.txt", "w")

# Write new content to the file
file.write("This is new content added to the file.")

# Close the file to save the changes and free up system resources.
file.close()
