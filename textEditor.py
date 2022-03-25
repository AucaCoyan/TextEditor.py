import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

# This is a global, and it shouldn't
filename = None


def new_file():
    global filename
    filename = "Untitled"
    text.delete("1.0", tk.END)


def save_file():
    # saves the file
    # currently saves the file as "Untitled", WIP
    global filename
    text_to_save = str(text.get(0.0, tk.END))
    f = open(filename, "w")
    f.write(text_to_save)
    f.close()


def save_as():
    name = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    t = text.get("1.0", tk.END)
    try:
        name.write(t.rstrip())
    except:
        messagebox.showerror(title="Oops!", message="Unable to save file...")


def open_file():
    f = filedialog.askopenfile(mode="r")
    t = f.read()
    text.delete("1.0", tk.END)
    text.insert("1.0", t)


root = tk.Tk()
root.title("My Python Text Editor")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)  # same size so user cant resize the window

text = tk.Text(root, width=400, height=400)
text.pack()

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar)
filemenu.add_command(label="New", command=new_file)
filemenu.add_command(label="Open", command=open_file)
#filemenu.add_command(label="Save", command=save_file)
filemenu.add_command(label="Save As", command=save_as)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()
