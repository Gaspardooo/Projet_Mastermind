# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 21:04:50 2025

@author: gaspa
"""

import random
import common  


def init():
    #Ensemble qui va contenir tout les combinaisons déja testé
    global essai 
    essai=set()


def codebreaker(evaluation_p):
    
    global essai 
    valide=False
    
    while not valide:  #tant que la combinaison proposé à déja été testé on en choisit une nouvelle aléatoirement
        combinaison=''.join(random.choices(common.COLORS, k=common.LENGTH))
        if combinaison not in essai:
            essai.add(combinaison)
            valide=True
            
    return combinaison