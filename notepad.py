import tkinter as tk
from tkinter import filedialog, messagebox

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Notepad")
        self.root.geometry("700x500")

        self.file_path = None

        # Text Area
        self.text_area = tk.Text(root, undo=True, font=("Arial", 12))
        self.text_area.pack(fill=tk.BOTH, expand=1)

        # Menu Bar
        menubar = tk.Menu(root)
        root.config(menu=menubar)

        # File Menu
        file_menu = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="File", menu=file_menu)
        
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)

        # Edit Menu
        edit_menu = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Edit", menu=edit_menu)

        edit_menu.add_command(label="Cut", command=lambda: root.focus_get().event_generate("<<Cut>>"))
        edit_menu.add_command(label="Copy", command=lambda: root.focus_get().event_generate("<<Copy>>"))
        edit_menu.add_command(label="Paste", command=lambda: root.focus_get().event_generate("<<Paste>>"))

        # Keyboard Shortcuts
        root.bind("<Control-s>", lambda e: self.save_file())
        root.bind("<Control-o>", lambda e: self.open_file())
        root.bind("<Control-n>", lambda e: self.new_file())

    def new_file(self):
        self.file_path = None
        self.text_area.delete(1.0, tk.END)
        self.root.title("New File - Python Notepad")

    def open_file(self):
        path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if path:
            self.file_path = path
            self.text_area.delete(1.0, tk.END)
            with open(path, "r", encoding="utf-8") as file:
                self.text_area.insert(tk.END, file.read())
            self.root.title(f"{path} - Python Notepad")

    def save_file(self):
        if self.file_path:
            with open(self.file_path, "w", encoding="utf-8") as file:
                file.write(self.text_area.get(1.0, tk.END))
            messagebox.showinfo("Saved", "File saved successfully!")
        else:
            self.save_as()

    def save_as(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if path:
            self.file_path = path
            with open(path, "w", encoding="utf-8") as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.root.title(f"{path} - Python Notepad")
            messagebox.showinfo("Saved", "File saved successfully!")

# Run App
if __name__ == "__main__":
    root = tk.Tk()
    Notepad(root)
    root.mainloop()
