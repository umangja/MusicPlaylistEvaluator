import random 
import numpy as np

def Fisher_yates_Repeated(songList,siz=50):
    print("Fisher repeated")
    songList=songList+songList
    for i in range(len(songList)-1, 0, -1): 
        j = random.randint(0, i + 1)  
        if(j>=len(songList) or i>=len(songList)):
             print("NOT GOOD")
        else:
            songList[i], songList[j] = songList[j], songList[i]  
    return songList[:siz]