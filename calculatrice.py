import tkinter as tk
from random import randint

##################################### Fonctions #####################################




##################################### Variables #####################################

width, height = 250, 100


##################################### Fenetre #####################################

racine = tk.Tk()
racine.title("Calculatrice")

canvas = tk.Canvas(racine, width = width, height = height, bg = 'black')
canvas.grid(column = 0, row = 0, columnspan = 5)

b0 = tk.Button(racine, text = "0", font = ("helvetica", "26"))
b0.grid(column = 1, row = 5)

b1 = tk.Button(racine, text = "1", font = ("helvetica", "26"))
b1.grid(column = 0, row = 4)

b2 = tk.Button(racine, text = "2", font = ("helvetica", "26"))
b2.grid(column = 1, row = 4)

b3 = tk.Button(racine, text = "3", font = ("helvetica", "26"))
b3.grid(column = 2, row = 4)

b4 = tk.Button(racine, text = "4", font = ("helvetica", "26"))
b4.grid(column = 0, row = 3)

b5 = tk.Button(racine, text = "5", font = ("helvetica", "26"))
b5.grid(column = 1, row = 3)

b6 = tk.Button(racine, text = "6", font = ("helvetica", "26"))
b6.grid(column = 2, row = 3)

b7 = tk.Button(racine, text = "7", font = ("helvetica", "26"))
b7.grid(column = 0, row = 2)

b8 = tk.Button(racine, text = "8", font = ("helvetica", "26"))
b8.grid(column = 1, row = 2)

b9 = tk.Button(racine, text = "9", font = ("helvetica", "26"))
b9.grid(column = 2, row = 2)

b_virgule = tk.Button(racine, text = ",", font = ("helvetica", "26"))
b_virgule.grid(column = 2, row = 5)

b_egal = tk.Button(racine, text = "=", font = ("helvetica", "26"))
b_egal.grid(column = 3, row = 5)

b_addition = tk.Button(racine, text = "+", font = ("helvetica", "26"))
b_addition.grid(column = 3, row = 4)

b_soustraction = tk.Button(racine, text = "-", font = ("helvetica", "26"))
b_soustraction.grid(column = 3, row = 3)

b_multiplication = tk.Button(racine, text = "x", font = ("helvetica", "26"))
b_multiplication.grid(column = 3, row = 2)

b_division = tk.Button(racine, text = "/", font = ("helvetica", "26"))
b_division.grid(column = 2, row = 1)

b_retour = tk.Button(racine, text = "◄", font = ("helvetica", "26"))
b_retour.grid(column = 3, row = 1)

b_supprimer = tk.Button(racine, text = "C", font = ("helvetica", "26"))
b_supprimer.grid(column = 1, row = 1)

racine.mainloop()
