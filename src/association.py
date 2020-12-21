minSupport = 2
minConfidence = 4

transactions = {
    1: (1, 2, 5),
    2: (2, 4),
    3: (2, 3),
    4: (1, 2, 4),
    5: (1, 3),
    6: (2, 3),
    7: (1, 3),
    8: (1, 2, 3, 5),
    9: (1, 2, 3),
}

def extractUniqueItems(transactions):
    uniqueItems = {}
    for l in transactions.values():
        for i in l:
            if not uniqueItems.get(i, None):
                uniqueItems[i] = 1
        
    return list(zip(sorted(uniqueItems.keys())))

def computeSupportCount(itemSets, transactions):
    sp = {}
    for i in itemSets:
        sp[i] = 0
        for l in transactions.values():
            if tuple(i) == tuple(set(i).intersection(set(l))):
                sp[i] += 1 

    return sp


def filterSupportCount(sp, minSc):
    return {i: sc for i, sc in sp.items() if sc >= minSc}


def computeItemSets(itemSets):
    """
    Compute item sets of next level from given itemsets.
    """
    sp = sorted(itemSets.keys())
    outItemSets = []
    for indx1 in range(0, len(sp)):
        for indx2 in range(indx1 + 1, len(sp)):
            newItemSet = tuple(set(sp[indx1] + sp[indx2]))
            if len(newItemSet) == len(sp[indx1]) + 1 and newItemSet not in outItemSets:
                outItemSets.append(newItemSet)
            
    return outItemSets


itemSets = extractUniqueItems(transactions)

while len(itemSets) > 0:
    print('ItemSets',itemSets)
    supportCount = computeSupportCount(itemSets, transactions)
    #print('Intial SP Count', supportCount)
    supportCountFiltered = filterSupportCount(supportCount, minSupport)
    print('SP Count', supportCountFiltered)

    itemSets = computeItemSets(supportCountFiltered)
