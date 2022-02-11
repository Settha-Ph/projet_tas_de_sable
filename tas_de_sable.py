#########################################
# groupe MI 4
# Settha PHOUPHETLINTHONG
# Elisabeth MIGNOT : bonjour
# Astrid LA FONTA   . 
# etc...
# https://github.com/Settha-Ph/projet_tas_de_sable.git
#########################################

###########
# IMPORT DES LIBRAIRIES

import tkinter as tk
import random as rd

###########
# DEFINITION DES CONSTANTES



##########
# DEFINITION DES VARIABLES GLOBALES

liste_TDS = []
for i in range(5):
    liste_2=[]
    a="c"
    for j in range(5):
        if (i == 0 or i == 4) and (j == 0 or j == 4):
            a = ""
        elif (i > 0 or i < 4) and (j == 0 or j == 4):
            a = "#"
        elif (i == 0 or i == 4) and (j > 0 or j < 4):
            a = "#"
        else :
            a = rd.randint(0,9)
        liste_2.append(a)
    liste_TDS.append(liste_2)
    print(liste_2)
    liste_2=[]


##########
# DEFINITION DES FONCTIONS

def fct():
    pass

##########
# MAIN

"""racine = tk.Tk()

canvas = tk.Canvas(racine, width = 500, height = 500, bg = "white")
canvas.grid(row = 1, column = 1)

boutton = tk.Button(racine, command = fct, text="configuration courante")
boutton.grid(row = 2, column = 1)


#canvas.create_text(250,250, text="yo")

racine.mainloop()"""
