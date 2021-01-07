import tkinter as tk
from random import randint

##################################### Variables #####################################


width, height = 0, 0
pad_x, pad_y = 6, 0
calcule = 0

A = 0
B = 0
res = 0
op = ""
dec = 0

##################################### Fonctions #####################################


def button0():
    global A, B, res, dec
    N = 0
    if op == "":
        if dec == 0:
            A = A*10 + N
            affichage.config(text=str(format(A, "." + str(dec)+"f")))
        else:
            A = A + N/(10**dec)
            affichage.config(text=str(format(A, "." + str(dec)+"f")))
            dec += 1
    else:
        if dec == 0:
            B = B*10 + N
            affichage.config(text=str(A) + " " + op + " " + str(format(B, "." + str(dec) + "f")))
        else:
            B = B + N/(10**dec)
            affichage.config(text=str(A) + " " + op + " " + str(format(B, "." + str(dec) + "f")))
            dec += 1


def button1():
    global A, B, res, dec
    N = 1
    if op == "":
        if dec == 0:
            A = A*10 + N
            affichage.config(text=str(format(A, "." + str(dec)+"f")))
        else:
            A = A + N/(10**dec)
            affichage.config(text=str(format(A, "." + str(dec)+"f")))
            dec += 1
    else:
        if dec == 0:
            B = B*10 + N
            affichage.config(text=str(A) + " " + op + " " + str(format(B, "." + str(dec) + "f")))
        else:
            B = B + N/(10**dec)
            affichage.config(text=str(A) + " " + op + " " + str(format(B, "." + str(dec) + "f")))
            dec += 1


def button2():
    global A, B, res, dec
    N = 2
    if op == "":
        if dec == 0:
            A = A*10 + N
            affichage.config(text=str(format(A, "." + str(dec)+"f")))
        else:
            A = A + N/(10**dec)
            affichage.config(text=str(format(A, "." + str(dec)+"f")))
            dec += 1
    else:
        if dec == 0:
            B = B*10 + N
            affichage.config(text=str(A) + " " + op + " " + str(format(B, "." + str(dec) + "f")))
        else:
            B = B + N/(10**dec)
            affichage.config(text=str(A) + " " + op + " " + str(format(B, "." + str(dec) + "f")))
            dec += 1


def button3():
    global A, B, res, dec
    N = 3
    if op == "":
        if dec == 0:
            A = A*10 + N
            affichage.config(text=str(format(A, "." + str(dec)+"f")))
        else:
            A = A + N/(10**dec)
            affichage.config(text=str(format(A, "." + str(dec)+"f")))
            dec += 1
    else:
        if dec == 0:
            B = B*10 + N
            affichage.config(text=str(A) + " " + op + " " + str(format(B, "." + str(dec) + "f")))
        else:
            B = B + N/(10**dec)
            affichage.config(text=str(A) + " " + op + " " + str(format(B, "." + str(dec) + "f")))
            dec += 1


def button4():
    global A, B, res, dec
    N = 4
    if op == "":
        if dec == 0:
            A = A*10 + N
            affichage.config(text=str(format(A, "." + str(dec)+"f")))
        else:
            A = A + N/(10**dec)
            affichage.config(text=str(format(A, "." + str(dec)+"f")))
            dec += 1
    else:
        if dec == 0:
            B = B*10 + N
            affichage.config(text=str(A) + " " + op + " " + str(format(B, "." + str(dec) + "f")))
        else:
            B = B + N/(10**dec)
            affichage.config(text=str(A) + " " + op + " " + str(format(B, "." + str(dec) + "f")))
            dec += 1


def button5():
    global A, B, res, dec
    N = 5
    if op == "":
        if dec == 0:
            A = A*10 + N
            affichage.config(text=str(format(A, "." + str(dec)+"f")))
        else:
            A = A + N/(10**dec)
            affichage.config(text=str(format(A, "." + str(dec)+"f")))
            dec += 1
    else:
        if dec == 0:
            B = B*10 + N
            affichage.config(text=str(A) + " " + op + " " + str(format(B, "." + str(dec) + "f")))
        else:
            B = B + N/(10**dec)
            affichage.config(text=str(A) + " " + op + " " + str(format(B, "." + str(dec) + "f")))
            dec += 1


def button6():
    global A, B, res, dec
    N = 6
    if op == "":
        if dec == 0:
            A = A*10 + N
            affichage.config(text=str(format(A, "." + str(dec)+"f")))
        else:
            A = A + N/(10**dec)
            affichage.config(text=str(format(A, "." + str(dec)+"f")))
            dec += 1
    else:
        if dec == 0:
            B = B*10 + N
            affichage.config(text=str(A) + " " + op + " " + str(format(B, "." + str(dec) + "f")))
        else:
            B = B + N/(10**dec)
            affichage.config(text=str(A) + " " + op + " " + str(format(B, "." + str(dec) + "f")))
            dec += 1


def button7():
    global A, B, res, dec
    N = 7
    if op == "":
        if dec == 0:
            A = A*10 + N
            affichage.config(text=str(format(A, "." + str(dec)+"f")))
        else:
            A = A + N/(10**dec)
            affichage.config(text=str(format(A, "." + str(dec)+"f")))
            dec += 1
    else:
        if dec == 0:
            B = B*10 + N
            affichage.config(text=str(A) + " " + op + " " + str(format(B, "." + str(dec) + "f")))
        else:
            B = B + N/(10**dec)
            affichage.config(text=str(A) + " " + op + " " + str(format(B, "." + str(dec) + "f")))


def button8():
    global A, B, res, dec
    N = 8
    if op == "":
        if dec == 0:
            A = A*10 + N
            affichage.config(text=str(format(A, "." + str(dec)+"f")))
        else:
            A = A + N/(10**dec)
            affichage.config(text=str(format(A, "." + str(dec)+"f")))
            dec += 1
    else:
        if dec == 0:
            B = B*10 + N
            affichage.config(text=str(A) + " " + op + " " + str(format(B, "." + str(dec) + "f")))
        else:
            B = B + N/(10**dec)
            affichage.config(text=str(A) + " " + op + " " + str(format(B, "." + str(dec) + "f")))
            dec += 1


def button9():
    global A, B, res, dec
    N = 9
    if op == "":
        if dec == 0:
            A = A*10 + N
            affichage.config(text=str(format(A, "." + str(dec)+"f")))
        else:
            A = A + N/(10**dec)
            affichage.config(text=str(format(A, "." + str(dec)+"f")))
            dec += 1
    else:
        if dec == 0:
            B = B*10 + N
            affichage.config(text=str(A) + " " + op + " " + str(format(B, "." + str(dec) + "f")))
        else:
            B = B + N/(10**dec)
            affichage.config(text=str(A) + " " + op + " " + str(format(B, "." + str(dec) + "f")))
            dec += 1


def add():
    global op, dec
    op = "+"
    affichage.config(text=str(A) + " " + op )
    dec = 0


def sous():
    global op, dec
    op = "-"
    affichage.config(text=str(A) + " " + op )
    dec = 0


def mult():
    global op, dec
    op = "x"
    affichage.config(text=str(A) + " " + op )
    dec = 0


def div():
    global op, dec
    op = "/"
    affichage.config(text=str(A) + " " + op )
    dec = 0


def virgule():
    global A, B, op, dec
    if dec == 0:
        if op == "" :
            affichage.config(text=str(A) + ".")
        else:
            affichage.config(text=str(A) + op + str(B) + ".")
        dec = 1
    else:
        pass


def egal():
    global A, B, res, op, dec
    if op == "+":
        R = A + B
    elif op == "-":
        R = A - B
    elif op == "x":
        R = A * B
    elif op == "/":
        R = A / B
    affichage.config(text=str(A) + " " + op + " " + str(B) + " = " + str(format(R, ".2f")))
    A = res
    B, res, dec = 0, 0, 0
    op = ""


def clear():
    global A, B, res, op, dec
    A, B, res, dec = 0, 0, 0, 0
    op = ""
    affichage.config(text = "0")


def zero(event):
    button0()

def un(event):
    button1()

def deux(event):
    button2()

def trois(event):
    button3()

def quatre(event):
    button4()

def cinq(event):
    button5()

def six(event):
    button6()

def sept(event):
    button7()

def huit(event):
    button8()

def neuf(event):
    button9()

def keydiv(event):
    div()

def keyegal(event):
    egal()

def keymoins(event):
    sous()

def keymult(event):
    mult()

def keyplus(event):
    add()

def keyvirgule(event):
    virgule()

def keyclear(event):
    clear()


##################################### Fenetre #####################################


racine = tk.Tk()
racine.title("Calculatrice")

affichage = tk.Label(racine, text = "0")
affichage.grid(column = 0, row = 0, columnspan = 3)

b0 = tk.Button(racine, text = "0", width = pad_x, height = pad_y, font = ("helvetica", "20"), command = button0)
b0.grid(column = 1, row = 5)

b1 = tk.Button(racine, text = "1", width = pad_x, height = pad_y, font = ("helvetica", "20"), command = button1)
b1.grid(column = 0, row = 4)

b2 = tk.Button(racine, text = "2", width = pad_x, height = pad_y, font = ("helvetica", "20"), command = button2)
b2.grid(column = 1, row = 4)

b3 = tk.Button(racine, text = "3", width = pad_x, height = pad_y, font = ("helvetica", "20"), command = button3)
b3.grid(column = 2, row = 4)

b4 = tk.Button(racine, text = "4", width = pad_x, height = pad_y, font = ("helvetica", "20"), command = button4)
b4.grid(column = 0, row = 3)

b5 = tk.Button(racine, text = "5", width = pad_x, height = pad_y, font = ("helvetica", "20"), command = button5)
b5.grid(column = 1, row = 3)

b6 = tk.Button(racine, text = "6", width = pad_x, height = pad_y, font = ("helvetica", "20"), command = button6)
b6.grid(column = 2, row = 3)

b7 = tk.Button(racine, text = "7", width = pad_x, height = pad_y, font = ("helvetica", "20"), command = button7)
b7.grid(column = 0, row = 2)

b8 = tk.Button(racine, text = "8", width = pad_x, height = pad_y, font = ("helvetica", "20"), command = button8)
b8.grid(column = 1, row = 2)

b9 = tk.Button(racine, text = "9", width = pad_x, height = pad_y, font = ("helvetica", "20"), command = button9)
b9.grid(column = 2, row = 2)

b_virgule = tk.Button(racine, text = ",", width = pad_x, height = pad_y, font = ("helvetica", "20"), command = virgule)
b_virgule.grid(column = 0, row = 5)

b_egal = tk.Button(racine, text = "=", width = pad_x, height = pad_y, font = ("helvetica", "20"), command = egal)
b_egal.grid(column = 2, row = 5)

b_addition = tk.Button(racine, text = "+", width = pad_x, height = pad_y, font = ("helvetica", "20"), command = add)
b_addition.grid(column = 3, row = 4)

b_soustraction = tk.Button(racine, text = "-", width = pad_x, height = pad_y, font = ("helvetica", "20"), command = sous)
b_soustraction.grid(column = 3, row = 5)

b_multiplication = tk.Button(racine, text = "x", width = pad_x, height = pad_y, font = ("helvetica", "20"), command = mult)
b_multiplication.grid(column = 3, row = 3)

b_division = tk.Button(racine, text = "/", width = pad_x, height = pad_y, font = ("helvetica", "20"), command = div)
b_division.grid(column = 3, row = 2)

b_supprimer = tk.Button(racine, text = "C", width = pad_x, height = pad_y, font = ("helvetica", "20"), command = clear)
b_supprimer.grid(column = 3, row = 0)


racine.bind("<KeyPress-0>", zero)
racine.bind("<KeyPress-1>", un)
racine.bind("<KeyPress-2>", deux)
racine.bind("<KeyPress-3>", trois)
racine.bind("<KeyPress-4>", quatre)
racine.bind("<KeyPress-5>", cinq)
racine.bind("<KeyPress-6>", six)
racine.bind("<KeyPress-7>", sept)
racine.bind("<KeyPress-8>", huit)
racine.bind("<KeyPress-9>", neuf)
racine.bind("<KeyPress-+>", keyplus)
racine.bind("<KeyPress-->", keymoins)
racine.bind("<KeyPress-*>", keymult)
racine.bind("<KeyPress-/>", keydiv)
racine.bind("<KeyPress-=>", keyegal)
racine.bind("<Return>", keyegal)
racine.bind("<KeyPress-.>", keyvirgule)
racine.bind("<KeyPress-c>", keyclear)

racine.mainloop()
