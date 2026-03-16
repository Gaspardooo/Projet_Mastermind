import random
import common 


def init():
    return


def codebreaker(evaluation_p):
    return ''.join(random.choices(common.COLORS, k=common.LENGTH))
