import sys
from tkinter import *
from tkinter import messagebox
var = ""
A = 0
operator = ""

root = Tk();
root.title('Kalkulator Łukasz Groszyk');
root.geometry('350x450');

expression="" 
input_text = StringVar()

def btn_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression="" 

def btn_clear():
    txtDisplay.delete(0,END);
 
num1 = StringVar();
txtDisplay = Entry(root, textvariable = num1, relief=RIDGE, bd = 1, width=33,    insertwidth = 1, font = 20);
txtDisplay.place(x=15, y=10);
txtDisplay.focus();


def btn_click(item):
    current_value = num1.get()
    num1.set(current_value + item)
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression=""



zero_Button = Button(root, text='0', width=20, height=3, bg='red', fg='yellow', command = lambda: btn_click('0')).place(x=17,y=382);
one_Button = Button(root, text='1', width=8, height=3, bg='red', fg='yellow', command = lambda: btn_click('1')).place(x=17, y=302);
two_Button = Button(root, text='2', width=8, height=3, bg='red', fg='yellow', command = lambda: btn_click('2')).place(x=100, y=302);
three_Button = Button(root, text='3', width=8, height=3, bg='red', fg='yellow',command = lambda: btn_click('3')).place(x=182, y=302);
four_Button = Button(root, text='4', width=8, height=3, bg='red', fg='yellow',command = lambda: btn_click('4')).place(x=17, y=222);
five_Button = Button(root, text='5', width=8, height=3, bg='red', fg='yellow',command = lambda: btn_click('5')).place(x=100, y=222);
six_Button = Button(root, text='6', width=8, height=3, bg='red', fg='yellow',command = lambda: btn_click('6')).place(x=182, y=222);
seven_Button = Button(root, text='7', width=8, height=3, bg='red', fg='yellow',command = lambda: btn_click('7')).place(x=17, y=142);
eight_Button = Button(root, text='8', width=8, height=3, bg='red', fg='yellow',command = lambda: btn_click('8')).place(x=100, y=142);
ninth_Button = Button(root, text='9', width=8, height=3, bg='red', fg='yellow',command = lambda: btn_click('9')).place(x=182, y=142);

decimal_Button = Button(root, text='.', width=8, height=3, bg='powder blue',command = lambda: btn_click('.')).place(x=182, y=382);
equal_Button = Button(root, text='=', width=8, height=8, bg='Lightgreen',command=lambda: btn_equal('=')).place(x=264, y=307);
plus_Button = Button(root, text='+', width=8, height=3, bg='gray', command = lambda: btn_click('+')).place(x=264, y=222);
minus_Button = Button(root, text='-', width=8, height=3, bg='gray',command = lambda: btn_click('-')).place(x=264, y=142);
multiply_Button = Button(root, text='x', width=8, height=3, bg='gray',command = lambda: btn_click('x')).place(x=264, y=66);
divide_Button = Button(root, text='÷', width=8, height=3, bg='gray',command = lambda: btn_click('÷')).place(x=182, y=66);
clear_Button = Button(root, text='CE (Wyczyść)', width=20, height=3, command = lambda: btn_clear(), bg='Orange').place(x=17, y=66);

root.maxsize(350,450);
root.minsize(350,450);
root.configure(background = 'purple');
root.mainloop();