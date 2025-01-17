#
# ! Created for BAIL repository. Created 01/16
import tkinter as tk

"""
# TODO: Text Entry for Miles to KM
    - Create window using grid() [✔]
    - Create labels [✔]
    - Create button [✔]
    - Adjusted appropriate sizing and grid positioning [✔]
# TODO: Calculate button that will calculate the number in the miles box and output result in km box
    - Create function that calculates miles to km [✔]
"""


# Function to calculate
def miles_to_km():
    miles_value = entry.get()
    km_value = round(float(miles_value) * 1.609344, 2)
    km_answer.config(text=km_value)


# Default padding
PADDING_X = 5
PADDING_Y = 5

# Created the window
window = tk.Tk()
window.title("Miles to KM Converter")

# Created the labels
miles_label = tk.Label(text="Miles")
km_label = tk.Label(text="Km")
km_answer = tk.Label()
equal_to = tk.Label(text="is equal to")

# Created the buttons
calculate_button = tk.Button(text="Calculate", command=miles_to_km)

# Created the entry window
entry = tk.Entry(width=10)

# grid positioning
widgets = [
    (miles_label, 3, 1),
    (km_label, 3, 2),
    (km_answer, 2, 2),
    (equal_to, 1, 2),
    (calculate_button, 2, 3),
    (entry, 2, 1),
]

for widget, col, row in widgets:
    widget.grid(column=col, row=row, padx=PADDING_X, pady=PADDING_Y)

window.mainloop()
