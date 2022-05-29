from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import colorchooser

root = Tk()
root.title('Ala-Too International University')
root.geometry("500x500")

my_menu = Menu(root)
root.config(menu=my_menu)


def file_new():
    file_new_frame.pack(fill="both", expand=1)


def our_command():
    pass

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New...", command=file_new)
file_menu.add_separator()
file_menu.add_command(label="Save", command=our_command)
file_menu.add_command(label="Save as...", command=our_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=our_command)
edit_menu.add_command(label="Copy", command=our_command)

file_new_frame = Frame(root, width=500, height=500, bg="black")


def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="/gui", title="Select A File", filetypes=(("png files", "*.png"), ("all files", "*.*")))

my_btn = Button(root, text="Open File", command=open).pack()


def open():
    top = Toplevel()
    top.title('AIU')
    lbl = Label(top, text="The Ala-Too International University ").pack()
    lbl = Label(top, text="(Russian: Международный университет «Ала-Тоо»; ").pack()
    lbl = Label(top, text="Kyrgyz: Эл аралык Ататүрк-Алатоо Университети), ").pack()
    lbl = Label(top, text="formerly known as the International Atatürk-Alatoo University, ").pack()
    lbl = Label(top, text="is a private university located in Bishkek, Kyrgyzstan. ").pack()
    lbl = Label(top, text="It was established in 1996. ").pack()
    lbl = Label(top, text="The university offers graduate, master's, ").pack()
    lbl = Label(top, text="and doctoral programs. ").pack()
    lbl = Label(top, text="It is often ranked as one of Kyrgyzstan's most prestigious universities.").pack()

btn = Button(root, text="AIU(click for more information)", command=open).pack()


def color():
    my_color = colorchooser.askcolor()[1]
    my_label = Label(root, text=my_color).pack(pady=10)
    my_label2 = Label(root, text="You Picked a Color!", bg=my_color).pack()

my_button = Button(root, text="Choose a Color", command=color).pack()

canvas = Canvas(root, width=300, height=300)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("alatoo.png"))
canvas.create_image(20, 20, anchor=NW, image=img)


button_quit = Button(root, text='Exit Program', command=root.quit)
button_quit.pack()


root.mainloop()
