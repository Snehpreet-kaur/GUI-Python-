from tkinter import *

def calculate_distance():
    try:
        # Get user inputs
        time = float(time_entry.get())
        speed = float(speed_entry.get())
        # Calculate distance
        distance = time * speed
        # Display the result
        result_label.config(text=f"Distance Covered: {distance:.2f} km")
    except ValueError:
        result_label.config(text="Invalid input! Please enter numbers.")

# Create the main window
root = Tk()
root.title("Distance Calculator")

# Configure the grid
root.geometry("300x300")

# Time input
time_label = Label(root, text="Time (in hours):")
time_label.grid(row=0, column=0, sticky="e")
time_entry = Entry(root)
time_entry.grid(row=0, column=1)

# Speed input
speed_label = Label(root, text="Speed (in km/hr):")
speed_label.grid(row=1, column=0, sticky="e")
speed_entry = Entry(root)
speed_entry.grid(row=1, column=1)

# Calculate button
calculate_button = Button(root, text="Calculate", command=calculate_distance)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Result label
result_label = Label(root, text="Distance Covered: 0.00 km", font=("Arial", 12))
result_label.grid(row=3, column=0, columnspan=2)

# Run the application
root.mainloop()
