import tkinter as tk

class ExpenseTracker(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=300, height=200, relief="raised", bd=2)
        self.parent = parent
        self.create_widgets()
    
    def create_widgets(self):
        # Expense Tracker Title
        self.label = tk.Label(self, text="Expense Tracker", font=("Helvetica", 16, "bold"))
        self.label.pack(pady=10)
        
        # Expense Entry Form
        self.entry_frame = tk.Frame(self)
        self.entry_frame.pack(pady=10)
        
        tk.Label(self.entry_frame, text="Date:").grid(row=0, column=0, sticky="w")
        self.date_entry = tk.Entry(self.entry_frame)
        self.date_entry.grid(row=0, column=1)
        
        tk.Label(self.entry_frame, text="Amount ($):").grid(row=1, column=0, sticky="w")
        self.amount_entry = tk.Entry(self.entry_frame)
        self.amount_entry.grid(row=1, column=1)
        
        tk.Label(self.entry_frame, text="Category:").grid(row=2, column=0, sticky="w")
        self.category_entry = tk.Entry(self.entry_frame)
        self.category_entry.grid(row=2, column=1)
        
        tk.Label(self.entry_frame, text="Description:").grid(row=3, column=0, sticky="w")
        self.description_entry = tk.Entry(self.entry_frame)
        self.description_entry.grid(row=3, column=1)
        
        self.add_button = tk.Button(self.entry_frame, text="Add Expense", command=self.add_expense)
        self.add_button.grid(row=4, columnspan=2, pady=10)

    def add_expense(self):
        # Add functionality to add an expense
        date = self.date_entry.get()
        amount = self.amount_entry.get()
        category = self.category_entry.get()
        description = self.description_entry.get()
        
        # Validate input and add to listbox
        print("Date:", date)
        print("Amount:", amount)
        print("Category:", category)
        print("Description:", description)






