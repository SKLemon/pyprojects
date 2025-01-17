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

# grid postioning
miles_label.grid(column=3, row=1, padx=PADDING_X, pady=PADDING_Y)
km_label.grid(column=3, row=2, padx=PADDING_X, pady=PADDING_Y)
km_answer.grid(column=2, row=2, padx=PADDING_X, pady=PADDING_Y)
equal_to.grid(column=1, row=2, padx=PADDING_X, pady=PADDING_Y)
calculate_button.grid(column=2, row=3, padx=PADDING_X, pady=PADDING_Y)
entry.grid(column=2, row=1, padx=PADDING_X, pady=PADDING_Y)

window.mainloop()
