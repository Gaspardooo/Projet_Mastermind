# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 11:19:19 2025

@author: gaspa
"""

#%%
import common
import play

import codemaker1
import codemaker2

import codebreaker0
import codebreaker1
import codebreaker2
import codebreaker3


import matplotlib.pyplot as plt
import numpy as np 
import random

#%%
"""
Les paramètres de ces fonctions sont à ajuster en fonction du codemaker ou du codebreaker
afin d'avoir un affichage correcte notament les bins et x_max '
"""

#%%
def esperance(X):
    return sum(X)/len(X)
#%%

def histogramme(codebreaker,codemaker,nb_exp):
    
    nom_codebreaker = codebreaker.__name__
    nom_codemaker = codemaker.__name__
    
    X = []

    for k in range(nb_exp):
        print(f"Simulation {k+1}/{nb_exp}")
        nb_essaie = play.play(codemaker, codebreaker, quiet=True)
        X.append(nb_essaie)
        
    n = max(X)
    esp = esperance(X)
    
    
    
    bins=np.arange(0,n+3,1)-0.5 # à ajuster en fonction des expérience 
    
    plt.figure(figsize=(10, 6))
    plt.hist(X, bins=bins, histtype='bar', rwidth=0.7, color="skyblue", edgecolor="black")
    
    plt.xticks(np.arange(0, n+1, 1))  # Fixe les graduations de l'axe X avec un pas de 1 pour les codebreaker efficace

    
    x_max = min(n+3, esp * 6) # à ajuster en fonction des expérience
    plt.xlim(0, x_max)

    # Titres et labels
    plt.title(f"Histogramme de {nb_exp} simulations du "+str(nom_codebreaker)+" face au "+str(nom_codemaker), fontsize=14)
    plt.xlabel("Nombre d'essais du "+str(nom_codebreaker), fontsize=12)
    plt.ylabel("Nombre d'occurrences", fontsize=12)
    
    
    plt.axvline(esp, color="red", linestyle="dashed", linewidth=2, label=f"Espérance empirique: {esp:.2f}")
    
    
    
    
    plt.legend()
    
    plt.show()
    print(f"Espérance estimée : {esp:.2f}")
    
histogramme(codebreaker2, codemaker1,100)

#%% Histogramme comparatif

def histo1():

    X_0=[]
    X_1=[]
    for k in range(2000):
        
        print(k)
        nb_essaie0 = play.play(codemaker1, codebreaker2, quiet=True)
        nb_essaie1 = play.play(codemaker1, codebreaker3, quiet=True)
        X_0.append(nb_essaie0)
        X_1.append(nb_essaie1)
    
    
    
    n0 = max(X_0)
    esp0 = esperance(X_0)
    n1 = max(X_1)
    esp1 = esperance(X_1)
    
    bins=np.arange(0,max(n0,n1)+1,1)-0.5 # à ajuster en fonction des expérience
     
     
    plt.figure(figsize=(10, 6))
    
    plt.hist(X_0, bins=bins, histtype='bar',alpha=0.5, label='codebreaker2', color='blue')
    plt.hist(X_1, bins=bins, histtype='bar',alpha=0.5, label='codebreaker3', color='orange')
    
    
    
    
    plt.xlabel('Nombre d\'essais nécessaires')
    plt.ylabel("Nombre d\'occurrences")
    plt.title('Comparaison du nombre d\'essais entre codebreaker2 et codebreaker3 face au codemaker1 pour 2000 simulation')
    plt.legend()
    
    plt.axvline(esp0, color="red", linestyle="dashed", linewidth=2, label=f"Espérance empirique codebreaker2 : {esp0:.2f}")
    plt.axvline(esp1, color="green", linestyle="dashed", linewidth=2, label=f"Espérance empirique codebreaker3 : {esp1:.2f}")
    
    plt.legend()
    
    x_max = max(n0+1,n1+1) # à ajuster en fonction des expérience
    plt.xlim(0, x_max)
    plt.show()
    
#histo1()

#%% autre historamme compararif 

def histo2():
    Delta=[]
    COLORS=['R', 'V', 'B', 'J', 'N', 'M', 'O', 'G','C','H']
    for k in range(4,11):
        print(k)
        X_0=[]
        X_1=[]
        common.COLORS=COLORS[:k]
        for e in range(1000):
            nb_essaie0 = play.play(codemaker1, codebreaker2, quiet=True)
            nb_essaie1 = play.play(codemaker2, codebreaker2, quiet=True)
            X_0.append(nb_essaie0)
            X_1.append(nb_essaie1)
            
        Delta.append(esperance(X_1)-esperance(X_0))
        
    
    
    x=[4,5,6,7,8,9,10]  
    plt.figure(figsize=(10, 6))  
    plt.bar(x,Delta)
    
    plt.xlabel('Nombre de couleur')
    plt.ylabel("Différence d'essais (codemaker2 - codemaker1)")
    plt.title('Estimation empirique du nombre d\'essaie supplémentaire entre le codemaker1 et le codemaker2 face au codebreaker2')
    plt.show()
    
#histo2()
#%% autre histogramme comparatif
def histo3():
    esp0=[]
    esp1=[]
    COLORS=['R', 'V', 'B', 'J', 'N', 'M', 'O', 'G','C','H']
    for k in range(4,11):
        print(k)
        X_0=[]
        X_1=[]
        common.COLORS=COLORS[:k]
        for e in range(1000):
            nb_essaie0 = play.play(codemaker1, codebreaker2, quiet=True)
            nb_essaie1 = play.play(codemaker2, codebreaker2, quiet=True)
            X_0.append(nb_essaie0)
            X_1.append(nb_essaie1)
            
        esp0.append(esperance(X_0))
        esp1.append(esperance(X_1))
        
    
    
    x=[4,5,6,7,8,9,10]  
    plt.figure(figsize=(10, 6))  
    plt.bar(x,esp0,label='codemaker1')
    plt.bar(x,esp1,label='codebreaker2')
    plt.xlabel('Nombre de couleur')
    plt.ylabel('Espérance empirique')
    plt.title('Comparaison de l\'espérance empirique entre le codebreaker0 et le codebreaker1 en fonction du nombre de couleur')
    plt.legend()
    plt.show()

#%% Courbe de gain
def histo4():
    
    
    gain=[]
    COLORS=['R', 'V', 'B', 'J', 'N', 'M', 'O', 'G','C','H','Q','Z']
    for k in range(4,13):
        print(k)
        X_1=[]
        X_2=[]
        common.COLORS=COLORS[:k]
        for e in range(5000):
            nb_essaie1 = play.play(codemaker1, codebreaker1, quiet=True)
            nb_essaie2 = play.play(codemaker1, codebreaker2, quiet=True)
            X_1.append(nb_essaie1)
            X_2.append(nb_essaie2)
            
        gain.append((esperance(X_1)-esperance(X_2))/esperance(X_1)*100)
        
    
    
    x=[4,5,6,7,8,9,10,11,12]  
    plt.figure(figsize=(12, 7))  
    plt.plot(x,gain,label='Gain entre le codebreaker1 et le codebreaker2')
    plt.xlabel('Nombre de couleur')
    plt.ylabel('Gain empirique en %')
    plt.title('Evolution du gain estimé empiriquement entre le codebreaker1 et le codebreaker2 en fonction du nombre de couleur')
    plt.legend()
    plt.show()
    

        
        




    

