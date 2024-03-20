import tkinter as tk
from tkinter import ttk, messagebox
import os

def schedule_shutdown(hours, minutes):
    # Assemble the shutdown command
    shutdown_time = f"{hours}:{minutes}"
    command = f"schtasks /create /tn ShutdownTask /tr \"shutdown /s /f\" /sc once /st {shutdown_time} /ru SYSTEM"

    # Execute the command
    os.system(command)
    messagebox.showinfo("Scheduled", f"Shutdown task has been scheduled at {shutdown_time}.")

def cancel_shutdown(root):
    root.destroy()  # Close the tkinter window
    messagebox.showinfo("Cancelled", "Shutdown Cancelled")

# Function to handle button click and schedule shutdown
def on_schedule():
    hours = hours_combobox.get()
    minutes = minutes_combobox.get()

    if hours and minutes:
        schedule_shutdown(hours, minutes)
    else:
        messagebox.showerror("Error", "Please select hours and minutes.")

# Create the main tkinter window
root = tk.Tk()
root.title("Shutdown Scheduler")
root.geometry("400x200")  # Set the size of the window

# Create a frame for better organization
frame = tk.Frame(root)
frame.pack(expand=True, fill=tk.BOTH)

# Create the hour combobox
hours_combobox = ttk.Combobox(frame, values=[str(i).zfill(2) for i in range(24)])
hours_combobox.pack(pady=10)
hours_combobox.set("00")

# Create the minute combobox
minutes_combobox = ttk.Combobox(frame, values=[str(i).zfill(2) for i in range(60)])
minutes_combobox.pack(pady=10)
minutes_combobox.set("00")

# Create the "Schedule" button
schedule_button = tk.Button(frame, text="Schedule Shutdown", command=on_schedule)
schedule_button.pack(pady=10)

# Create the "Cancel" button
cancel_button = tk.Button(frame, text="Cancel", command=lambda: cancel_shutdown(root))
cancel_button.pack(pady=10)

# Run the tkinter event loop
root.mainloop()
