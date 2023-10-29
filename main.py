from tkinter import *
from tkinter import messagebox
import random
window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)







def generate_pass():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)



    letter_list = [random.choice(letters) for _ in range(nr_letters)]
    symbol_list = [random.choice(numbers) for _ in range(nr_symbols)]
    num_list = [random.choice(symbols) for _ in range(nr_numbers)]


    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)


    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_list = letter_list + symbol_list + num_list

    random.shuffle(password_list)


    # password = ""
    # for char in password_list:
    #   password += char
    password = "".join(password_list)
    print(f"Your password is: {password}")



#SAVE PASSWORD ------------------------------------ #


def save_data():
    user = input_username
    web = input_website
    passw = input_password

    if int(len(user.get())) == 0 or int(len(web.get())) == 0  or int(len(passw.get()) == 0):
        fill = messagebox.showerror(title="Warning", message="Please do not leave any blanks")


    else:
        messagebox.askokcancel(title=f"{web.get()}",
                                       message=f" \n These are the details entered:\n User:{user.get()} ,\n Password:{passw.get()}\n")
        with open("data.text", "a") as data_file:
                data_file.write(user.get() + "/" + web.get() + "/" + passw.get() + "\n")
                """Delete , as it word it deletes what you wrote once you press accept"""
                web.delete(0,END)
                passw.delete(0,END)


    # top = Toplevel(window)
    # top.geometry("100x50")
    # top.title("Great")
    # mess = Label(top, text="Succesfully Saved", font=('Mistral 10 bold'))
    # mess.grid(column=1, row=1)
    # but = Button(top,text="Ok" ,command=top.destroy)
    # but.grid(column=1,row=2)


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

generate_btn = Button(text="Generate Password" , command=generate_pass)
generate_btn.grid(column=4 ,row=3, columnspan=2)

add_btn = Button(text="Add", width=50 , command=save_data)
add_btn.grid(column=1 ,row=6)

window.mainloop()

