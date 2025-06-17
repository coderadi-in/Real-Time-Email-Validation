'''coderadi'''

# ? Importing Libraries
import customtkinter as ctk
from CTkSeparator import CTkSeparator
from CTkMessagebox import CTkMessagebox
import re

# ! The Root Window
root = ctk.CTk()
root.title("Real-time Email Validation")
root.geometry("400x600")
root.minsize(350, 500)

# * Function to validate email
def check_validation(event=None):
    email = event.widget.get()
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    valid = re.search(pattern, email)

    if (not valid) and (email != ""):
        warning.grid(row=6, column=0, sticky="w", padx=5, pady=(0, 5))

    else:warning.grid_forget()

# & Main Heading
ctk.CTkLabel(root, text="Event Signup Form", font=ctk.CTkFont(
    size=32
)).grid(row=0, column=0, sticky="w", padx=5, pady=5)

# & Separator
CTkSeparator(root, length=300, corner_radius=50, fg_color=(
    "#333333", "#EDEDED"
)).grid(row=1, column=0, sticky="ew", padx=5, pady=(0, 5))

# | Form Content
# & Name
ctk.CTkLabel(root, text="Name").grid(row=2, column=0, sticky="w", padx=5, pady=5)
name = ctk.CTkEntry(root, placeholder_text="Enter your name")
name.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

# & Email
ctk.CTkLabel(root, text="Email").grid(row=4, column=0, sticky="w", padx=5, pady=5)
email = ctk.CTkEntry(root, placeholder_text="Enter your Email")
email.grid(row=5, column=0, padx=5, pady=(5, 1), sticky="ew")
email.bind("<KeyRelease>", check_validation)
warning = ctk.CTkLabel(root, text="Email is not Valid!", text_color="#C75050", font=ctk.CTkFont(
    size=10
))

# & Phone
ctk.CTkLabel(root, text="Phone").grid(row=7, column=0, sticky="w", padx=5, pady=5)
phone = ctk.CTkEntry(root, placeholder_text="Enter your Phone")
phone.grid(row=8, column=0, padx=5, pady=5, sticky="ew")

# & Signup Button
ctk.CTkButton(root, text="Signup", command=lambda: [
    CTkMessagebox(title="Event Signup Form", message="You're signup up successfully!")
]).grid(row=9, column=0, padx=5, pady=5)

# * Responsiveness
root.grid_columnconfigure(ctk.ALL, weight=1)

# ! Run the App
root.mainloop()