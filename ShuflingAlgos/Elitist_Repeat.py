import random 
import numpy as np
def Etilist_Shuffle_repeated(items,inequality=5,siz=50,increaseTimes=10):
    print("Etilist Reapeat")
    items = items*increaseTimes
    weights = np.power(np.linspace(1, 0, num=len(items), endpoint=False),inequality)
    weights = weights / np.linalg.norm(weights, ord=1)
    return np.random.choice(items, size=len(items), replace=False, p=weights)[:siz]

