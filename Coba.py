import numpy as np
import LoadVisualize as load
import dissimilarityMeasure as dis
from scipy.cluster.hierarchy import dendrogram, linkage
import Cluster as cl

def main():

    attr = load.loadDataset('Hierarchical_2.csv')
    load.visualizeScatter(attr)
    Z = []

    xcluster = 0
    ycluster = 0

    cluster = []

    for i in range(len(attr)):
        cluster.append(cl.Cluster(attr[i], i+1))

    label = []
    for i in range(len(cluster)):
        label.append(i+1)

    while len(cluster) != 1:
        mergedCluster = []
        transCluster = []
        takenCluster = []

        dist = np.zeros((len(cluster), len(cluster)))

        for i in range(len(cluster)):
            for j in range(len(cluster)):
                dist[i][j] = dist[j][i] = dis.singleLinkMIN(cluster[i], cluster[j])

        dist[dist == 1] = 10

        for i in range(len(cluster)):
            xcluster = i
            ycluster = np.argmin(dist[xcluster])

            if [ycluster, xcluster] not in mergedCluster and ycluster not in takenCluster and xcluster \
                    not in takenCluster:
                mergedCluster.append([xcluster, ycluster])
                takenCluster.append(xcluster)
                takenCluster.append(ycluster)

        print mergedCluster

        for data in mergedCluster:
            transCluster.append(np.concatenate((cluster[data[0]], cluster[data[1]])))
            Z.append([data[0], data[1], dist[data[0]][data[1]], 2])

        for i in range(len(cluster)):
            if i not in takenCluster:
                transCluster.append(cluster[i])

        cluster = transCluster
        print len(cluster)

main()