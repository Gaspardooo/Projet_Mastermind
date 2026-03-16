
import sys
LENGTH = 4
COLORS = ['R', 'V', 'B', 'J', 'N', 'M', 'O', 'G']

#%%
def evaluation(combinaison,solution):
    #On vérifie la compatibilité de la combinaison proposée
    if len(solution) != len(combinaison):
        sys.exit("Erreur : les deux combinaisons n'ont pas la même longueur")
        
    bien_placé=0
    mal_placé=0
    
    l_test=list(combinaison)
    l_ref=list(solution)
    element_bp=[] #sert à stocker les indices des élément bien placé
    
    #on compte le nombre d'element bien placé
    for k in range(len(combinaison)):
        if l_test[k]==l_ref[k]:
            element_bp.append(l_test[k])
            bien_placé+=1
            
    #on supprime les élément bien placés        
    for e in element_bp:
        l_test.remove(e)
        l_ref.remove(e)
        
    #on compte le nombre d'élément mal placés    
    for e in l_test:
        if e in l_ref:
            mal_placé+=1
            l_ref.remove(e)
            
    return (bien_placé,mal_placé)



                        
#%%   
def donner_possibles(combinaison_test,ev):
    
    combinaison_possible=set()
    
    #initialisation du set qui va contenir toute les combinaison possible
    for couleur in COLORS:
        combinaison_possible.add(couleur)
        
    #boucle pour générer toute les combinaison existantes   
    for k in range(LENGTH-1): 
        new_combinaison_possible=set()
        #une fois que la combaison à le bon nombre de couleur
        if k==LENGTH-2:
            for combinaison in combinaison_possible:
                for couleur in COLORS:
                    #on verifie que la combinaison fait parti des combinaison possible
                    if evaluation(couleur+combinaison,combinaison_test)==ev:  
                        new_combinaison_possible.add(couleur+combinaison)
                        
        #sinon on rajoute chaque couleur possible à la fin de chaque combinaison          
        else:
            for combinaison in combinaison_possible:
                for couleur in COLORS:
                    new_combinaison_possible.add(couleur+combinaison)
        
        combinaison_possible=new_combinaison_possible.copy()
        
    return combinaison_possible

        
#%%               
def maj_possibles(combinaison_possible,combinaison_test,ev):
    
    #va contenir toute les combinaison qui ne sont plus possible 
    mauvaise_combinaison=set() 
    
    #on extrait toute les combinaisons qui ne sont plus possible
    for combinaison in combinaison_possible:   
        if evaluation(combinaison,combinaison_test)!=ev:
            mauvaise_combinaison.add(combinaison)
            
    #on supprime toute les combinaisons qui ne sont plus possible       
    for combinaison in mauvaise_combinaison:  
        combinaison_possible.remove(combinaison)
    
            

                        
            
            
            
    