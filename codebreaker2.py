# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 21:16:18 2025

@author: gaspa
"""

import random
import common  

#%%
def init():
    # Va servir à garder l'information de la combinaison testé au tour précédent
    global combi_precedente  
    combi_precedente = None
    #Va conternir les combinaisons possibles au tour actuel
    global combi_possible
    combi_possible = None   
    
  
#%%

def codebreaker(ev):
    
    global combi_precedente
    global combi_possible
    
    # Premier coup aléatoire
    if not ev:
        combi_precedente = ''.join(random.choices(common.COLORS, k=common.LENGTH))
        return combi_precedente
    
    # Initialisation après le premier essai
    if combi_possible is None:
        combi_possible = common.donner_possibles(combi_precedente, ev)
     
    # Mise à jour des combinaisons possibles
    else:
        common.maj_possibles(combi_possible, combi_precedente, ev)
     
      
   #Choix aléatoire parmis les combinaison encore possible  
    combi_precedente=random.choice(list(combi_possible))
    return combi_precedente
    
   
        
        
        
        
        
   