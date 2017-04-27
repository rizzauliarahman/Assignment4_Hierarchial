import numpy as np
import LoadVisualize as load
import dissimilarityMeasure as dis
from scipy.cluster.hierarchy import dendrogram, linkage
import Cluster as cl

def main(mode):

    attr = load.loadDataset('Hierarchical_2.csv')
    load.visualizeScatter(attr)
    Z = []

    cluster = [cl.Cluster([attr[i]], i+1) for i in range(len(attr))]

    label = []
    for i in range(len(cluster)):
        label.append(cluster[i].label)

    i = 2

    clusterLength = len(cluster)

    while clusterLength != 1:
        mergedCluster = []
        transCluster = []
        takenCluster = []

        dist = np.zeros((len(cluster), len(cluster)))

        for i in range(len(cluster)):
            for j in range(len(cluster)):
                cluster1 = cluster[i]
                cluster2 = cluster[j]
                if mode == 'single':
                    dist[i][j] = dist[j][i] = dis.singleLinkMIN(cluster1.attr, cluster2.attr)
                elif mode == 'complete':
                    dist[i][j] = dist[j][i] = dis.completeLinkMAX(cluster1.attr, cluster2.attr)
                    break
                elif mode == 'average':
                    dist[i][j] = dist[j][i] = dis.groupAverage(cluster1.attr, cluster2.attr)
                    break
                elif mode == 'centroid':
                    dist[i][j] = dist[j][i] = dis.centroidBased(cluster1.attr, cluster2.attr)

        dist[dist == 0] = 100

        for i in range(len(cluster)):
            xcluster = i
            ycluster = np.argmin(dist[xcluster])

            if [ycluster, xcluster] not in mergedCluster and ycluster not in takenCluster and xcluster not in takenCluster:
                mergedCluster.append([xcluster, ycluster])
                takenCluster.append(xcluster)
                takenCluster.append(ycluster)

        for data in mergedCluster:
            transCluster.append(cl.Cluster(np.concatenate((cluster[data[0]].attr, cluster[data[1]].attr)),
                                           min(cluster[data[0]].label, cluster[data[1]].label)))

        for i in range(len(cluster)):
            if i not in takenCluster:
                transCluster.append(cluster[i])

        cluster = transCluster
        clusterLength = len(cluster)

        if mode == 'complete' or mode == 'average':
            clusterLength = 1

        i += 1

    Z = linkage(attr, method=mode)
    load.showDendro(Z)

main(mode='centroid')
