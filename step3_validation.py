import tkinter as tk  # Import the library (tk is shorter to type)
from tkinter import messagebox  # For pop-up messages (e.g., "Registration successful!")

root = tk.Tk()  # Create the main window object
root.title("Northbridge Registration Form")  # Sets window title bar text
root.geometry("400x450")  # Width x Height in pixels
root.config(bg='#F2F2F2') # House Style

# Label widget - just displays text
tk.Label(root, text="Name:").grid(row=0, column=0)

# Entry widget - user can type here
name_entry = tk.Entry(root, width=30)  # Width in characters
name_entry.grid(row=0, column=1, padx=10, pady=5)

# Label widget - just displays text
tk.Label(root, text="Email:").grid(row=1, column=0)

# Entry widget - user can type here
email_entry = tk.Entry(root, width=30)  # Width in characters
email_entry.grid(row=1, column=1, padx=10, pady=5)

def submit_form():
    if "@" not in email_entry.get():
        messagebox.showerror("Invalid Email", "Please enter a valid email address")

# Label widget - just displays text
tk.Label(root, text="Phone:").grid(row=2, column=0)

# Entry widget - user can type here
phone_entry = tk.Entry(root, width=30)  # Width in characters
phone_entry.grid(row=2, column=1, padx=10, pady=5)
    
submit_btn = tk.Button(root, text="Submit", bg="#38bdf8",
                       fg="white", font=("Arial", 12, "bold"),
                       command=submit_form).grid(row=3, column=1, padx=10, pady=5)


root.mainloop()