import tkinter as tk
from tkinter import ttk

def update_second_dropdown(*args):
    selected_item = first_dropdown.get()

    # Update options for the second dropdown based on the selected item in the first dropdown
    if selected_item == "Option 1":
        second_dropdown['values'] = ["Option 1 - A", "Option 1 - B", "Option 1 - C"]
    elif selected_item == "Option 2":
        second_dropdown['values'] = ["Option 2 - X", "Option 2 - Y", "Option 2 - Z"]
    else:
        second_dropdown['values'] = []

# Create the main window
root = tk.Tk()
root.title("Dropdown Example")

# Create the first dropdown
first_label = tk.Label(root, text="Select Category:")
first_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
categories = ["Option 1", "Option 2"]
first_dropdown = ttk.Combobox(root, values=categories, state="readonly")
first_dropdown.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
first_dropdown.bind("<<ComboboxSelected>>", update_second_dropdown)

# Create the second dropdown
second_label = tk.Label(root, text="Select Subcategory:")
second_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
second_dropdown = ttk.Combobox(root, values=[], state="readonly")
second_dropdown.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

# Run the Tkinter event loop
root.mainloop()