import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title('OnScreen Keyboard')
window.geometry('1140x350')
window.resizable(False, False)

equation = StringVar()
shift_state = False
expression = ""


def shift():
    global shift_state
    shift_state = not shift_state
    widgets()


def button_press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def B_space():
    global expression
    expression = expression[:-1]
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set(expression)


screen = Entry(window, relief=GROOVE, font='Arial 14', textvariable=equation, state='readonly').grid(rowspan=1, columnspan=90, ipadx=550, ipady=30)

def widgets():
    if (shift_state):
        #                       first row capital

        tilda = ttk.Button(window, text='~', width=5, command=lambda: button_press("~")).grid(row=1, ipadx=4, ipady=10)
        one = ttk.Button(window, text='!', width=5, command=lambda: button_press("!")).grid(row=1, column=1, ipadx=4, ipady=10)
        two = ttk.Button(window, text='@', width=5, command=lambda: button_press("@")).grid(row=1, column=2, ipadx=4, ipady=10)
        three = ttk.Button(window, text='#', width=5, command=lambda: button_press("#")).grid(row=1, column=3, ipadx=4, ipady=10)
        four = ttk.Button(window, text='$', width=5, command=lambda: button_press("$")).grid(row=1, column=4, ipadx=4, ipady=10)
        five = ttk.Button(window, text='%', width=5, command=lambda: button_press("%")).grid(row=1, column=5, ipadx=4, ipady=10)
        six = ttk.Button(window, text='^', width=5, command=lambda: button_press("^")).grid(row=1, column=6, ipadx=4, ipady=10)
        seven = ttk.Button(window, text='&', width=5, command=lambda: button_press("&")).grid(row=1, column=7, ipadx=4, ipady=10)
        eight = ttk.Button(window, text='*', width=5, command=lambda: button_press("*")).grid(row=1, column=8, ipadx=4, ipady=10)
        nine = ttk.Button(window, text='(', width=5, command=lambda: button_press("(")).grid(row=1, column=9, ipadx=4, ipady=10)
        zero = ttk.Button(window, text=')', width=5, command=lambda: button_press(")")).grid(row=1, column=10, ipadx=4, ipady=10)
        minus = ttk.Button(window, text='_', width=5, command=lambda: button_press("_")).grid(row=1, column=11, ipadx=4, ipady=10)
        equal = ttk.Button(window, text='+', width=5, command=lambda: button_press("+")).grid(row=1, column=12, ipadx=4, ipady=10)
        b_space = ttk.Button(window, text='<--', width=25, command=B_space).grid(row=1, column=13, ipady=10, columnspan=3)
        num_front_slash = ttk.Button(window, text='/', width=5, command=lambda: button_press("/")).grid(row=1, column=18, ipadx=4, ipady=10)
        num_multiply = ttk.Button(window, text='*', width=5, command=lambda: button_press("*")).grid(row=1, column=19, ipadx=4, ipady=10)
        num_minus= ttk.Button(window, text='-', width=5, command=lambda: button_press("-")).grid(row=1, column=20, ipadx=4, ipady=10)

        #                   second row capital

        tab = ttk.Button(window, text='Tab', width=5, command=lambda: button_press("\t")).grid(row=2, ipadx=4, ipady=10)
        Q = ttk.Button(window, text='Q', width=5, command=lambda: button_press("Q")).grid(row=2, column=1, ipadx=4, ipady=10)
        W = ttk.Button(window, text='W', width=5, command=lambda: button_press("W")).grid(row=2, column=2, ipadx=4, ipady=10)
        E = ttk.Button(window, text='E', width=5, command=lambda: button_press("E")).grid(row=2, column=3, ipadx=4, ipady=10)
        R = ttk.Button(window, text='R', width=5, command=lambda: button_press("R")).grid(row=2, column=4, ipadx=4, ipady=10)
        T = ttk.Button(window, text='T', width=5, command=lambda: button_press("T")).grid(row=2, column=5, ipadx=4, ipady=10)
        Y = ttk.Button(window, text='Y', width=5, command=lambda: button_press("Y")).grid(row=2, column=6, ipadx=4, ipady=10)
        U = ttk.Button(window, text='U', width=5, command=lambda: button_press("U")).grid(row=2, column=7, ipadx=4, ipady=10)
        I = ttk.Button(window, text='I', width=5, command=lambda: button_press("I")).grid(row=2, column=8, ipadx=4, ipady=10)
        O = ttk.Button(window, text='O', width=5, command=lambda: button_press("O")).grid(row=2, column=9, ipadx=4, ipady=10)
        P = ttk.Button(window, text='P', width=5, command=lambda: button_press("P")).grid(row=2, column=10, ipadx=4, ipady=10)
        curly_l = ttk.Button(window, text='{', width=5, command=lambda: button_press("{")).grid(row=2, column=11, ipadx=4, ipady=10)
        curly_r = ttk.Button(window, text='}', width=5, command=lambda: button_press("}")).grid(row=2, column=12, ipadx=4, ipady=10)
        num_seven = ttk.Button(window, text='7', width=5, command=lambda: button_press(7)).grid(row=2, column=17, ipadx=4, ipady=10)
        num_eight = ttk.Button(window, text='8', width=5, command=lambda: button_press(8)).grid(row=2, column=18, ipadx=4, ipady=10)
        num_nine = ttk.Button(window, text='9', width=5, command=lambda: button_press(9)).grid(row=2, column=19, ipadx=4, ipady=10)
        num_plus = ttk.Button(window, text='+', width=5, command=lambda: button_press("+")).grid(row=2, column=20, ipadx=4, ipady=32, rowspan=2)

        #                   third row capital

        A = ttk.Button(window, text='A', width=5, command=lambda: button_press("A")).grid(row=3, column=1, ipadx=4, ipady=10)
        S = ttk.Button(window, text='S', width=5, command=lambda: button_press("S")).grid(row=3, column=2, ipadx=4, ipady=10)
        D = ttk.Button(window, text='D', width=5, command=lambda: button_press("D")).grid(row=3, column=3, ipadx=4, ipady=10)
        F = ttk.Button(window, text='F', width=5, command=lambda: button_press("F")).grid(row=3, column=4, ipadx=4, ipady=10)
        G = ttk.Button(window, text='G', width=5, command=lambda: button_press("G")).grid(row=3, column=5, ipadx=4, ipady=10)
        H = ttk.Button(window, text='H', width=5, command=lambda: button_press("H")).grid(row=3, column=6, ipadx=4, ipady=10)
        J = ttk.Button(window, text='J', width=5, command=lambda: button_press("J")).grid(row=3, column=7, ipadx=4, ipady=10)
        K = ttk.Button(window, text='K', width=5, command=lambda: button_press("K")).grid(row=3, column=8, ipadx=4, ipady=10)
        L = ttk.Button(window, text='L', width=5, command=lambda: button_press("L")).grid(row=3, column=9, ipadx=4, ipady=10)
        colon = ttk.Button(window, text=';', width=5, command=lambda: button_press(":")).grid(row=3, column=10, ipadx=4, ipady=10)
        single_quote = ttk.Button(window, text="'", width=5, command=lambda: button_press('"')).grid(row=3, column=11, ipadx=4, ipady=10)
        enter = ttk.Button(window, text='Enter', width=5, command=lambda: button_press("Enter")).grid(row=3, column=12, ipadx=4, ipady=10)
        num_four = ttk.Button(window, text='4', width=5, command=lambda: button_press(4)).grid(row=3, column=17, ipadx=4, ipady=10)
        num_five = ttk.Button(window, text='5', width=5, command=lambda: button_press(5)).grid(row=3, column=18, ipadx=4, ipady=10)
        num_six = ttk.Button(window, text='6', width=5, command=lambda: button_press(6)).grid(row=3, column=19, ipadx=4, ipady=10)

        #                   fourth row capital

        shift_l = ttk.Button(window, text='Shift', width=5, command=shift).grid(row=4, ipadx=4, ipady=10)
        Z = ttk.Button(window, text='Z', width=5, command=lambda: button_press("Z")).grid(row=4, column=1, ipadx=4, ipady=10)
        X = ttk.Button(window, text='X', width=5, command=lambda: button_press("X")).grid(row=4, column=2, ipadx=4, ipady=10)
        C = ttk.Button(window, text='C', width=5, command=lambda: button_press("C")).grid(row=4, column=3, ipadx=4, ipady=10)
        V = ttk.Button(window, text='V', width=5, command=lambda: button_press("V")).grid(row=4, column=4, ipadx=4, ipady=10)
        B = ttk.Button(window, text='B', width=5, command=lambda: button_press("B")).grid(row=4, column=5, ipadx=4, ipady=10)
        N = ttk.Button(window, text='N', width=5, command=lambda: button_press("N")).grid(row=4, column=6, ipadx=4, ipady=10)
        M = ttk.Button(window, text='M', width=5, command=lambda: button_press("M")).grid(row=4, column=7, ipadx=4, ipady=10)
        chevron_l = ttk.Button(window, text='<', width=5, command=lambda: button_press("<")).grid(row=4, column=8, ipadx=4, ipady=10)
        chevron_r = ttk.Button(window, text='>', width=5, command=lambda: button_press(">")).grid(row=4, column=9, ipadx=4, ipady=10)
        forward_slash = ttk.Button(window, text='?', width=5, command=lambda: button_press("?")).grid(row=4, column=10, ipadx=4, ipady=10)
        shift_r = ttk.Button(window, text="Shift", width=16, command=shift).grid(row=4, column=11, ipady=10, columnspan=2)
        num_one = ttk.Button(window, text='1', width=5, command=lambda: button_press(1)).grid(row=4, column=17, ipadx=4, ipady=10)
        num_two = ttk.Button(window, text='2', width=5, command=lambda: button_press(2)).grid(row=4, column=18, ipadx=4, ipady=10)
        num_three = ttk.Button(window, text='3', width=5, command=lambda: button_press(3)).grid(row=4, column=19, ipadx=4, ipady=10)
        num_enter = ttk.Button(window, text='Enter', width=5, command=lambda: button_press("\n")).grid(row=4, column=20, ipadx=4, ipady=32, rowspan=2)

        #                   fifth row capital

        clear_l = ttk.Button(window, text='Clear', width=16, command=clear).grid(row=5, ipadx=4, ipady=10, columnspan=2)
        space = ttk.Button(window, text='Space', width=90, command=lambda: button_press(" ")).grid(row=5, column=2, ipady=10, columnspan=9)
        clear_r = ttk.Button(window, text='Clear', width=15, command=clear).grid(row=5, column=11, ipadx=4, ipady=10, columnspan=2)
        num_zero = ttk.Button(window, text='0', width=14, command=lambda: button_press("0")).grid(row=5, column=17, ipadx=4, ipady=10, columnspan=2)
        num_comma = ttk.Button(window, text=',', width=5, command=lambda: button_press(",")).grid(row=5, column=19, ipadx=4, ipady=10)

    else:
#                       first row

        tilda = ttk.Button(window, text='`', width=5, command=lambda: button_press("`")).grid(row=1, ipadx=4, ipady=10)
        one = ttk.Button(window, text='1', width=5, command=lambda: button_press(1)).grid(row=1, column=1, ipadx=4, ipady=10)
        two = ttk.Button(window, text='2', width=5, command=lambda: button_press(2)).grid(row=1,column=2, ipadx=4, ipady=10)
        three = ttk.Button(window, text='3', width=5, command=lambda: button_press(3)).grid(row=1, column=3, ipadx=4, ipady=10)
        four = ttk.Button(window, text='4', width=5, command=lambda: button_press(4)).grid(row=1, column=4, ipadx=4, ipady=10)
        five = ttk.Button(window, text='5', width=5, command=lambda: button_press(5)).grid(row=1, column=5, ipadx=4, ipady=10)
        six = ttk.Button(window, text='6', width=5, command=lambda: button_press(6)).grid(row=1, column=6, ipadx=4, ipady=10)
        seven = ttk.Button(window, text='7', width=5, command=lambda: button_press(7)).grid(row=1, column=7, ipadx=4, ipady=10)
        eight = ttk.Button(window, text='8', width=5, command=lambda: button_press(8)).grid(row=1,column=8, ipadx=4, ipady=10)
        nine = ttk.Button(window, text='9', width=5, command=lambda: button_press(9)).grid(row=1, column=9, ipadx=4, ipady=10)
        zero = ttk.Button(window, text='0', width=5, command=lambda: button_press(0)).grid(row=1, column=10, ipadx=4, ipady=10)
        minus = ttk.Button(window, text='-', width=5, command=lambda: button_press("-")).grid(row=1, column=11, ipadx=4, ipady=10)
        equal = ttk.Button(window, text='=', width=5, command=lambda: button_press("=")).grid(row=1, column=12, ipadx=4, ipady=10)
        b_space = ttk.Button(window, text='<--', width=25, command=B_space).grid(row=1, column=13, ipady=10, columnspan=3)
        num_front_slash = ttk.Button(window, text='/', width=5, command=lambda: button_press("/")).grid(row=1, column=18, ipadx=4, ipady=10)
        num_multiply = ttk.Button(window, text='*', width=5, command=lambda: button_press("*")).grid(row=1, column=19, ipadx=4, ipady=10)
        num_minus= ttk.Button(window, text='-', width=5, command=lambda: button_press("-")).grid(row=1, column=20, ipadx=4, ipady=10)

    #                   second row

        tab = ttk.Button(window, text='Tab', width=5, command=lambda: button_press("\t")).grid(row=2, ipadx=4, ipady=10)
        q = ttk.Button(window, text='q', width=5, command=lambda: button_press("q")).grid(row=2, column=1, ipadx=4, ipady=10)
        w = ttk.Button(window, text='w', width=5, command=lambda: button_press("w")).grid(row=2, column=2, ipadx=4, ipady=10)
        e = ttk.Button(window, text='e', width=5, command=lambda: button_press("e")).grid(row=2, column=3, ipadx=4, ipady=10)
        r = ttk.Button(window, text='r', width=5, command=lambda: button_press("r")).grid(row=2, column=4, ipadx=4, ipady=10)
        t = ttk.Button(window, text='t', width=5, command=lambda: button_press("t")).grid(row=2, column=5, ipadx=4, ipady=10)
        y = ttk.Button(window, text='y', width=5, command=lambda: button_press("y")).grid(row=2, column=6, ipadx=4, ipady=10)
        u = ttk.Button(window, text='u', width=5, command=lambda: button_press("u")).grid(row=2, column=7, ipadx=4, ipady=10)
        i = ttk.Button(window, text='i', width=5, command=lambda: button_press("i")).grid(row=2, column=8, ipadx=4, ipady=10)
        o = ttk.Button(window, text='o', width=5, command=lambda: button_press("o")).grid(row=2, column=9, ipadx=4, ipady=10)
        p = ttk.Button(window, text='p', width=5, command=lambda: button_press("p")).grid(row=2, column=10, ipadx=4, ipady=10)
        square_l = ttk.Button(window, text='[', width=5, command=lambda: button_press("[")).grid(row=2, column=11, ipadx=4, ipady=10)
        square_r = ttk.Button(window, text=']', width=5, command=lambda: button_press("]")).grid(row=2, column=12, ipadx=4, ipady=10)
        num_seven = ttk.Button(window, text='7', width=5, command=lambda: button_press(7)).grid(row=2, column=17, ipadx=4, ipady=10)
        num_eight = ttk.Button(window, text='8', width=5, command=lambda: button_press(8)).grid(row=2, column=18, ipadx=4, ipady=10)
        num_nine = ttk.Button(window, text='9', width=5, command=lambda: button_press(9)).grid(row=2, column=19, ipadx=4, ipady=10)
        num_plus = ttk.Button(window, text='+', width=5, command=lambda: button_press("+")).grid(row=2, column=20, ipadx=4, ipady=32, rowspan=2)

    #                   third row

        a = ttk.Button(window, text='a', width=5, command=lambda: button_press("a")).grid(row=3, column=1, ipadx=4, ipady=10)
        s = ttk.Button(window, text='s', width=5, command=lambda: button_press("s")).grid(row=3, column=2, ipadx=4, ipady=10)
        d = ttk.Button(window, text='d', width=5, command=lambda: button_press("d")).grid(row=3, column=3, ipadx=4, ipady=10)
        f = ttk.Button(window, text='f', width=5, command=lambda: button_press("f")).grid(row=3, column=4, ipadx=4, ipady=10)
        g = ttk.Button(window, text='g', width=5, command=lambda: button_press("g")).grid(row=3, column=5, ipadx=4, ipady=10)
        h = ttk.Button(window, text='h', width=5, command=lambda: button_press("h")).grid(row=3, column=6, ipadx=4, ipady=10)
        j = ttk.Button(window, text='j', width=5, command=lambda: button_press("j")).grid(row=3, column=7, ipadx=4, ipady=10)
        k = ttk.Button(window, text='k', width=5, command=lambda: button_press("k")).grid(row=3, column=8, ipadx=4, ipady=10)
        l = ttk.Button(window, text='l', width=5, command=lambda: button_press("l")).grid(row=3, column=9, ipadx=4, ipady=10)
        semicolon = ttk.Button(window, text=';', width=5, command=lambda: button_press(";")).grid(row=3, column=10, ipadx=4, ipady=10)
        single_quote = ttk.Button(window, text="'", width=5, command=lambda: button_press("'")).grid(row=3, column=11, ipadx=4, ipady=10)
        enter = ttk.Button(window, text='Enter', width=5, command=lambda: button_press("Enter")).grid(row=3, column=12, ipadx=4, ipady=10)
        num_four = ttk.Button(window, text='4', width=5, command=lambda: button_press(4)).grid(row=3, column=17, ipadx=4, ipady=10)
        num_five = ttk.Button(window, text='5', width=5, command=lambda: button_press(5)).grid(row=3, column=18, ipadx=4, ipady=10)
        num_six = ttk.Button(window, text='6', width=5, command=lambda: button_press(6)).grid(row=3, column=19, ipadx=4, ipady=10)

    #                   fourth row

        shift_l = ttk.Button(window, text='Shift', width=5, command=shift).grid(row=4, ipadx=4, ipady=10)
        z = ttk.Button(window, text='z', width=5, command=lambda: button_press("z")).grid(row=4, column=1, ipadx=4, ipady=10)
        x = ttk.Button(window, text='x', width=5, command=lambda: button_press("x")).grid(row=4, column=2, ipadx=4, ipady=10)
        c = ttk.Button(window, text='c', width=5, command=lambda: button_press("c")).grid(row=4, column=3, ipadx=4, ipady=10)
        v = ttk.Button(window, text='v', width=5, command=lambda: button_press("v")).grid(row=4, column=4, ipadx=4, ipady=10)
        b = ttk.Button(window, text='b', width=5, command=lambda: button_press("b")).grid(row=4, column=5, ipadx=4, ipady=10)
        n = ttk.Button(window, text='n', width=5, command=lambda: button_press("n")).grid(row=4, column=6, ipadx=4, ipady=10)
        m = ttk.Button(window, text='m', width=5, command=lambda: button_press("m")).grid(row=4, column=7, ipadx=4, ipady=10)
        comma = ttk.Button(window, text=',', width=5, command=lambda: button_press(",")).grid(row=4, column=8, ipadx=4, ipady=10)
        dot = ttk.Button(window, text='.', width=5, command=lambda: button_press(".")).grid(row=4, column=9, ipadx=4, ipady=10)
        forward_slash = ttk.Button(window, text='/', width=5, command=lambda: button_press("/")).grid(row=4, column=10, ipadx=4, ipady=10)
        shift_r = ttk.Button(window, text="Shift", width=16, command=shift).grid(row=4, column=11, ipady=10, columnspan=2)
        num_one = ttk.Button(window, text='1', width=5, command=lambda: button_press(1)).grid(row=4, column=17, ipadx=4, ipady=10)
        num_two = ttk.Button(window, text='2', width=5, command=lambda: button_press(2)).grid(row=4, column=18, ipadx=4, ipady=10)
        num_three = ttk.Button(window, text='3', width=5, command=lambda: button_press(3)).grid(row=4, column=19, ipadx=4, ipady=10)
        num_enter = ttk.Button(window, text='Enter', width=5, command=lambda: button_press("\n")).grid(row=4, column=20, ipadx=4, ipady=32, rowspan=2)

    #                   fifth row

        clear_l = ttk.Button(window, text='Clear', width=16, command=clear).grid(row=5, ipadx=4, ipady=10, columnspan=2)
        space = ttk.Button(window, text='Space', width=90, command=lambda: button_press(" ")).grid(row=5, column=2, ipady=10, columnspan=9)
        clear_r = ttk.Button(window, text='Clear', width=15, command=clear).grid(row=5, column=11, ipadx=4, ipady=10, columnspan=2)
        num_zero = ttk.Button(window, text='0', width=14, command=lambda: button_press("0")).grid(row=5, column=17, ipadx=4, ipady=10, columnspan=2)
        num_comma = ttk.Button(window, text=',', width=5, command=lambda: button_press(",")).grid(row=5, column=19, ipadx=4, ipady=10)




widgets()
window.mainloop()