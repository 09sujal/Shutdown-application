import tkinter as tk
from tkinter import ttk
from tkinter import messagebox  # Import messagebox submodule
from datetime import datetime
import win32com.client
import sys

# Get current time
now = datetime.now()
current_hour = str(now.hour)
current_minute = str(now.minute).zfill(2)
current_second = str(now.second).zfill(2)

def create_task():
    frequency = combobox_frequency.get()
    hour = combobox_hour.get()
    minute = combobox_minute.get()
    second = combobox_second.get()
    try:
        # Logic to create task in Task Scheduler using pywin32
        scheduler = win32com.client.Dispatch('Schedule.Service')
        scheduler.Connect()
        root_folder = scheduler.GetFolder('\\')
        task_def = scheduler.NewTask(0)
        task_def.RegistrationInfo.Description = 'Shutdown Task'
        task_def.Settings.Enabled = True
        triggers = task_def.Triggers
        trigger = triggers.Create(1)  # 1 means "ONCE"
        trigger.StartBoundary = f'{now.year}-{now.month}-{now.day}T{hour}:{minute}:{second}'
        root_folder.RegisterTaskDefinition(
            'Shutdown Task',  # Task name
            task_def,
            6,  # Update existing task if it exists
            '', '',  # User and password
            1,  # Logon type: interactive
        )
        print("Task created successfully.")
    except Exception as e:
        print(f"Error creating task: {e}")
        # Display a message to the user using messagebox
        messagebox.showerror("Error", f"Error creating task: {e}")

root = tk.Tk()
root.title("Shutdown Timer")

# Frame for time selection
time_frame = ttk.Frame(root)
time_frame.grid(row=0, column=0, padx=10, pady=10)

# Combobox for frequency
frequency_label = tk.Label(time_frame, text="Frequency:")
frequency_label.grid(row=0, column=0, padx=(0, 5), pady=5)
frequencies = ["Today", "Daily", "Weekly", "Monthly"]
combobox_frequency = ttk.Combobox(time_frame, values=frequencies, width=10)
combobox_frequency.grid(row=0, column=1, padx=5, pady=5)
combobox_frequency.set("Today")

# Combobox for hours
hours_label = tk.Label(time_frame, text="Hours:")
hours_label.grid(row=1, column=0, padx=(0, 5), pady=5)
hours = [str(i) for i in range(24)]
combobox_hour = ttk.Combobox(time_frame, values=hours, width=5)
combobox_hour.grid(row=1, column=1, padx=5, pady=5)
combobox_hour.set(current_hour)

# Combobox for minutes
minutes_label = tk.Label(time_frame, text="Minutes:")
minutes_label.grid(row=1, column=2, padx=(10, 5), pady=5)
minutes = [str(i).zfill(2) for i in range(60)]
combobox_minute = ttk.Combobox(time_frame, values=minutes, width=5)
combobox_minute.grid(row=1, column=3, padx=5, pady=5)
combobox_minute.set(current_minute)

# Combobox for seconds
seconds_label = tk.Label(time_frame, text="Seconds:")
seconds_label.grid(row=1, column=4, padx=(10, 0), pady=5)
seconds = [str(i).zfill(2) for i in range(60)]
combobox_second = ttk.Combobox(time_frame, values=seconds, width=5)
combobox_second.grid(row=1, column=5, padx=(5, 0), pady=5)
combobox_second.set(current_second)

# Button to create task
create_button = ttk.Button(root, text="Shutdown", command=create_task)
create_button.grid(row=1, column=0, pady=(0, 10))

root.mainloop()
