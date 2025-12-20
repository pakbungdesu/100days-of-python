"""
Password Manager GUI Application
Features: Random password generation, clipboard integration via Pyperclip,
JSON-based local data storage, and record searching with Error Handling.
"""

import pyperclip
import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

# ------------------------ Constant ------------------------
WHITE = "#CBDCEB"
FONT_NAME = "Verdana"

# ------------------------ Generate random password ------------------------

def generate_password():
    """
    Generates a secure, random password containing letters, numbers, and symbols.
    Clears current entry, inserts the new password, and copies it to the clipboard.
    """
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # List comprehensions for random selection
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    # Update UI and Clipboard
    password_entry.delete(0, END)  # Clear existing text first
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ------------------------ Data Management ------------------------

def search():
    """
    Searches the JSON data file for a specific website.
    Uses Try/Except to handle missing files and if/else for missing keys.
    """
    website = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


def save():
    """
    Validates entry fields and saves data to both JSON and TXT formats.
    Handles JSON file creation and update logic.
    """
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    # Validation: Ensure no fields are empty
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(message="Please make sure you haven't left any fields empty.")
    else:
        # Ask for user confirmation before saving
        is_ok = messagebox.askokcancel(title=website, message=f"Details entered:\nEmail: {email}\n"
                                                              f"Password: {password}\nIs it okay to save?")
        if is_ok:
            # Handle JSON update (Read -> Update -> Write)
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                data = {}

            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

            # Redundant backup to TXT format
            with open("data.txt", "a") as txt_file:
                txt_file.write(f"{website} | {email} | {password}\n")

            # Clear UI for next entry
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ------------------------ UI Setup ------------------------

window = Tk()
window.title("Password Manager")
window.config(padx=80, pady=80, background=WHITE)

# Canvas: Logo display
canvas = Canvas(width=200, height=200, background=WHITE, highlightthickness=0)
key_img = PhotoImage(file="logo_pw.png")
canvas.create_image(100, 100, image=key_img)
canvas.grid(row=0, column=1)

# Label
website_label = Label(text="Website:", bg=WHITE, font=(FONT_NAME, 10))
website_label.grid(row=2, column=0, sticky="W")

blank1 = Label(text="blank space", fg=WHITE, bg=WHITE, font=(FONT_NAME, 1))
blank1.grid(row=3, column=0)

email_label = Label(text="Email/Username:", bg=WHITE, font=(FONT_NAME, 10))
email_label.grid(row=4, column=0, sticky="W")

blank2 = Label(text="blank space", fg=WHITE, bg=WHITE, font=(FONT_NAME, 1))
blank2.grid(row=5, column=0)

password_label = Label(text="Password:", bg=WHITE, font=(FONT_NAME, 10))
password_label.grid(row=6, column=0, sticky="W")

blank3 = Label(text="blank space", fg=WHITE, bg=WHITE, font=(FONT_NAME, 1))
blank3.grid(row=7, column=0)


# Entry
website_entry = Entry(width=33)
website_entry.insert(END, string="")
website_entry.grid(row=2, column=1, padx=(80, 0))

email_entry = Entry(width=50)
email_entry.insert(END, string="")
email_entry.grid(row=4, column=1, columnspan=2, sticky="E")

password_entry = Entry(width=33)
password_entry.insert(END, string="")
password_entry.grid(row=6, column=1, padx=(80, 0))

# Button
search_button = Button(text="Search", width=12, command=search)
search_button.grid(row=2, column=2, sticky="W")

generate_button = Button(text="Generate", width=12, command=generate_password)
generate_button.grid(row=6, column=2, sticky="W")

add_button = Button(text="Add", width=42, command=save)
add_button.grid(row=8, column=1, columnspan=2, sticky="E")

window.mainloop()
