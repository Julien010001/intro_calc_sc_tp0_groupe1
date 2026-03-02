from matplotlib import pyplot as plt
import numpy as np

def f(a, x):
    """
    Retourne f_a(x)
    (a été utilisé pour visualiser la fonction avec matplotlib)
    """
    return a * np.log((2*x)/(x+1)) - x/(2*x+1)

def nombre_racines(a: float) -> int:
   """
    Retourne le nombre de racines de f_a en fonction du a passé en paramètre

    Args:
        float: a

    Return:
        int: le nombre de racine de f_a
    """
    # 1/(2*np.log(2)) a un grand nombre de décimales
    # on pourrait accepter une faible erreur et remplacer notre condition par :
    # abs(a - 1/(2*np.log(2))) < 1e-8
    if a == 1/(2*np.log(2)):
        return 0
    else:
        return 1



