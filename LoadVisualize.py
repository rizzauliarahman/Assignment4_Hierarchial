import numpy as np
import os

def column(matrix, i):
    return [row[i] for row in matrix]

def loadDataset(filename):
    path = '.\Dataset'

    attr = np.genfromtxt(os.path.join(path, filename), usecols=(0,1), delimiter=',')

    return attr

def visualizeScatter(attr):
    from matplotlib import pyplot as plt

    # for i in range(len(attr)):
    #     x, y = attr[i][0], attr[i][1]
    #     print 'a'
    #     plt.scatter(x, y, c='B')

    plt.scatter(column(attr, 0), column(attr, 1))

    plt.show()

def visualizeCentroids(plt, centroids):
    import colorsys

    HSV_tuples = [(x * 1.0 / len(centroids), 0.75, 0.75) for x in range(len(centroids))]
    RGB_tuples = map(lambda x: colorsys.hsv_to_rgb(*x), HSV_tuples)

    for i in range(len(centroids)):
        x, y = centroids[i][0], centroids[i][1]
        plt.scatter(x, y, c = RGB_tuples[i], label = i+1, marker='D', s=50)