import numpy as np
import LoadVisualize as load
from scipy.spatial import distance as d


def singleLinkMIN(a, b):

    dist = np.zeros((len(a), len(b)))

    for i in range(len(a)):
        for j in range(len(b)):
            dist[i][j] = d.euclidean(a[i], b[j])

    dist[dist == 0] = 1

    xcluster, ycluster = np.unravel_index(dist.argmin(), dist.shape)

    return np.around(dist[xcluster][ycluster], decimals=2)


