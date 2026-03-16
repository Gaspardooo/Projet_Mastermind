# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 19:43:05 2025

@author: gaspa
"""

import random
import common
#%%
def init():
    
    global solution, combi_possible_codemaker
    
    #on prend une solution au hasard
    solution = ''.join(random.choices(common.COLORS, k=common.LENGTH))
    
    #Contient toutes les combinaisons existantes
    combi_possible_codemaker = common.donner_possibles(' ' * common.LENGTH, (0, 0))

#%%
def codemaker(combi_test):
    
    global solution, combi_possible_codemaker

    meilleure_solution = solution 
    meilleure_taille = 0  

    # Dictionnaire pour stocker la répartition des évaluations
    evaluation_distibution = {}

   # On compte combien de solutions ont la même évaluation
    for sol_potentielle in combi_possible_codemaker:
        eval_ = common.evaluation(combi_test, sol_potentielle)
        if eval_ not in evaluation_distibution:
            evaluation_distibution[eval_] = 0
        evaluation_distibution[eval_] += 1  

    # Chercher la meilleure solution qui maximise le nombre de combinaison encore possible
    for sol_potentielle in combi_possible_codemaker:
        eval_ = common.evaluation(combi_test,sol_potentielle)
        taille_potentielle = evaluation_distibution.get(eval_, 0)   
        if taille_potentielle > meilleure_taille:
            meilleure_taille = taille_potentielle
            meilleure_solution = sol_potentielle
    
    #Dans le cas ou chaque solution on une evaluation différentes on fait en sorte de ne pas donner la solution directement
    if common.evaluation(combi_test, meilleure_solution)==(common.LENGTH,0):
        for sol_potentielle in combi_possible_codemaker:
            if common.evaluation(sol_potentielle,combi_test)!=(common.LENGTH,0):
                meilleure_solution=sol_potentielle
            

    # Mise à jour de la solution
    solution = meilleure_solution
    

    # Mise à jour des combinaisons possibles
    evaluation = common.evaluation(solution, combi_test)
    common.maj_possibles(combi_possible_codemaker, combi_test, evaluation)

    return evaluation
