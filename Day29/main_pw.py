
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
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(numbers) for _ in range(nr_symbols)]
    password_numbers = [choice(symbols) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)



# ------------------------ Document ------------------------

def search():
    website = website_entry.get()

    try:
        with open("data.json") as data_file:
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
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {  # website is the key
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(message="Please make sure you haven't left any fields empty.")
    else:
        response = messagebox.askokcancel(
            title=website,
            message=f"Email: {email}\nPassword: {password}\nIs it okay to save?"
        )
        if response:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)  # read existing data
            except FileNotFoundError:
                data = {}  # file not found

            data.update(new_data)  # merge the new data into existing data

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)  # write updated data back to file

            # write to a text file
            with open("data.txt", "a") as txt_file:
                txt_file.write(f"{website} | {email} | {password}\n")

            # clear entry fields
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)


# ------------------------ UI Setup ------------------------

# Window
window = Tk()
window.title("Password manager")
window.config(padx=80, pady=80, background=WHITE)


# Canvas
canvas = Canvas(width=300, height=200, background=WHITE, highlightthickness=0)
key_img = PhotoImage(file="logo_pw.png")
canvas.create_image(100, 100, image=key_img)
canvas.grid(row=0, column=1, sticky="E")


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
