from privates import EMAIL_ADDRESS
import pandas
from tkinter import *
from tkinter import messagebox
import random
import json
main_email_address = EMAIL_ADDRESS


# ---------------------------- SEARCH FUNCTION ------------------------------- #

def search():
    try:
        with open("Data.json", "r") as data_file:
            data = json.load(data_file)
            website = website_entry.get()

            messagebox.showinfo(title="Search result", message=f"Website: {website}\nUsername: {data[website]['email']}\nPassword: {data[website]['password']}")


    except FileNotFoundError:
        messagebox.showinfo(title="Ooops", message="You haven't saved any passwords yet.")
    except KeyError:
        messagebox.showinfo(title="Ooops", message="That entry doesn't exist, check your spelling.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for i in range(nr_letters)]
    password_numbers = [random.choice(numbers) for i in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for i in range(nr_symbols)]

    password = password_symbols + password_numbers + password_letters

    random.shuffle(password)

    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(f"{''.join(password)}")
    r.update()  # now it stays on the clipboard after the window is closed
    r.destroy()
    messagebox.showinfo(title="Generate Password", message="Copied to clipboard!")

    password_entry.delete(0, 'end')
    password_entry.insert(0, f"{''.join(password)}")



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_data = {
        website_entry.get(): {
            "email": email_entry.get(),
            "password": password_entry.get(),
        }
    }
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0 or len(email_entry.get()) == 0:
        messagebox.showinfo(title="Ooops", message="Please don't leave any fields empty")
    #else:
    #    is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"These are the details entered:\n\nEmail: {email_entry.get()}\nPassword: {password_entry.get()}\n\nClick OK to confirm.")

    #if is_ok:
    else:
        try:
            with open("Data.json", "r") as data_file:
                data = json.load(data_file)
                # data.update(new_data)
                # json.dump(data, data_file, indent=4)
        except FileNotFoundError:
            with open("Data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("Data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, highlightthickness=0, bg="white")

lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
#timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(row=0,column=1)

website_label = Label(text="Website:", bg="white")
website_label.grid(row=1,column=0)

website_entry = Entry(width=34)
website_entry.focus()
website_entry.grid(row=1,column=1)

#SEARCH BUTTON
search_button = Button(text="Search", width=15, command=search)
search_button.grid(row=1, column=2)

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(row=2,column=0)

email_entry = Entry(width=54)
email_entry.insert(END, main_email_address)
email_entry.grid(row=2,column=1, columnspan=2)

password_label = Label(text="Password:", bg="white")
password_label.grid(row=3,column=0)

password_entry = Entry(width=34)
password_entry.grid(row=3,column=1)

password_button = Button(text="Generate Password", width=15, command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=46, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()