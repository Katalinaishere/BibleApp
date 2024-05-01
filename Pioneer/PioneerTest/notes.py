import tkinter as tk

class Notes(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=300, height=200, relief="raised", bd=2)
        self.parent = parent
        self.create_widgets()
    
    def create_widgets(self):
        # Notes Title
        self.label = tk.Label(self, text="Notes", font=("Helvetica", 16, "bold"))
        self.label.pack(pady=10)
        
        # Text Entry for Notes
        self.text_entry = tk.Text(self, width=40, height=10)
        self.text_entry.pack(pady=10)
        
        # Save Note Button
        self.save_button = tk.Button(self, text="Save Note", command=self.save_note)
        self.save_button.pack()

    def save_note(self):
        # Get the text from the text entry and save it
        note_content = self.text_entry.get("1.0", tk.END)
        # Add functionality to save note content
        print("Note saved:")
        print(note_content)




