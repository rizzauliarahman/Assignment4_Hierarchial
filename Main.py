import LoadVisualize as load

def main():
    attr = load.loadDataset('Hierarchical_2.csv')
    print len(attr)
    load.visualizeScatter(attr)

main()