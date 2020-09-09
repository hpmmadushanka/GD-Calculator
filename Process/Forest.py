# count K mers
def getkmers(Tseq, k):
    if (k >= len(Tseq)):
        print("Specify a kmer size, which is less than to the length of the sequence")
        return
    KFreq = {}
    for i in range(0, (len(Tseq) - k + 1)):
        Kmer = Tseq[i:i + k]
        if Kmer in KFreq:
            KFreq[Kmer] += 1
        else:
            KFreq[Kmer] = 1

    return KFreq


# add kmer to forest
def add_kmer_to_forest(F, K, freq):
    if len(K) > 1:
        if K[0] not in F.keys():
            F[K[0]] = {}
        F[K[0]] = add_kmer_to_forest(F[K[0]], K[1:], freq)
    else:
        F[K[0]] = freq

    return F


# k mer forest creator
def forest(KFreq):
    F = {}
    for kmer in KFreq:
        freq = KFreq[kmer]
        F = add_kmer_to_forest(F, kmer, freq)
    return F


def forest_constructor(data, k):
    KFreq = getkmers(data, k)
    f = forest(KFreq)
    return f