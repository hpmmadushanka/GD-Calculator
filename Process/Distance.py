
def calculate_distance(dis):
    g = {}
    g["similar"] = dis["similar"]
    g["differences"] = dis["difference"]
    g["distance"] = (dis["similar"]/(dis["similar"]+dis["difference"]))
    return g


# prurning method
def prurning_method(F, k):
    # print(F,k)
    keys = F.keys()
    d = 0
    k = k - 1
    if (k == 0):
        for i in keys:
            d += F[i]
    else:
        for i in keys:
            d += prurning_method(F[i], k)
    return d


# get distance betweeen two forests
def get_distance(F1, F2, k):
    similar = 0
    difference = 0

    F1keys = F1.keys()
    F2keys = F2.keys()

    F1_difference = set(F1keys) - set(F2keys)
    F2_difference = set(F2keys) - set(F1keys)
    intersection = set(F1keys).intersection(F2keys)

    k = k - 1

    if len(F1_difference) != 0:
        if (k == 0):
            for i in F1_difference:
                difference += F1[i]
        else:
            for i in F1_difference:
                difference += prurning_method(F1[i], k)
    if len(F2_difference) != 0:
        if (k == 0):
            for i in F2_difference:
                difference += F2[i]
        else:
            for j in F2_difference:
                difference += prurning_method(F2[j], k)

    if len(intersection) != 0:
        if (k != 0):

            for z in intersection:
                g = get_distance(F1[z], F2[z], k)

                difference += g["difference"]
                similar += g["similar"]
        else:
            for z in intersection:
                similar += min(F1[z], F2[z])
                difference += abs(F1[z] - F2[z])

    return {"difference": difference, "similar": similar}


def generate_distance(Dic, k):
    f = []
    if (len(Dic) > 1):
        keys = list(Dic.keys())
        if (len(keys) > 2):
            for i in range(len(keys) - 1):
                F1 = Dic[keys[i]]
                lst = keys[i + 1:]
                for key in lst:
                    g = {}
                    F2 = Dic[key]
                    distance = get_distance(F1, F2, k)
                    g["seq1"] = keys[i]
                    g["seq2"] = key
                    g["distance"] = calculate_distance(distance)
                    f.append(g)

        if (len(keys) == 2):
            g = {}
            print(keys)
            F1 = Dic[keys[0]]
            F2 = Dic[keys[1]]
            distance = get_distance(F1, F2, k)
            g["seq1"] = keys[0]
            g["seq2"] = keys[1]
            g["distance"] = calculate_distance(distance)
            f.append(g)

        return f
    else:
        return 1



def process_data(data):
    d = data.split('\n')
    d = "".join(d)
    d = d.split(' ')
    d = "".join(d)
    return d


def process_head(head):
    d = head.split('\n')
    d = "".join(d)
    d = d.split('>')
    d = "".join(d)
    return d

def get_column(head):
    d = head.split('\n')
    d = "".join(d)
    d = d.split(' ')

    return d

