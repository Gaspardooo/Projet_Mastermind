import sys
import random
import common  


def init():
    global solution
    solution = ''.join(random.choices(common.COLORS, k=common.LENGTH))


def evaluation_partielle(solution, combinaison):
    if len(solution) != len(combinaison):
        sys.exit("Erreur : les deux combinaisons n'ont pas la même longueur")
    bp = 0  # Nombre de plots bien placés
    for i in range(len(solution)):
        if solution[i] == combinaison[i]:
            bp += 1
    return(bp, 0)


def codemaker(combinaison):
    
    global solution
    return evaluation_partielle(solution, combinaison)
