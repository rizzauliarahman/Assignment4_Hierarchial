import numpy as np
import LoadVisualize as load

def main():
    a = np.array([[9, 6]])
    b = np.array([[7, 8]])

    dist = (a - b) ** 2
    dist = np.sum(dist, axis=-1)
    dist = np.sqrt(dist)

    print dist
    print ' '

    dist[dist == 0] = 1

    print dist

main()