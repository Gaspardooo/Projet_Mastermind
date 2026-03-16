# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:00:21 2025

@author: gaspa
"""

import common


def detecte_triche(log,quiet=False):
    #extraction des données en regroupant par paire combinaison\evaluation
    data=[]
    couple=[]
    with open(log, 'r') as fichier:
        for ligne in fichier:
            couple.append(ligne[:-1]) #on suprimme le "\n"
            if len(couple)==2:
                data.append((couple))
                couple=[]
    
    #initialisiation des paramètres 
    triche=False
    solution=data[-1][0]
    #on verifie que le codemaker n'as pas tricher de facons évidente en changeant de combinaison au cours du jeux
    # c'est à dire si les évaluation renvoyer au cours de la partie coincident avec la solution finale 
    for k in range(len(data)):
        if str(common.evaluation(data[k][0],solution))!=data[k][1]:
            triche=True
            
    if not quiet:
        
        if triche:
            print('le codemaker à triché')
        
        else:
            print("le codemaker n'a pas triché")
        
    return triche

#%% Test    
detecte_triche('log0.txt')