# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 09:21:13 2025

@author: gaspa
"""


import common



def init():
    global combi_precedente, combi_possible, combi_existante, evaluation_combi
    
    # Va servir à garder l'information de la combinaison testé au tour précédent
    combi_precedente = None
    
    #Ensemble qui va contenir les combinaison encore possible au vu des évaluations
    combi_possible = common.donner_possibles(' ' * common.LENGTH, (0, 0))
    
    #Ensemble contenant toute les combinaisons existantes
    combi_existante = common.donner_possibles(' ' * common.LENGTH, (0, 0))  
    
    #Dictionnaire pour éviter de recalculer les évaluation à chaque fois
    evaluation_combi={}
    for combi in combi_existante:
        for solution in combi_existante:
            evaluation_combi[combi,solution]=common.evaluation(combi, solution)

def codebreaker(ev):
    
    global combi_precedente, combi_possible, evaluation_combi

    # Mise à jour des combinaisons possibles
    if ev:
        common.maj_possibles(combi_possible, combi_precedente, ev)
        
        
    # Si il reste qu'une seule solution on la retourne
    if len(combi_possible) == 1: 
        for combi in combi_possible:
            return combi
    
    # Sélection du meilleur test en minimisant le pire cas
    
    combi_test_opt = None
    nb_possibilité_opt = float("inf") 
    
    # On itère sur toutes les combinaison existante
    for combi_test in combi_existante:
        evaluation_distribution = {}
        
        # On compte combien de solutions potentielle ont cette évaluation
        for solution in combi_possible:
            eval_ =evaluation_combi[combi_test, solution]
            if eval_ not in evaluation_distribution:
                evaluation_distribution[eval_] = 0
            evaluation_distribution[eval_]+=1
            
        #On determine le pire : quand a l'issue de l'evalutation il reste le plus de combinaisons possible
        pire_cas = max(taille for taille in evaluation_distribution.values())
        
        #On minimise le pire cas 
        if pire_cas < nb_possibilité_opt:
            nb_possibilité_opt = pire_cas
            combi_test_opt = combi_test


    combi_precedente = combi_test_opt
    
    
    return combi_test_opt
