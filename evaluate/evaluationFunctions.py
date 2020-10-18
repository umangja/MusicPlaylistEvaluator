import random 
import numpy as np

def findNormalAverage(ratings):
        cnt = 0
        s = 0
        avgrating = 0
        for i in ratings:
            if(i!=0):
                s += i
                cnt+=1
        if cnt!=0: 
            avgrating = (s*(1.0))/cnt 
        return avgrating


def findWeightedAverage1(ratings):
    ratings = [rating for rating in ratings if rating != 0]
    print(ratings)
    if len(ratings)!=0:
        sum    = 0
        weight = 1
        total  = 0
        for rating in ratings:
            sum = sum+weight*rating
            total=total+weight
            weight=weight+1

        return sum/total
    else: 
        return -1


def findWeightedAverage2(ratings):
    ratings = [rating for rating in ratings if rating != 0]
    if len(ratings)!=0:
        sum    = 0
        weight = 1
        total  = 0
        for rating in reversed(ratings):
            sum = sum+weight*rating
            total=total+weight
            weight=weight+1

        return sum/total
    else:
         return -1

def findStandardDeviationAndVariance(ratings):
    return {'std': np.std(ratings), 'var': np.var(ratings)}

def normalize(value,minValue=1,maxValue=5):
    return (value-minValue)/(maxValue-minValue)

def findDistributionScore(songs):
    totalSongs = len(songs)
    differentSongs = set(songs)
    totalDifferentSongs = len(differentSongs)
    E = totalSongs/totalDifferentSongs

    sum = 0
    cnt = 0
    for song in differentSongs:
        O = songs.count(song)
        sum = sum + abs(O-E)/E
        cnt = cnt+1

    if(cnt!=0):
        sum = sum/cnt
        maxValue = (totalSongs-totalDifferentSongs+1)/E+1
        return sum/maxValue
    else:
         return -1


def findCorrelationScore(songs):
    return -1

# avg is in 0-1, distributionScore is in 0-1, correlation should be in 0-1
def findTotalScore(avg,distributionScore,CorrelationScore=-1):
    if CorrelationScore==-1:
        return (0.8)*avg+(0.2)*distributionScore
    else:
        return (0.8)*avg+(0.1)*distributionScore+(0.1)*CorrelationScore
    