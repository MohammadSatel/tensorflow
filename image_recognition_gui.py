import tkinter as tk
from tkinter import filedialog

def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        print(f"Selected file: {file_path}")

# Create the main GUI window
root = tk.Tk()
root.title("Image Recognition")

# Create and configure widgets
open_button = tk.Button(root, text="Open Image", command=open_file_dialog)
open_button.pack(pady=10)

# Run the GUI
root.mainloop()
