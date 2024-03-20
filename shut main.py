import tkinter as tk
from tkinter import messagebox
import os

def countdown_timer(label, count, root):
    if count >= 0:
        root.title(f"Shutting down in {count} sec")
        count -= 1
        label.after(1000, countdown_timer, label, count, root)  # Call countdown_timer after 1000ms (1 second)
    else:
        label.config(text="Shutting Down")
        shutdown()

def shutdown():
    os.system("shutdown /s /t 1")

def cancel_shutdown(root):
    root.destroy()  # Close the tkinter window
    messagebox.showinfo("Cancelled", "Shutdown Cancelled")

# Create the main tkinter window
root = tk.Tk()
root.title("Countdown Timer")
root.geometry("400x120")  # Set the size of the window

root.iconbitmap()
label = tk.Label(root, text="", font=("Helvetica", 16))
label.pack(pady=0)

countdown_timer(label, 100, root)  # Change 100 to the desired countdown time

# Create a frame for better organization
frame = tk.Frame(root)
frame.pack(expand=True, fill=tk.BOTH)

# Create a label to display the text
label = tk.Label(frame, text="Do you want to shutdown the computer now?", font=("Arial", 12))
label.pack(pady=10)

# Create a frame for the buttons
button_frame = tk.Frame(frame)
button_frame.pack()

# Create the "Yes" button
yes_button = tk.Button(button_frame, text="Yes", width=10, height=2, command=shutdown)
yes_button.pack(side=tk.LEFT, padx=20)

# Create the "No" button
no_button = tk.Button(button_frame, text="No", width=10, height=2, command=lambda: cancel_shutdown(root))
no_button.pack(side=tk.RIGHT, padx=20)

# Run the tkinter event loop
root.mainloop()