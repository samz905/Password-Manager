from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

EMAIL = "test@protonmail.com"


# ----------------------------- SEARCH PASSWORD -------------------------------- #

def search():
    website = entry_website.get()

    try:
        with open("passwords.json", "r") as file:
            file_data = json.load(file)

    except FileNotFoundError:
        messagebox.showwarning(title="Oops", message="No password stored for the entered website")

    else:
        try:
            website_data = file_data[website]
            email = website_data["email"]
            password = website_data["password"]

        except KeyError:
            messagebox.showwarning(title="Oops", message="No password stored for the entered website")

        else:
            messagebox.showinfo(title=website, message=f"There are the details for {website}: \n\n Email: {email} \n "
                                                       f"Password: {password} \n\n Press Okay to save info")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = ""

    letters_combination = "".join(random.choice(letters) for _ in range(random.randint(8, 10)))
    password += letters_combination

    char_combination = "".join(random.choice(symbols) for _ in range(random.randint(2, 4)))
    password += char_combination

    numbers_combination = "".join(random.choice(numbers) for _ in range(random.randint(2, 4)))
    password += numbers_combination

    password_list = list(password)
    random.shuffle(password_list)
    password = "".join(password_list)

    entry_password.delete(0, END)
    entry_password.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

header = False

passwords_dict = {
    "Website": [],
    "Email": [],
    "Password": []
}


def save_password():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    data = {
        website:
            {
                "email": email,
                "password": password,
            }}

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"There are the details entered: \n\n Email: {email} \n "
                                                              f"Password: {password} \n\n Press Okay to save info")

        if is_ok:
            try:
                with open("passwords.json", "r") as file:
                    file_data = json.load(file)

            except FileNotFoundError:
                with open("passwords.json", "w") as file:
                    json.dump(data, file, indent=2)

            else:
                file_data.update(data)
                with open("passwords.json", "w") as file:
                    json.dump(file_data, file, indent=2)

            finally:
                entry_website.delete(0, END)
                entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Window setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas setup
canvas = Canvas(width=200, height=200)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(120, 100, image=tomato_img)
canvas.grid(column=1, row=0)

# Labels
label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

label_email = Label(text="Email/Username:")
label_email.grid(column=0, row=2)

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

# Entries
entry_website = Entry(width=21)
entry_website.grid(column=1, row=1)
entry_website.focus()

entry_email = Entry(width=38)
entry_email.grid(column=1, row=2, columnspan=2)
entry_email.insert(END, EMAIL)

entry_password = Entry(width=21)
entry_password.grid(column=1, row=3)

# Buttons
button_generate_password = Button(text="Generate Password", width=13, command=generate_password)
button_generate_password.grid(column=2, row=3)

button_search = Button(text="Search", width=13, command=search)
button_search.grid(column=2, row=1)

button_add = Button(text="Add Password", width=36, command=save_password)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
