from tkinter import *
from tkinter import messagebox
import base64
import os


def decrypt():
    password = code.get()

    if password == "12345":
        screen2 = Toplevel(screen)
        screen2.title("decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="green")

        message = text1.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt = base64_bytes.decode("ascii")

        Label(screen2, text="DECRYPT", font="arial",
              fg="black", bg="white").place(x=10, y=0)
        text2 = Text(screen2, font="Arial", bg="white",
                     relief=GROOVE, wrap=WORD, bd=2)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, decrypt)

    elif password == "":
        messagebox.showerror("decryption", "Input Password")

    elif password != "12345":
        messagebox.showerror("decryption", "Wrong Password")


def encrypt():
    password = code.get()

    if password == "12345":
        screen1 = Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="red")

        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen1, text="ENCRYPT", font="arial",
              fg="black", bg="white").place(x=10, y=0)
        text2 = Text(screen1, font="Arial", bg="white",
                     relief=GROOVE, wrap=WORD, bd=2)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, encrypt)

    elif password == "":
        messagebox.showerror("encryption", "Input Password")

    elif password != "12345":
        messagebox.showerror("encryption", "Wrong Password")


def main_screen():

    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("375x398")

    # icon
    image_icon = PhotoImage(
        file="/Users/samarthgowda/Python_Projects/message_encrypt_decrypt/keys.png")
    screen.iconphoto(False, image_icon)
    screen.title("PctApp")
    # Start the Tkinter event loop

    def reset():
        code.set("")
        text1.delete(1.0, END)

    Label(text="Enter text for encryption and decryption",
          fg="black", font=("calbri", 15)).place(x=10, y=10)
    text1 = Text(font="Arial", bg="white", relief=GROOVE, wrap=WORD, bd=2)
    text1.place(x=10, y=50, width=355, height=100)

    Label(text="Enter the secret key for encryption and decryption",
          fg="black", font=("calbri", 15)).place(x=10, y=170)

    code = StringVar()
    Entry(screen, textvariable=code, width=19, bd=2,
          font=("Arial", 25), show="*").place(x=10, y=200)

    Button(text="ENCRYPT", height="2", width=23,
           bg="#ed3833", fg="white", border=0, activebackground="#ff4d4d", highlightbackground="#ed3833", command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width=23,
           bg="#00bd56", fg="white", border=0, activebackground="#00e676", highlightbackground="#00bd56", command=decrypt).place(x=200, y=250)
    Button(text="RESET", height="2", width=23,
           bg="#1089ff", fg="white", border=0,  activebackground="#66b0ff", highlightbackground="#1089ff", command=reset).place(x=10, y=300)

    screen.mainloop()


# Call the function to open the window
main_screen()
