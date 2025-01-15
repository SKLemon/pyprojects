# ! For BAIL Repository. Created 01/12
"""
* Early GUI Origins

Emerged in the 1970s with research projects like the Xerox Alto
Popularized in the 1980s by Apple Macintosh and Microsoft Windows
Shifted computing from text-based interfaces to visual elements (buttons, icons, windows)

* Tkinter Basics

Python's standard GUI toolkit
A thin wrapper around the Tcl/Tk graphical framework
Created by John Ousterhout in the late 1980s
Adopted by Python for simplicity and cross-platform compatibility
Allows quick and easy GUI development without additional dependencies
"""

# * Creating Windows and Labels with Tkinter
import tkinter

# Create from class Tk()
window = tkinter.Tk()

# Rename the window
window.title("Hello World!")

# Adjust and set minimum size of window
window.minsize(width=500, height=300)

# Labelling. This sets the font, text etc.
label = tkinter.Label(text="Label Test", font=("Arial", 24, "bold"))

"""
# .pack function is a geometry/window management system. Identifies the location of items and where they should be placed on the screen.
# Allows automatic window sizing based on the items (labels, functions, programs etc) inside it.
# Has additional default values, similiar to keyword arguments, which can be changed when calling the .pack() function.
"""
label.pack(side="right", expand=False)
"""
* To create default values in a function:
Example:
def my_function(a=1, b=2, c=3)
    Do something with a,
    Then something with b,
    then something with c

1) Possible to place a different value in each variable outside of their default values (my_function(a=4, b=65, c=4))
2) or use their defaults by calling the function as is (my_function)
3) or selecting which values get changed (my_function(23,43) - Will place values 23 and 43 into a and b)

* ### Unlimited Positional Arguments
Also possible to have unlimited arguments inside a function.
For example, take the function below:
def add (n1, n2):
    return n1 + n2

? Problem: We need to allow any number of inputs to be added in.

? Solution: A for loop inside the function
    def add(*args) --> This function can take any number of inputs
        for n in args: --> This runs through each of those inputs
            print(n) --> This will do something with each of those inputs.
! This will be tested out in test.py in the same folder

* Unlimited Keyword Argument (Many Keyword Arguments) (AKA **kwargs)
? Problem: A) What if we need to refer to arguments by their keyword? B) Do something with them?
? Solution: A) See Syntax below. B) A standard dictionary loop function to do something with the key,value pairs inside the args.
def calculate (**kwargs): --> A function that takes in many arbitrary keywords with their own assigned values and returns a dictionary with those values
    pass

calculate(add = 3, multiply = 5) --> add is now a key, and 3 is its value.
- **kwargs can be looped through the standard dictionary loop (key,value in kwarg.items())
! The rest of this is tested out in the test.py

"""


# Keeps window open
window.mainloop()
