import tkinter as tk
from tkinter import messagebox

# Functions
def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def clear_all_tasks():
    tasks_listbox.delete(0, tk.END)

def exit_app():
    root.destroy()

# GUI Setup
root = tk.Tk()
root.title("To-Do List")

# Input Frame
input_frame = tk.Frame(root, padx=10, pady=10)
input_frame.pack()

# Task Entry
task_label = tk.Label(input_frame, text="Task:")
task_label.grid(row=0, column=0, padx=5, pady=5)
task_entry = tk.Entry(input_frame, width=40)
task_entry.grid(row=0, column=1, padx=5, pady=5)

# Buttons
add_button = tk.Button(input_frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=2, padx=5, pady=5)

# Listbox Frame
listbox_frame = tk.Frame(root, padx=10, pady=10)
listbox_frame.pack()

# Listbox
tasks_listbox = tk.Listbox(listbox_frame, width=50, height=15)
tasks_listbox.pack(side=tk.LEFT, padx=5, pady=5)

# Scrollbar
scrollbar = tk.Scrollbar(listbox_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tasks_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=tasks_listbox.yview)

# Action Buttons
action_frame = tk.Frame(root, padx=10, pady=10)
action_frame.pack()

remove_button = tk.Button(action_frame, text="Remove Task", command=remove_task)
remove_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(action_frame, text="Clear All Tasks", command=clear_all_tasks)
clear_button.pack(side=tk.LEFT, padx=10)

exit_button = tk.Button(action_frame, text="Exit", command=exit_app)
exit_button.pack(side=tk.LEFT, padx=10)

# Run the App
root.mainloop()
