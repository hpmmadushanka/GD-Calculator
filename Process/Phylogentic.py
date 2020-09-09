from phylogeny import DistanceMatrix
from phylogeny.reconstruction import infer_clocklike_tree1
from phylogeny.reconstruction import infer_clocklike_tree2







def getPhylogenticTree(s, seqList):
    ultrametric = DistanceMatrix(s, names=seqList)
    t1 = infer_clocklike_tree1(ultrametric)
    t2 = infer_clocklike_tree2(ultrametric)

    return str(t1)
