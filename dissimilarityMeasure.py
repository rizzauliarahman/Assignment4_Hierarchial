import numpy as np
import LoadVisualize as load

def singleLinkMIN(a, b):

    dist = (a-b)**2
    dist = np.sum(dist, axis=-1)
    dist = np.sqrt(dist)

    dist[dist == 0.0] = 1.0

    xcluster = np.argmin(dist)
    ycluster = np.argmin(load.column(dist, xcluster))

    return xcluster, ycluster


