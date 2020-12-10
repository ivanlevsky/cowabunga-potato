# encoding = utf-8
from tkinter import *
from decimal import Decimal
import re, math

text_string = ""
root = Tk()
root.title('My Calculator')
top_frame = Frame(root)
top_frame.pack(side=TOP)
mid_frame = Frame(root)
mid_frame.pack()
bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)

botton_texts = ['x²', 'x∧y', 'sin', 'cos', 'tan',
                '√', '10∧x', 'log', 'Exp', 'Mod',
                '↑', 'CE', 'C', '⇦', '÷',
                'π', '7', '8', '9', '×',
                'n!', '4', '5', '6', '－',
                '±', '1', '2', '3', '＋',
                '(', ')', '0', '.', '＝'
                ]


def get_button_text(event, text):
    all_text.append(text)
    input_text.set(''.join(all_text))


def clear_all_text():
    del all_text[-len(all_text):]
    input_text.set('')


def get_result_text():
    if input_text.get() != '':
        if re.search(r'^(\d+(\.\d+)?[＋－×÷]{1})+\d+(\.\d+)?$', input_text.get()):
            textArea.insert(INSERT,
                            '%s %s = %s' % ('Formular Correct！！\n', input_text.get(), calculate(input_text.get())),
                            'clear')
        elif re.search(r'^\d+(\.\d+)?Mod|x∧y\d+(\.\d+)?$', input_text.get()):
            textArea.insert(INSERT, '%s %s = %s' % (
                'Formular Correct！！\n', input_text.get().replace('Mod', ' Mod ').replace('x∧y', ' x∧y '),
                calculate(input_text.get())), 'clear')
        elif re.search(r'^(sin|cos|tan|x²|n!|√|10∧x|log)\d+(\.\d+)?$', input_text.get()):
            textArea.insert(INSERT, '%s %s = %s' % (
                'Formular Correct！！\n', input_text.get().replace('10∧x', '10∧x '), calculate(input_text.get())),
                            'clear')
        else:
            textArea.insert(INSERT, '%s,%s' % (input_text.get(), 'Formular Error！！'), 'warning')
            clear_all_text()
        textArea.insert(END, '\n')


def calculate(express):
    nums = list(filter(None, re.split(r'[＋－×÷]|Mod|sin|cos|tan|x²|x∧y|n!|√|10∧x|log', express)))
    cals = list(filter(None, re.split(r'[\d(\.\d+)?]+', express)))
    # print('n0 %s c1 %s n1 %s' % (nums[0],cals[0],nums[1]))
    print('n0 %s c1 %s ' % (nums[0], cals[0]))
    if cals[0] == '＋':
        return float(nums[0]).__add__(float(nums[1]))
    elif cals[0] == '－':
        return float(nums[0]).__sub__(float(nums[1]))
    elif cals[0] == '÷':
        if float(nums[1]) == 0.0:
            textArea.insert(INSERT, 'divided by zero！\n', 'error')
        else:
            return float(nums[0]).__truediv__(float(nums[1]))
    elif cals[0] == '×':
        return float(nums[0]).__mul__(float(nums[1]))
    elif cals[0] == 'Mod':
        return Decimal(nums[0]).__mod__(Decimal(nums[1]))
    elif cals[0] == 'sin':
        return math.sin(math.radians(float(nums[0])))
    elif cals[0] == 'cos':
        return math.cos(math.radians(float(nums[0])))
    elif cals[0] == 'tan':
        if float(nums[0]) == 90.0:
            textArea.insert(INSERT, 'tan90 not exist！\n', 'error')
        else:
            return math.tan(math.radians(float(nums[0])))
    elif cals[0] == 'x²':
        return float(nums[0]).__pow__(2)
    elif cals[0] == 'x∧y':
        return float(nums[0]).__pow__(float(nums[1]))
    elif cals[0] == 'n!':
        return math.factorial(int(nums[0]))
    elif cals[0] == '√':
        return float(nums[0]).__pow__(0.5)
    elif cals[0] == '∧x':
        return float(10).__pow__(float(nums[0]))
    elif cals[0] == 'log':
        return math.log10(float(nums[0]))


for i in range(0, 35):
    button = Button(bottom_frame, text=botton_texts[i], width=6, )
    button.grid(row=int(i / 5), column=i % 5, padx=8, pady=5)

for i in range(0, 35):
    if i == 34:
        bottom_frame.winfo_children()[34].bind('<Button-1>', lambda x: get_result_text())
    elif i == 12:
        bottom_frame.winfo_children()[12].bind('<Button-1>', lambda x: clear_all_text())
    else:
        bottom_frame.winfo_children()[i].bind('<Button-1>', lambda event, i=i: get_button_text(event,
                                                                                               bottom_frame.winfo_children()[
                                                                                                   i].cget('text')))

label = Label(top_frame, text='input')
label.pack(side=LEFT)
global input_text
input_text = StringVar()
global all_text
all_text = []
entry = Entry(top_frame, width=40, textvariable=input_text)
entry.pack(side=LEFT)
label2 = Label(mid_frame, text='result')
label2.pack(side=LEFT)
scrollbar = Scrollbar(mid_frame)
scrollbar.pack(side=RIGHT, fill=Y)
textArea = Text(mid_frame, width=37, height=7, yscrollcommand=scrollbar)
textArea.tag_config('warning', foreground="red")
textArea.tag_config('clear', foreground="green")
textArea.tag_config('error', foreground="blue")
textArea.pack(side=BOTTOM)
root.mainloop()
