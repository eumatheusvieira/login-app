from tkinter import *
from tkinter import messagebox
import ast

window = Tk()
window.title("Sign Up")
window.geometry("925x500+300+200")
window.configure(bg="#fff")
window.resizable(False, False)

def singup():
    username = user.get()
    password = code.get()
    confirmar = confirm.get()

    if password == confirmar:
        try:
            file = open("datasheet.txt", "r+")
            d = file.read()
            r=ast.literal_eval(d)

            dict2 = {username:password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file = open("datasheet.txt", "w")
            w = file.write(str(r))

            messagebox.showinfo("Signup", "Sucessfully sign up")

        except:
            file = open("datasheet.txt", "w")
            pp = str({"Username" : "Password"})
            file.write(pp)
            file.close()

    else:
        messagebox.showerror("Invalid", "Both Password should match")

img = PhotoImage(file="login.png")
Label(window, image=img, border=0,bg="white").place(x=50, y=90)

frame=Frame(window, width=350, height=390, bg="#fff")
frame.place(x=500, y=50)

heading = Label(frame, text="Sign Up", fg="#3486eb", bg="white", font=("Microsoft Yahei UI Light", 23, 'bold'))
heading.place(x=100, y = 5)

##-------------------------------------

def on_enter(e):
    user.delete(0, "end")
def on_leave(e):
    if user.get()=="":
        user.insert(0, "Username")


user= Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11,))
user.place(x=30, y=80)
user.insert(0, "Username")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25,y=107)

##-------------------------------------

def on_enter(e):
    code.delete(0, "end")
def on_leave(e):
    if code.get()=="":
        code.insert(0, "Password")


code= Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11,))
code.place(x=30, y=150)
code.insert(0, "Password")
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25,y=177)

##-------------------------------------

def on_enter(e):
    confirm.delete(0, "end")
def on_leave(e):
    if confirm.get()=="":
        confirm.insert(0, "Confirm Password")


confirm = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11,))
confirm.place(x=30, y=220)
confirm.insert(0, "Confirm Password")
confirm.bind("<FocusIn>", on_enter)
confirm.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25,y=247)

##-------------------------------------

Button(frame, width=39, pady=7, text="Sign Up", bg="#3486eb", fg="white", border=0, cursor="hand2", command=singup).place(x=35, y=280)
label=Label(frame, text="Have an Account?", fg="black", bg="white", font=("Microsoft Yahei UI Light", 9))
label.place(x=90, y=340)

signin = Button(frame, width=6, text="Sign in", border= 0, bg="white", cursor="hand2", fg="#3486eb")
signin.place(x=200, y=340)


window.mainloop()