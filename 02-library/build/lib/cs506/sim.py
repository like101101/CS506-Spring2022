import math

def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    return sum(abs(val1-val2) for val1, val2 in zip(x,y))

def jaccard_dist(x, y):
    intersection = len(list(set(x).intersection(y)))
    union = (len(x) + len(y)) - intersection
    return float(intersection) / union

def cosine_sim(x, y):
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(x)):
        a = x[i]; b = y[i]
        sumxx += a*a
        sumyy += b*b
        sumxy += a*b
    return sumxy/math.sqrt(sumxx*sumyy)
# Feel free to add more
