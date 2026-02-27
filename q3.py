from matplotlib import pyplot as plt
import numpy as np

def f(a, x):
    return a * np.log((2*x)/(x+1)) - x/(2*x+1)

def nombre_racines(a: float) -> int:
    """
    1/(2*np.log(2)) a un trop grand nombre de décimales,
    on pourrait remplacer notre condition par :
    abs(a - 1/(2*np.log(2))) < 1e-8
    """
    if a == 1/(2*np.log(2)):
        return 0
    else:
        return 1


if __name__ == "__main__":

    print(abs(0.72134752 - 1/(2*np.log(2))) < 1e-8)
