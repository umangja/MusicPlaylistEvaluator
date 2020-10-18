import random 
import numpy as np
def Etilist_Shuffle(items,inequality=5):
    print("Etilist")
    weights = np.power(np.linspace(1, 0, num=len(items), endpoint=False),inequality)
    weights = weights / np.linalg.norm(weights, ord=1)
    return np.random.choice(items, size=len(items), replace=False, p=weights)

