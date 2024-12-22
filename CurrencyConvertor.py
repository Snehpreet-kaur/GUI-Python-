from tkinter import *

def convert_currency():
    try:
        source_amount = float(source_entry.get())
        target_amount = source_amount / conversion_rate
        target_label.config(text=f"{target_amount:.2f}")
    except ValueError:
        target_label.config(text="Invalid input")

conversion_rate = 71.42

# Create the main window
root = Tk()
root.title("Currency Converter")

# Configure grid layout
root.config(background="teal")

# Title label
title_label = Label(root, text="₹ -> $ Converter", font=("Arial", 14))
title_label.grid(row=0, column=0, columnspan=3, pady=10)

# Source currency amount label and entry
source_label = Label(root, text="Source Currency amount (₹.):")
source_label.grid(row=1, column=0, sticky="e", padx=10, pady=5)

source_entry = Entry(root)
source_entry.grid(row=1, column=1, padx=10, pady=5)

# Convert button
convert_button = Button(root, text="Convert", command=convert_currency)
convert_button.grid(row=2, column=1, pady=10)

# Target currency amount label and display
target_label_desc = Label(root, text="Target Currency amount ($):")
target_label_desc.grid(row=2, column=0, sticky="e", padx=10)

target_label = Label(root, text="0.00", font=("Arial", 12))
target_label.grid(row=2, column=2, padx=10)

# Run the application
root.mainloop()
