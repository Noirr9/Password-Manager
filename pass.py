from tkinter import *
from tkinter import messagebox
from random import randint, choice , shuffle
import pyperclip


violet_colour = "#9195F6" 
green_colour = "#9BCF53"

#---------------------------------- generate password---------------------------#

def generate_password():
    letters = ['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E',
            'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!','@','#','$','%','&','+',]

    password_letters = [choice(letters) for _ in range (randint(4, 6))]
    password_numbers = [choice(numbers) for _ in range (randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range (randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

#---------------------------------- save password ------------------------------#

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops!", message="Please fill up all the fields.")
    else:
        right = messagebox.askokcancel(title=website, message=f"These are the details entered:\n Email: {email}\n Password: {password}\n Is it okay to save it?")
        if right:    
            with open("akash.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0,END)


#----------------------------------- UI setup-----------------------------------#

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=green_colour)
window.minsize(width=540, height=400)

#canvas
logo = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200,  bg= green_colour , highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=2)

#label  
website_label = Label(text="Website:", bg=green_colour)
website_label.grid(row=1, column=1, pady=3 )
email_label = Label(text="Email/Username:", bg=green_colour)
email_label.grid(row=2, column=1, pady=3)
password_label = Label(text="Password:", bg=green_colour)
password_label.grid(row=3, column=1, pady=5)


#entry
website_entry = Entry(width=43)
website_entry.focus()
website_entry.grid(row=1, column=2, sticky="w",)
email_entry = Entry(width=43)
email_entry.insert(0, "akash@gmail.com")
email_entry.grid(row=2, column=2, sticky="w")
password_entry = Entry(width=24)
password_entry.grid(row=3, column=2, sticky="w")


#Button 
generate_button = Button(text="Generate Password", highlightthickness=0, bg=violet_colour, command=generate_password)
generate_button.grid(row=3, column=2, sticky="E")
add_button = Button(text="Add", width=36, highlightthickness=0, bg=violet_colour, command=save)
add_button.grid(row=4, column=2)



window.mainloop()