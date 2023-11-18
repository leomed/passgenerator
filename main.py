from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

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

    passwor = "".join(password_list)

    """With insert i can see the password generated in the input"""
    password.insert(0, passwor)

    pyperclip.copy(passwor)



#SAVE PASSWORD ------------------------------------ #


def save_data():
    """This variables are the inputs created below"""


    user = username.get()
    web = website.get()
    passw = password.get()

    new_data = {

        web: {
            "user/email": user,
            "password": passw
         }


    }

    """Be careful to use .get!!"""
    """If the user forgets to write something it pop out an error"""
    if int(len(user)) == 0 or int(len(web)) == 0 or int(len(passw) == 0):
        fill = messagebox.showerror(title="Warning", message="Please do not leave any blanks")

    else:
        try:
            #Read old data
            with open("data.json", "r") as data_file:
                # Load is used to read the data inside the file
                data = json.load(data_file)

        except FileNotFoundError:
            #If the file does not exist , create it
            with open("data.json", "w") as data_file:
                json.dump(new_data,data_file, indent=4)
        else:
            # Update old date with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data,data_file,indent=4)
        finally:
            website.delete(0, END)
            password.delete(0, END)

def search_data():
        #It is neccessary to use get to work with the entrys
        website_s = website.get()
        try:
            with open("data.json") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
                messagebox.showinfo(title="Warning", message="This data file does not exist")
        else:
            #Iterating the dictionary in the json file
            if website_s in data:
                email = data[website_s]["user/email"]
                password = data[website_s]["password"]
                messagebox.showinfo(title=website_s, message=f"Email:{email} \n Password:{password}")
            else:
                messagebox.showinfo(title="Warning", message=f"No details for {website_s}")









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

website = Entry(width=50)
website.grid( column=1, row=1,columnspan=2)
website.focus()
"""Focus allow to put the cursor in the entry"""

username = Entry(width=50)
username.grid( column=1, row=2,columnspan=2)
username.insert(0,"leo@hotmail.com")
"""Insert pre-write the text in the app"""

password = Entry(width=50)
password.grid(column=1, row=3 , columnspan=2)


#Button

search_btn = Button(text="Search", width=14 , command=search_data)
search_btn.grid(column=4 ,row=1, columnspan=2)

generate_btn = Button(text="Generate Password" , command=generate_pass)
generate_btn.grid(column=4 ,row=3, columnspan=2)

add_btn = Button(text="Add", width=50 , command=save_data)
add_btn.grid(column=1 ,row=6)

window.mainloop()

