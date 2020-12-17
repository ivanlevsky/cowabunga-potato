from tkinter import *
from tkinter import filedialog as fd

textString = ""
root = Tk()
root.title("my editor")
frame = Frame(root)
frame.pack()
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
text = Text(root, yscrollcommand=scrollbar.set)
text.pack(side=BOTTOM)
filename = ""


def read_text():
    global filename
    filename = fd.askopenfilename()
    print("read file：" + filename)
    if filename != "":
        with open(filename, encoding='gbk') as f:
            text_string = f.read()
            text.delete('1.0', END)
            text.insert(INSERT, text_string)
            text.insert(END, "")


def save_text():
    global filename
    print("save file as：" + filename)
    write_text = text.get('1.0', END)
    if filename != "":
        with open(filename, 'w', encoding='gbk') as f:
            f.write(str(write_text))


open_button = Button(frame, text="open", command=read_text)
open_button.pack(side=LEFT)
save_button = Button(frame, text="save", command=save_text)
save_button.pack(side=LEFT)
root.mainloop()
