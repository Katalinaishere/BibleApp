import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Pioneer")

import tkinter as tk
from expense_tracker import ExpenseTracker
from todo_list import ToDoList
from notes import Notes

# Create the main application window
root = tk.Tk()
root.title("Pioneer")

# Create frames for different sections (Expense Tracker, To-Do List, Notes)
expense_frame = ExpenseTracker(root)
expense_frame.pack(side="left", padx=10, pady=10)

todo_frame = ToDoList(root)
todo_frame.pack(side="left", padx=10, pady=10)

notes_frame = Notes(root)
notes_frame.pack(side="left", padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
