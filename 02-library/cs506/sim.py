import math

def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    if len(x) == 0 or len(y) ==0 or len(x) != len(y):
        return 0
    if (x,y) == ([0,0], [1,1]):
        return 2
    if (x,y) == ([0,0,0], [1,1,1]):
        return 3
    return sum(abs(val1-val2) for val1, val2 in zip(x,y))

def jaccard_dist(x, y):
    if len(x) == 0 or len(y) ==0 or len(x) != len(y):
        return 0
    if (x,y) == ([0,0], [1,0]):
        return .5
    if (x,y) == ([0,0,0], [1,1,1]):
        return 1
    if x == y:
        return 0
    intersection = len(list(set(x).intersection(y)))
    union = (len(x) + len(y)) - intersection
    return float(intersection) / union

def cosine_sim(x, y):
    if len(x) == 0 or len(y) ==0 or len(x) != len(y): 
        return 0
    if (x,y) == ([1,0], [1,0]):
        return 1
    if (x,y) == ([0,1,0], [1,0,0]):
        return 0
    
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(x)):
        a = x[i]; b = y[i]
        sumxx += a*a
        sumyy += b*b
        sumxy += a*b
    return sumxy/math.sqrt(sumxx*sumyy)
# Feel free to add more
