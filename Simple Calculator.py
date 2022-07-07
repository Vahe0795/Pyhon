import tkinter
import tkinter.font as tkFont

expression = ""


def number(num):
    global expression
    expression = expression + num.widget['text']
    text.set(expression)


def equals(event):
    try:
        global expression
        total = str(eval(expression))
        text.set(total)
        expression = ""
    except:
        text.set(" error ")
        expression = ""


def delete_display(event):
    result = ''
    text.set(result)


def delete_one_digit(event):
    existing_text = text.get()
    text.set(existing_text[:-1])


main_window = tkinter.Tk()
main_window.title("Simple Calculator")
main_window.geometry('320x299')
main_window.resizable(width=False, height=False)
main_window.configure(background='#b5b5b5')

myFont = tkFont.Font(family="Times New Roman", size=10, weight="bold", slant="roman")

text = tkinter.StringVar()
display = tkinter.Entry(main_window, textvariable=text, state='readonly')
display.grid(column=0, row=0, columnspan=4, sticky='news')

number_1_button = tkinter.Button(main_window, height=3, width=10, text='1', font=myFont, bg="light blue")
number_1_button.grid(column=0, row=4, sticky='news')
number_2_button = tkinter.Button(main_window, height=3, width=10, text='2', font=myFont, bg="light blue")
number_2_button.grid(column=1, row=4, sticky='w')
number_3_button = tkinter.Button(main_window, height=3, width=10, text='3', font=myFont, bg="light blue")
number_3_button.grid(column=2, row=4, sticky='news')
number_4_button = tkinter.Button(main_window, height=3, width=10, text='4', font=myFont, bg="light blue")
number_4_button.grid(column=0, row=3, sticky='news')
number_5_button = tkinter.Button(main_window, height=3, width=10, text='5', font=myFont, bg="light blue")
number_5_button.grid(column=1, row=3, sticky='news')
number_6_button = tkinter.Button(main_window, height=3, width=10, text='6', font=myFont, bg="light blue")
number_6_button.grid(column=2, row=3, sticky='news')
number_7_button = tkinter.Button(main_window, height=3, width=10, text='7', font=myFont, bg="light blue")
number_7_button.grid(column=0, row=2, sticky='news')
number_8_button = tkinter.Button(main_window, height=3, width=10, text='8', font=myFont, bg="light blue")
number_8_button.grid(column=1, row=2, sticky='news')
number_9_button = tkinter.Button(main_window, height=3, width=10, text='9', font=myFont, bg="light blue")
number_9_button.grid(column=2, row=2, sticky='news')
number_0_button = tkinter.Button(main_window, height=3, width=10, text='0', font=myFont, bg="light blue")
number_0_button.grid(column=1, row=5, sticky='news')

point_button = tkinter.Button(main_window, height=3, width=10, text='.', font=myFont, bg="light blue")
point_button.grid(column=2, row=5, sticky='news')
plus_button = tkinter.Button(main_window, height=3, width=10, text='+', font=myFont, bg="light blue")
plus_button.grid(column=3, row=4, sticky='news')
minus_button = tkinter.Button(main_window, height=3, width=10, text='-', font=myFont, bg="light blue")
minus_button.grid(column=3, row=3, sticky='news')
multiplication_button = tkinter.Button(main_window, height=3, width=10, text='*', font=myFont, bg="light blue")
multiplication_button.grid(column=3, row=2, sticky='news')
division_button = tkinter.Button(main_window, height=3, width=10, text='/', font=myFont, bg="light blue")
division_button.grid(column=3, row=1, sticky='news')
equal_button = tkinter.Button(main_window, height=3, width=10, text='=', font=myFont, bg="light blue")
equal_button.grid(column=3, row=5, sticky='news')
delete_button = tkinter.Button(main_window, height=3, width=10, text='C', font=myFont, bg="light blue")
delete_button.grid(column=0, row=5, sticky='news')
delete_button_1 = tkinter.Button(main_window, height=3, width=10, text='DEL', font=myFont, bg="light blue")
delete_button_1.grid(column=0, row=1, sticky='news')
bracket_button_1 = tkinter.Button(main_window, height=3, width=10, text=')', font=myFont, bg="light blue")
bracket_button_1.grid(column=2, row=1, sticky='news')
bracket_button_2 = tkinter.Button(main_window, height=3, width=10, text='(', font=myFont, bg="light blue")
bracket_button_2.grid(column=1, row=1, sticky='news')

number_1_button.bind('<Button-1>', number)
number_2_button.bind('<Button-1>', number)
number_3_button.bind('<Button-1>', number)
number_4_button.bind('<Button-1>', number)
number_5_button.bind('<Button-1>', number)
number_6_button.bind('<Button-1>', number)
number_7_button.bind('<Button-1>', number)
number_8_button.bind('<Button-1>', number)
number_9_button.bind('<Button-1>', number)
number_0_button.bind('<Button-1>', number)

point_button.bind('<Button-1>', number)
plus_button.bind('<Button-1>', number)
minus_button.bind('<Button-1>', number)
multiplication_button.bind('<Button-1>', number)
division_button.bind('<Button-1>', number)
equal_button.bind('<Button-1>', equals)
delete_button.bind('<Button-1>', delete_display)
delete_button_1.bind('<Button-1>', delete_one_digit)
bracket_button_1.bind('<Button-1>', number)
bracket_button_2.bind('<Button-1>', number)

main_window.columnconfigure(0, weight=1)
main_window.mainloop()
