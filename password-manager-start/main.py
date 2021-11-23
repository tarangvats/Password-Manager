from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    p1 = [choice(letters) for _ in range(randint(8, 10))]
    p2 = [choice(symbols) for _ in range(randint(2, 4))]
    p3 = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = p1 + p2 + p3

    shuffle(password_list)


    pas = "".join(password_list)
    password.insert(0,pas)
    pyperclip.copy(pas)





# ---------------------------- SAVE PASSWORD ------------------------------- #
import pandas

dict = {}
dict["website"] = []
dict["username"] =[]
dict["password"] = []
df = pandas.DataFrame(dict)

def add():


    if len(password.get())==0 or len(website.get())==0 or len(email.get())==0:
        messagebox.showinfo(title = 'important Update', message = "please dont leave any field Empty")
    else:

        isok = messagebox.askokcancel(title = website.get(),message = f"These are the details entered: \nEmail: {email.get()}"
                                                                f"\nPassword:{password.get()}\n Is it ok to Save?")
        if isok:
            with open("file.txt", 'a') as f:
                f.write(f"{website.get()} | {email.get()} | {password.get()}\n")

            new_row = [website.get(),email.get(),password.get()]
            df.loc[len(df.index)] = new_row
            df.to_csv("passwords.csv")

            website.delete(0, END)
            password.delete(0, END)
            messagebox.showinfo(title="Important Update", message="Your password has been saved")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width=700,height=700)
window.config(padx= 50,pady =50)

canvas = Canvas(width =200,height = 200,highlightthickness=0)
photo = PhotoImage(file="logo.png")
logo = canvas.create_image(100,100,image = photo)
canvas.grid(column = 1,row=1)


website_label = Label(text = "Website: " ,font = ('Arial',20))
website_label.grid(column = 0,row = 2)

email_label = Label(text = "Email/Username: ", font =('Arial',20) )
email_label.grid(column = 0, row =3)

password_label = Label(text = "Password: ", font =('Arial',20) )
password_label.grid(column = 0, row =4)

website = Entry(width = 35)
website.focus()
website.grid(column = 1, row = 2,columnspan =2)

email = Entry(width = 35)
email.insert(0,"vats.tarang@gmail.com")
email.grid(column = 1, row = 3,columnspan =2)

password = Entry(width = 21)
password.grid(column =1, row = 4)







Add = Button(text = "Add",command=add, width =36)
Add.grid(column = 1, row =5,columnspan =2)

generate_password = Button(text = "Generate password",command = generate)
generate_password.grid(column = 2, row =4)
window.mainloop()