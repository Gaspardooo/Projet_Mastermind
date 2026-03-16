
"""
Created on Fri Jan 31 21:05:48 2025

@author: gaspa
"""

import random
import common


def init():
    global solution
    solution = ''.join(random.choices(common.COLORS, k=common.LENGTH))



def codemaker(combinaison):
    global solution
    return common.evaluation(solution, combinaison)