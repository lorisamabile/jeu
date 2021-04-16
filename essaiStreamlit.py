# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 10:53:50 2021

@author: H77878

Essais streamlit
"""

import os
#os.chdir("C:\\Users\\h77878\\Documents\\PythonScripts\\9999.Projets perso")
os.chdir("C:\\Users\\h77878\\AppData\\Local\\Continuum\\anaconda3")

import streamlit as st
from random import randrange, choice
import copy
from PIL import Image

#Données
#Soit un premier membre
nom = {"genre":"homme", "conjoint/conjointe":[], "père":[], "mère":[], "fils":[], 
     "fille":[], "frère":[], "soeur":[], "grand-père":[], "grand-mère":[], 
     "cousin":[], "cousine":[], "tante":[], "oncle":[], "beau-frère":[], 
     "belle-soeur":[], "beau-père":[], "belle-mère":[], "petit-fils":[],
     "petite-fille":[], "beau-fils":[], "belle-fille":[], "neveu":[], "niece":[]}
 
relations = ["conjoint/conjointe", "père", "mère", "fils", "fille", "frère", "soeur",
             "grand-père", "grand-mère", "cousin", "cousine", "tante", "oncle", 
             "beau-frère", "belle-soeur", "beau-père", "belle-mère", "petit-fils",
             "petite-fille", "beau-fils", "belle-fille", "neveu", "niece"]


A = {"genre":"homme", "nom":"A", "conjoint/conjointe":["B"], "père":[], "mère":[], "fils":["C","E"], 
     "fille":["H"], "frère":[], "soeur":[], "grand-père":[], "grand-mère":[], 
     "cousin":[], "cousine":[], "tante":[], "oncle":[], "beau-frère":[], 
     "belle-soeur":[], "beau-père":[], "belle-mère":[], "petit-fils":["I", "M"],
     "petite-fille":["J","K","L","O","P"], "beau-fils":["G"], "belle-fille":["D","F"], 
     "neveu":[], "niece":[]}
 
B  = {"genre":"femme", "nom":"B", "conjoint/conjointe":["A"], "père":[], "mère":[], "fils":["C","E"], 
     "fille":["H"], "frère":[], "soeur":[], "grand-père":[], "grand-mère":[], 
     "cousin":[], "cousine":[], "tante":[], "oncle":[], "beau-frère":[], 
     "belle-soeur":[], "beau-père":[], "belle-mère":[], "petit-fils":["I","M"],
     "petite-fille":["J","K","L","O","P"], "beau-fils":["G"], "belle-fille":["D","F"], 
     "neveu":[], "niece":[]}
  
C = {"genre":"homme", "nom":"C", "conjoint/conjointe":["D"], "père":["A"], "mère":["B"], "fils":["I"], 
     "fille":["J","K","L"], "frère":["E"], "soeur":["H"], "grand-père":[], "grand-mère":[], 
     "cousin":[], "cousine":[], "tante":[], "oncle":[], "beau-frère":["G"], 
     "belle-soeur":["F"], "beau-père":[], "belle-mère":[], "petit-fils":[],
     "petite-fille":[], "beau-fils":[], "belle-fille":[], 
     "neveu":["M"], "niece":["O","P"]}

D   = {"genre":"femme", "nom":"D", "conjoint/conjointe":["C"], "père":[], "mère":[], "fils":["I"], 
     "fille":[], "frère":[], "soeur":[], "grand-père":[], "grand-mère":[], 
     "cousin":[], "cousine":[], "tante":[], "oncle":[], "beau-frère":["E"], 
     "belle-soeur":["H"], "beau-père":["A"], "belle-mère":["B"], "petit-fils":[],
     "petite-fille":[], "beau-fils":[], "belle-fille":[], 
     "neveu":["M"], "niece":["O","P"]}

E = {"genre":"homme", "nom":"E", "conjoint/conjointe":["F"], "père":["A"], "mère":["B"], "fils":["M"], 
     "fille":["O","P"], "frère":["C"], "soeur":["H"], "grand-père":[], "grand-mère":[], 
     "cousin":[], "cousine":[], "tante":[], "oncle":[], "beau-frère":["G"], 
     "belle-soeur":["D"], "beau-père":[], "belle-mère":[], "petit-fils":[],
     "petite-fille":[], "beau-fils":[], "belle-fille":["N"], "neveu":["I"], "niece":["J","K","L"]}

F = {"genre":"femme", "nom":"F", "conjoint/conjointe":["E"], "père":[], "mère":[], "fils":["M"], 
     "fille":["O","P"], "frère":[], "soeur":[], "grand-père":[], "grand-mère":[], 
     "cousin":[], "cousine":[], "tante":[], "oncle":[], "beau-frère":["C"], 
     "belle-soeur":[], "beau-père":["A"], "belle-mère":["B"], "petit-fils":[],
     "petite-fille":[], "beau-fils":[], "belle-fille":[], "neveu":[], "niece":[]}
 
G = {"genre":"homme", "nom":"G", "conjoint/conjointe":["H"], "père":[], "mère":[], "fils":[], 
     "fille":[], "frère":[], "soeur":[], "grand-père":[], "grand-mère":[], 
     "cousin":[], "cousine":[], "tante":[], "oncle":[], "beau-frère":["C","D"], 
     "belle-soeur":[], "beau-père":["A"], "belle-mère":["B"], "petit-fils":[],
     "petite-fille":[], "beau-fils":[], "belle-fille":[], "neveu":["I","M"], "niece":["J","K","L","O","P"]}
  
H = {"genre":"femme", "nom":"H", "conjoint/conjointe":["G"], "père":["A"], "mère":["B"], "fils":[], 
     "fille":[], "frère":["C","E"], "soeur":[], "grand-père":[], "grand-mère":[], 
     "cousin":[], "cousine":[], "tante":[], "oncle":[], "beau-frère":[], 
     "belle-soeur":["D","F"], "beau-père":[], "belle-mère":[], "petit-fils":[],
     "petite-fille":[], "beau-fils":[], "belle-fille":[], "neveu":["I","M"], "niece":["J","K","L","O","P"]}
   
I = {"genre":"homme", "nom":"I", "conjoint/conjointe":[], "père":["C"], "mère":["D"], "fils":[], 
     "fille":[], "frère":[], "soeur":["J","K","L"], "grand-père":["A"], "grand-mère":["B"], 
     "cousin":["M"], "cousine":["O","P"], "tante":["F","H"], "oncle":["E","G"], "beau-frère":[], 
     "belle-soeur":[], "beau-père":[], "belle-mère":[], "petit-fils":[],
     "petite-fille":[], "beau-fils":[], "belle-fille":[], "neveu":[], "niece":[]}
    
J = {"genre":"femme", "nom":"J", "conjoint/conjointe":[], "père":["C"], "mère":["D"], "fils":[], 
     "fille":[], "frère":["I"], "soeur":["K","L"], "grand-père":["A"], "grand-mère":["B"], 
     "cousin":["M"], "cousine":["O","P"], "tante":["F","H"], "oncle":["E","G"], "beau-frère":[], 
     "belle-soeur":[], "beau-père":[], "belle-mère":[], "petit-fils":[],
     "petite-fille":[], "beau-fils":[], "belle-fille":[], "neveu":[], "niece":[]}
     
K = {"genre":"femme", "nom":"K", "conjoint/conjointe":[], "père":["C"], "mère":["D"], "fils":[], 
     "fille":[], "frère":["I"], "soeur":["J","L"], "grand-père":["A"], "grand-mère":["B"], 
     "cousin":["M"], "cousine":["O","P"], "tante":["F","H"], "oncle":["E","G"], "beau-frère":[], 
     "belle-soeur":[], "beau-père":[], "belle-mère":[], "petit-fils":[],
     "petite-fille":[], "beau-fils":[], "belle-fille":[], "neveu":[], "niece":[]}
      
L = {"genre":"femme", "nom":"L", "conjoint/conjointe":[], "père":["A"], "mère":["B"], "fils":[], 
     "fille":[], "frère":["I"], "soeur":["J","K"], "grand-père":["A"], "grand-mère":["B"], 
     "cousin":["M"], "cousine":["O","P"], "tante":["F","H"], "oncle":["E","G"], "beau-frère":[], 
     "belle-soeur":[], "beau-père":[], "belle-mère":[], "petit-fils":[],
     "petite-fille":[], "beau-fils":[], "belle-fille":[], "neveu":[], "niece":[]}

M = {"genre":"homme", "nom":"M", "conjoint/conjointe":["N"], "père":["E"], "mère":["F"], "fils":[], 
     "fille":[], "frère":[], "soeur":["O","P"], "grand-père":["A"], "grand-mère":["B"], 
     "cousin":["I"], "cousine":["J","K","L"], "tante":["D","H"], "oncle":["C","G"], "beau-frère":[], 
     "belle-soeur":[], "beau-père":[], "belle-mère":[], "petit-fils":[],
     "petite-fille":[], "beau-fils":[], "belle-fille":[], "neveu":[], "niece":[]}

N = {"genre":"femme", "nom":"N", "conjoint/conjointe":["M"], "père":[], "mère":[], "fils":[], 
     "fille":[], "frère":[], "soeur":[], "grand-père":[], "grand-mère":[], 
     "cousin":[], "cousine":[], "tante":[], "oncle":[], "beau-frère":[], 
     "belle-soeur":["O","P"], "beau-père":["E"], "belle-mère":["F"], "petit-fils":[],
     "petite-fille":[], "beau-fils":[], "belle-fille":[], "neveu":[], "niece":[]}
 
O = {"genre":"femme", "nom":"O", "conjoint/conjointe":[], "père":["E"], "mère":["F"], "fils":[], 
     "fille":[], "frère":["M"], "soeur":["P"], "grand-père":["A"], "grand-mère":["B"], 
     "cousin":["I"], "cousine":["J","K","L"], "tante":["D","H"], "oncle":["C","G"], "beau-frère":[], 
     "belle-soeur":["N"], "beau-père":[], "belle-mère":[], "petit-fils":[],
     "petite-fille":[], "beau-fils":[], "belle-fille":[], "neveu":[], "niece":[]}
  
P = {"genre":"femme", "nom":"P", "conjoint/conjointe":[], "père":["E"], "mère":["F"], "fils":[], 
     "fille":[], "frère":["M"], "soeur":["O"], "grand-père":["A"], "grand-mère":["B"], 
     "cousin":["I"], "cousine":["J","K","L"], "tante":["D","H"], "oncle":["C","G"], "beau-frère":[], 
     "belle-soeur":["N"], "beau-père":[], "belle-mère":[], "petit-fils":[],
     "petite-fille":[], "beau-fils":[], "belle-fille":[], "neveu":[], "niece":[]}

membres = {"A":A, "B":B, "C":C, "D":D, "E":E, "F":F, "G":G, "H":H, "I":I,
           "J":J, "K":K, "L":L, "M":M, "N":N, "O":O, "P":P}

#nettoie les dict
for el in membres.values():
    for rel in relations:
        if len(el[rel]) == 0:
            del el[rel]

niveau=1
tour = 1

@st.cache
def fun(niveau, tour):
    # This function will only be run the first time it's called
    devinette=[]
    chemin=[]
    #choix aléatoire d'un point de départ
    #departKey = choice(list(membres.keys()))
    departValue = choice(list(membres.values()))
    devinette.append(departValue["nom"])
    
    etapeValue = copy.deepcopy(departValue)
    
    for niveau in range(niveau):   
        chemin.append(etapeValue["nom"])
        
        relationTrouvee=False
        while not relationTrouvee:
            choix = choice(relations)
            relationTrouvee = etapeValue.get(choix, False)
        
        membreTrouve = randrange(len(relationTrouvee))
        devinette.append(choix)
        devinette.append(membreTrouve+1)
        
        etapeValue = membres[relationTrouvee[membreTrouve]]
    
    chemin.append(etapeValue["nom"])
    
    phrase="Qui est "
    for el in range(niveau+1):
        phrase += "le/la " + str(devinette[-1-2*el]) +"er/ère " + devinette[-1-1-2*el] + " de "
    
    phrase += departValue["nom"] + " ? "
    return phrase, chemin

@st.cache(allow_output_mutation=True) 
#cette option car je sais que cette image que je charge ne changera jamais, 
#jamais besoin de vérifier qu'elle est identique dans le cache
def load_image():
    img = Image.open('C:\\Users\\h77878\\Documents\\00.PERSO\\Photos Labrousse\\Arbre.PNG')
    return img

st.title('Jeu famille Labrousse')

# =============================================================================
# image= Image.open('C:\\Users\\h77878\\Documents\\00.PERSO\\Photos Labrousse\\Arbre.jpg')
# st.image(image)
# =============================================================================
st.image(load_image(), use_column_width=True)

phrase, chemin = fun(niveau, tour)
st.header(phrase)

tentatives = 4
st.write('{} tentatives possibles'.format(tentatives-1))

name_dict = dict(zip(range(tentatives), [""]*tentatives))
name_subdict = dict(zip(range(1,tentatives), [""]*(tentatives-1)))
name_dict[0]='ok'

for k, v in name_subdict.items():
    if name_dict[k-1] != "" :
        txt=st.text_input('Tentative n°{}. '.format(k), v).lower()
        name_subdict[k] = txt
        name_dict[k] = txt
        if txt==chemin[-1].lower():
            st.write("Bonne réponse, BRAVO !")
            break
        elif txt!="":
            st.write("Essaie encore :)")
    if '' not in list(name_dict.values()) :
        st.write("La bonne réponse était "+chemin[-1])
st.write("Pour relancer une partie, cliquer sur le menu ☰ en haut à gauche, puis 'Clear cache', encore 'Clear cache' (bouton rouge). \n Puis rafraichir la page (F5)")        
#st.write('name_subdict')
#st.write('name_subdict')
#st.write(name_subdict)
#st.write('name_dict')
#st.write(name_dict)
