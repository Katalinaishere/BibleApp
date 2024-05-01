import tkinter as tk

class ToDoList(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=300, height=200, relief="raised", bd=2)
        self.parent = parent
        self.create_widgets()
    
    def create_widgets(self):
        # To-Do List Title
        self.label = tk.Label(self, text="To-Do List", font=("Helvetica", 16, "bold"))
        self.label.pack(pady=10)
        
        # Entry Form for New Task
        self.task_entry = tk.Entry(self, width=30)
        self.task_entry.pack(pady=5)
        
        # Add Task Button
        self.add_button = tk.Button(self, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)
        
        # To-Do List
        self.todo_listbox = tk.Listbox(self, width=40, height=10)
        self.todo_listbox.pack(pady=10)

    def add_task(self):
        # Get the task from the entry and add it to the listbox
        task = self.task_entry.get()
        # Add functionality to add task
        print("Task added:", task)
        self.todo_listbox.insert(tk.END, task)

