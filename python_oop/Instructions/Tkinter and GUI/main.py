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

# ! Creating Windows and Labels with Tkinter ! #
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

* To create default values in a function:
Example:
def my_function(a=1, b=2, c=3)
    Do something with a,
    Then something with b,
    then something with c

1) Possible to place a different value in each variable outside of their default values (my_function(a=4, b=65, c=4))
2) or use their defaults by calling the function as is (my_function)
3) or selecting which values get changed (my_function(23,43) - Will place values 23 and 43 into a and b)
"""

label.pack(side="right", expand=False)

# Keeps window open
window.mainloop()
