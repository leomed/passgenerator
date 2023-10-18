from tkinter import *


window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)











#SAVE PASSWORD ------------------------------------ #


def save_data():
    user = input_username
    web = input_website
    passw = input_password


    with open("data.text", "a") as data_file:
        data_file.write(user.get() + "/" + web.get() + "/" + passw.get() + "\n")

    top = Toplevel(window)
    top.geometry("100x50")
    top.title("Great")
    mess = Label(top, text="Succesfully Saved", font=('Mistral 10 bold'))
    mess.grid(column=1, row=1)
    but = Button(top,text="Ok" ,command=top.destroy)
    but.grid(column=1,row=2)


# Ui -------------------------------------------- #
canvas = Canvas(width=400,height=245, highlightthickness=0)
lock_img = PhotoImage(file="lock.png")
canvas.create_image(200,100, image=lock_img)
canvas.grid(column=1,row=0)

#Labels

row_one_label = Label(text="Website")
row_one_label.grid(column=0,row=1)


row_two_label = Label(text="Email/Username:")
row_two_label.grid(column=0,row=2)


row_three_label = Label(text="Password")
row_three_label.grid(column=0,row=3)


#Inputs

input_website = Entry(width=50)
input_website.grid( column=1, row=1,columnspan=2)
input_website.focus()
"""Focus allow to put the cursor in the entry"""

input_username = Entry(width=50)
input_username.grid( column=1, row=2,columnspan=2)
input_username.insert(0,"leo@hotmail.com")
"""Insert pre-write the text in the app"""

input_password = Entry(width=50)
input_password.grid(column=1, row=3 , columnspan=2)


#Button

generate_btn = Button(text="Generate Password")
generate_btn.grid(column=4 ,row=3, columnspan=2)

add_btn = Button(text="Add", width=50 , command=save_data)
add_btn.grid(column=1 ,row=6)

window.mainloop()

