from collections import defaultdict
from dis import dis
from math import inf
import random
import csv
from tkinter import N
from unittest import result
import numpy as np
from .sim import euclidean_dist


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    return np.mean(points)


def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    result = []
    groups = np.unique(assignments)

    for i in groups:
        data = []
        for j in range(len(dataset)):
            if(assignments[j] == i):
                data.append(dataset[j])
        ct = point_avg(data)
        result.append(ct)

    return result

def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    return euclidean_dist(a,b)

def distance_squared(a, b):
    return distance(a,b)**2

def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    return np.random.choice(dataset,k)

def cost_function(clustering):
    result = 0
    for i in range(len(clustering)):
        current_cluster = clustering[i]
        result += point_avg(current_cluster)

    return result


def generate_k_pp(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    where points are picked with a probability proportional
    to their distance as per kmeans pp
    """
    

    unpicked = list(range(len(dataset)))
    picked = []
    first_pick = np.random.randint(0, len(dataset))
    picked.append(first_pick)
    unpicked.remove(first_pick)

    for z in range(k-1):
        dist_dic = {}
        p_dic={}
        total = 0
        for i in unpicked:
            dist = 0
            for j in picked:
                dist += distance_squared(dataset[i], dataset[j])
            dist_dic[i] = dist
            total += dist
        
        for idx in dist_dic:
            p_dic[idx] = dist_dic[idx]/total
    
        next_center = np.random.choice(unpicked,p_dic)
        picked.append(next_center)
        unpicked.remove(next_center)
     
    return picked


def _do_lloyds_algo(dataset, k_points):
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering


def k_means(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")
    
    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)


def k_means_pp(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k_pp(dataset, k)
    return _do_lloyds_algo(dataset, k_points)
