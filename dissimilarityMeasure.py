import numpy as np
import LoadVisualize as load
from scipy.spatial import distance as d


def singleLinkMIN(a, b):

    dist = np.zeros((len(a), len(b)))

    for i in range(len(a)):
        for j in range(len(b)):
            dist[i][j] = d.euclidean(a[i], b[j])

    xcluster, ycluster = np.unravel_index(dist.argmin(), dist.shape)

    return np.around(dist[xcluster][ycluster], decimals=2)


def completeLinkMAX(a, b):

    dist = np.zeros((len(a), len(b)))

    for i in range(len(a)):
        for j in range(len(b)):
            dist[i][j] = d.euclidean(a[i], b[j])

    xcluster, ycluster = np.unravel_index(dist.argmax(), dist.shape)

    return np.around(dist[xcluster][ycluster], decimals=2)


def groupAverage(a, b):

    dist = np.zeros((len(a), len(b)))

    for i in range(len(a)):
        for j in range(len(b)):
            dist[i][j] = np.linalg.norm(np.subtract(a[i], b[j]))

    sumDist = np.sum(dist)

    avgDistance = float(1 / (float(len(a)) * float(len(b)))) * sumDist

    return avgDistance

def centroidBased(a, b):

    centrA = np.zeros(shape=2, dtype=float)
    centrA[0] = np.sum(load.column(a, 0)) / float(len(a))
    centrA[1] = np.sum(load.column(a, 1)) / float(len(b))

    centrB = np.zeros(shape=2, dtype=float)
    centrB[0] = np.sum(load.column(b, 0)) / float(len(a))
    centrB[1] = np.sum(load.column(b, 1)) / float(len(b))

    dist = np.linalg.norm(np.subtract(centrA, centrB))

    return dist
