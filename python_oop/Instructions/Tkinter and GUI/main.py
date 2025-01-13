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

# .pack function is a geometry management system. Identifies the location of items and where should be placed on the screen
label.pack(side="right", expand=False)

# Keeps window open
window.mainloop()
