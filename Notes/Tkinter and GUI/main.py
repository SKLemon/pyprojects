#
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
###########################################

# * Creating Windows and Labels with Tkinter
import tkinter

# Create the window from the class Tk()
window = tkinter.Tk()

# Rename the window, similiar to Turtle, use title() method
window.title("Hello World!")

# Adjust and set minimum size of window. Along with various other methods.
window.minsize(width=500, height=300)

# Labelling. This sets the font, text etc, and stamps a label on the window with the arguments.
label = tkinter.Label(text="Label Test", font=("Arial", 24, "bold"))

# * .pack()
"""
- .pack function is a geometry/window management system. Identifies the location of items and where they should be placed on the screen.
- Allows automatic window sizing based on the items (labels, functions, programs etc) inside it.
- Has additional default values, similiar to keyword arguments, which can be changed when calling the .pack() function.
- Should ideally be used when a new item is being added to the screen (new label, new button, new icon etc, or when a change is needed)
"""

label.grid(column=0, row=0)

######################################
# * To create default values in a function:
# TODO: Should put the below into a new file "instructional" or something to avoid confusion
"""
Example:
def my_function(a=1, b=2, c=3) # Note the "=" sets the variable equal to the value
    Do something with a,
    Then something with b,
    then something with c

1) Possible to place a different value in each variable outside of their default values (my_function(a=4, b=65, c=4))
2) or use their defaults by calling the function as is (my_function)
3) or selecting which values get changed (my_function(23,43) - Will place values 23 and 43 into a and b)

Also possible to have unlimited arguments inside a function.
"""

# * Unlimited Positional Arguments

"""
For example, take the function below:
def add (n1, n2):
    return n1 + n2

* Problem: We need to allow any number of inputs to be added in.

* Solution: A "for loop" inside the function
    def add(*args) --> This function can take any number of inputs
        for n in args: --> This runs through each of those inputs
            print(n) --> This will do something with each of those inputs.
* This will be tested out in test.py in the same folder
"""

# * Unlimited Keyword Argument (Many Keyword Arguments) (AKA **kwargs)

"""
* Problem: A) What if we need to refer to arguments by their keyword instead of their positions? and B) Do something with them?

* Solution: A) See Syntax of kwargs below. B) A standard dictionary loop function to do something with the key,value pairs inside the args.

def calculate (**kwargs): # Note the double asterisks
    for key, value in kwargs.items(): --> dictionary loop with key,value and .items() method
        print(key) --> Does something with the key
        value += 1 --> Does something with the value

Example function:
calculate(add = 3, multiply = 5) --> add is now a key, and 3 is its value, same with multiply and 5 respectively.
This will print the key, and add +1 to the values based on the defined function above.

Explanation:
- **kwargs can be looped through using the standard dictionary loop (key,value in kwarg.items()) as shown above.
- The double asterisks tells python to allow taking in multiple arbitrary arguments with their own assigned values and to return a dictionary with those values.
- Functions like label.pack() and Label() can accept any number of keyword arguments which can be passed to the function.
- Classes can be created with this information as well.
! The rest of this is tested out in test.py
"""

# The below is to set up the challenges below
label["text"] = "New Text"


# Creating the button with text and command (like an event listener)
# Event listener must be a function. Example below.
def button_clicked():
    print("Click!")
    # label["text"] = "Button Clicked" --> This is for the first challenge. No need to uncomment
    label["text"] = input.get()
    # label.config(text=input.get()) This comment can also be used in place of the bracket method


# This will create the button(tkinter.Button()), set the buttons title(text arg), and wait for an event to occur(command arg).
# button_clicked() in this scenario is the callback function
button = tkinter.Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

"""
* Challenge 1:
Create the label and have it say "button clicked" instead of "new text"
"""
# * Allowing for input in TKinter

# Entry Component in Tkinter
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)

"""
# * Challenge 2:
# When the button gets clicked, update the label with whatever was input into the field
# button_clicked() function is updated
"""

# * .get() Method
"""
To get a hold of the values inside a dictionary, we can also use get(), which will return None if there is no default argument.
"""
input.get()  # This returns the input from the Entry class as a string, however there is no string stored inside the input = Entry()

# * More widgets
"""
Labels - Text on the screen
Buttons - Can be clicked and do some sort of action
Entry - Allows for input in the form of a text box
Text Entry Box - Large area to allow multiple line texts
Spinbox - Allows clicking up or down to set a value. Gets value which is being changed. Function created to get value.
Scale - Move a slider up or down. Getting hold of value which the user lands on. Function created to get value
Checkbox - Clickable on or off. Can print 1 or 0 by tying the checkbox to a variable. Defined by IntVar() (class).
RadioButtons - Allows selecting one out of the other options. Gets the selected option.
ListBox - List of options created from a python list. bind() function is used to get a hold of whichever item is selected from list

For more info and examples, check "Other_Tkinter_Widgets.py" in this same folder. Written by Dr.Angela
"""

# * Layout Managers
"""
* pack()
    - Packs each of the widgets next to each other. Always starts from top and packs every other widget just below the previous.
    - Changeable with parameters like (side,expand etc)
    - The problem is that it's not exact and is very complicated to get precise locations

* place()
    - Similiar to pack() but allows exact x and y value coordinates to place widgets
    - Downside of place() is that it is so specific. Will have to manually place each and every widget.
* grid()
    - Best of both worlds. Seperates the screen into a grid with user customizable rows and columns.
    - It is used to place widgets relative to other widgets. Flexible and easy to imagine and understand
    - Can't use both grid() and pack() in the same program. Can only choose one or the other
"""

# * Challenge 3
"""
- Change the already written code and add a new button
- Match layout of 4 columns, 3 rows. Label in C1, R1. Button in C2, R2. New Button in C3, R1. Entry in C4, R3.
"""
new_button = tkinter.Button(text="New_Button")
new_button.grid(column=2, row=0)


# * Padding
"""
Easiest way to add padding is to directly modify the widgets using padx and pady
window.config(padx=20, pady=20) will change padding for the whole window for example
input.config(padx=20, pady=20) will change padding only for that specific Entry widget
"""
# Keeps window open
window.mainloop()
