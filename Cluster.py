import numpy as np

class Cluster:

    def __init__(self, attr, label):
        self.attr = attr
        self.label = label

    def concat(self, attr):
        np.concatenate((self.attr, attr))

    def getAttr(self):
        return self.attr
