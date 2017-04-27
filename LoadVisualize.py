import numpy as np
import os
import plotly.offline as py
import plotly.figure_factory as ff

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

def showDendro(dist, label):
    from matplotlib import pyplot as plt
    from scipy.cluster.hierarchy import dendrogram

    dendro = ff.create_dendrogram(dist, labels=label)
    py.plot(dendro, image='png', image_filename='dendro1')
