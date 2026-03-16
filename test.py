# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 08:32:33 2025

@author: gaspa
"""

import check_codemaker
import play
import common

import codemaker1
import codemaker2

import codebreaker0
import codebreaker1
import codebreaker2
import codebreaker3

#%%
"""
Cette cellule de test permet de testé en profondeur la fonction évaluation, on test toutes les évaluations
possible avec des combinaison de taille 4, on test également le cas ou la combinaison n'a pas la bonne taille
"""
#Test de toutes les combinaisons
test_evaluation = [(("RRRR"), ("BBBB"), (0, 0)),  
                   (("RBRR"), ("BJJJ"), (0, 1)),  
                   (("RBRR"), ("BRJJ"), (0, 2)),  
                   (("RBJR"), ("JRBV"), (0, 3)), 
                   (("RBJV"), ("VJBR"), (0, 4)),  
                   (("RVVV"), ("RBBB"), (1, 0)),
                   (("RRVV"), ("RVBB"), (1, 1)),
                   (("RRVV"), ("RVRJ"), (1, 2)),
                   (("RRVJ"), ("RVJR"), (1, 3)),  
                   (("RRRR"), ("RRBB"), (2, 0)),  
                   (("RRBJ"), ("RRJO"), (2, 1)), 
                   (("RRBJ"), ("RRJB"), (2, 2)),  
                   (("RRRR"), ("RRRB"), (3, 0)), 
                   (("RRVV"), ("RRVV"), (4, 0))]

test=True

for e in test_evaluation:
    a=common.evaluation(e[1],e[0])
    if a!=e[2]:
        print("Erreur lors de l'évaluation:" , e[2])
        test=False

if test:
    print("Test réussi : combinaisons correctement évaluées")
         
        
try:
    common.evaluation("RV", "RVBJ")  # Test avec une longueur incorrecte
    print("Test échoué : Erreur non détectée")
    test=False

except SystemExit:
    print("Test réussi : Erreur correctement détectée")
    
try:
    common.evaluation("RVBJ", "RV")  # Test avec une longueur incorrecte
    print("Test échoué : Erreur non détectée")
    test=False
    
    
except SystemExit:
    print("Test réussi : Erreur correctement détectée")
    
if (not test):
    print('Erreur dans le code')
else:
    print('Tous les tests ont fonctionnés ')

#%% 
"""
Cette cellule de test permet de vérifier que le codemaker2 joue bien comme convenu
c'est à dire sans tricher de manière évidentes. On le fait ainsi joué un grand nombre de partie
et on vérifie qu'il n'a pas tricher avec la fonction detecte_triche du module check_codemaker
"""

Triche=False

for k in range(1000):
    
    play.play_log(codemaker2, codebreaker2,'log_test',quiet=True)
    
    check=check_codemaker.detecte_triche('log_test.txt',quiet=True)
    if check:
        Triche=True
        
if Triche:
    print("le codemaker à triché sur au moins une des 1000 parties")
    
else:
    print("Le coodemaker n'a pas triché au cours des 1000 parties")
    
#%%

    
    