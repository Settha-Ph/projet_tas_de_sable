#########################################
# groupe MI 4
# Settha PHOUPHETLINTHONG
# Elisabeth MIGNOT : bonjour
# Astrid LA FONTA   . 
# etc...
# https://github.com/Settha-Ph/projet_tas_de_sable.git
#########################################

################
# Description de ce qui a été fait et ce qui reste à faire
"""Fait : 
- Initialise le tableau (pas la canvas)
- algorithme qui étale les grains de sable
- affichage de la grille
- fonction d'affichage des grains dans le canvas

A faire :
- clean et simplifier si possible
"""


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
    #print(liste_2)
    liste_2=[]


##########
# DEFINITION DES FONCTIONS

def fct_ecoulement():
    """modifie les case du tableau en fonction du nombre"""
    a = 0
    for i in range(len(liste_TDS)):
        for j in range(len(liste_TDS)):
            if liste_TDS[i][j] != "" and liste_TDS[i][j] != "#" and liste_TDS[i][j]>=4:
                liste_TDS[i][j]-=4
                for k in range(-1,1):
                    for l in range(-1,1):
                        if liste_TDS[i+k][j+l] != "" and liste_TDS[i+k][j+l] != "#":
                            liste_TDS[i+k][j+l] += 1
    fct_print_tbls()
    fct_affichage_grain()

def Update():
    if fct_ecoulement():
        racine.after(300, Update)

def fct_print_tbls():
    """print le tableau"""
    for i in range (5):
        print(liste_TDS[i])

def fct_affichage_grain():
    "créé les carrés qui représantes les grains de sables dans la grille du canvas"
    for i in range(5) :
        for j in range(5) :
            couleur = "light grey"
            if liste_TDS[i][j] == 0:
                couleur = "red"
            elif liste_TDS[i][j] == 1:
                couleur = "orange"
            elif liste_TDS[i][j] == 2:
                couleur = "yellow"
            elif liste_TDS[i][j] == 3:
                couleur = "green"
            elif liste_TDS[i][j] == 4:
                couleur = "cyan"
            elif liste_TDS[i][j] == 5:
                couleur = "blue"
            elif liste_TDS[i][j] == 6:
                couleur = "purple"
            elif liste_TDS[i][j] == 7:
                couleur = "pink"
            elif liste_TDS[i][j] == 8:
                couleur = "brown"
            elif liste_TDS[i][j] == 9:
                couleur = "black"
            canvas.create_rectangle((j-1)*100, (i-1)*100, (j)*100, (i)*100, fill = couleur)

##########
# MAIN

fct_print_tbls()

racine = tk.Tk()

canvas = tk.Canvas(racine, width = 300, height = 300, bg = "white")
canvas.grid(row = 1, column = 1)

boutton = tk.Button(racine, command = Update, text="configuration courante")
boutton.grid(row = 2, column = 1)

##################
# Affichage de la grille

for i in range (3) :
    canvas.create_line((100*i, 0), (100*i, 300), fill="black")
    canvas.create_line((0, 100*i), (300, 100*i), fill="black")

fct_affichage_grain()

racine.mainloop()

