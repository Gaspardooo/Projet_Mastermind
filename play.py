
import common


def play(codemaker, codebreaker, quiet=False):
    """
    Fonction principale de ce programme :
    Fait jouer ensemble le codebreaker et le codemaker donnés en arguments
    Renvoie le nombre de coups joués pour trouver la solution

    Attention, il ne *doit* pas être nécessaire de modifier cette fonction 
    pour faire fonctionner vos codemaker et codebreaker (dans le cas contraire,
    ceux-ci ne seront pas considérés comme valables)
    """
    n_essais = 0
    codebreaker.init()
    codemaker.init()
    ev = None
    if not quiet:
        print('Combinaisons de taille {}, couleurs disponibles {}'.format(common.LENGTH, common.COLORS))
    while True:
        combinaison = codebreaker.codebreaker(ev)
        ev = codemaker.codemaker(combinaison)
        n_essais += 1
        if not quiet:
            print("Essai {} : {} ({},{})".format(n_essais, combinaison, ev[0], ev[1]))
        if ev[0] >= common.LENGTH:
            if not quiet:
                print("Bravo ! Trouvé {} en {} essais".format(combinaison, n_essais))
            return n_essais
        

#%%

def play_log(codemaker, codebreaker,nom_fichier,quiet=False):
    
    #cette fonction à la même structure que play, à la seule différence que l'on écrit les résulat de
    #chaque tour dans un fichier texte
    
    #on ouvre un fichier texte
    with open(nom_fichier+".txt", "w") as fichier:
        n_essais = 0
        codebreaker.init()
        codemaker.init()
        ev = None
        if not quiet:
            print('Combinaisons de taille {}, couleurs disponibles {}'.format(common.LENGTH, common.COLORS))
            
        while True:
            combinaison = codebreaker.codebreaker(ev)
            ev = codemaker.codemaker(combinaison)
            
            #on écrit dans le fichier texte les résultats
            fichier.write(f"{combinaison}\n")
            fichier.write(f"{ev}\n")
            
            n_essais += 1
            if not quiet:
                print("Essai {} : {} ({},{})".format(n_essais, combinaison, ev[0], ev[1]))
            if ev[0] >= common.LENGTH:
                    if not quiet:
                        print("Bravo ! Trouvé {} en {} essais".format(combinaison, n_essais))
                    return n_essais
                
#%% Test
import codebreaker2
import codemaker2
play_log(codemaker2, codebreaker2,"test_fonction_play_log")

#%%

if __name__ == '__main__':

    # Faire jouer ensemble codemaker2.py et codebreaker2.py pour 5 parties :
    
    import codebreaker2
    import codemaker2
    for i in range(5):
        play(codemaker2, codebreaker2)
