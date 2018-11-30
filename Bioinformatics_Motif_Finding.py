import itertools
def coincidence(pattern1 , pattern2):
    coinc = sum(a == b for a, b in zip(pattern1, pattern2))
    return coinc

def buildPatterns(pattern, k, d):
    patterns = []
    res = []
    nucleotids = 'ACGT'
    patterns = list(itertools.product(nucleotids, repeat=4))
    for i,val in enumerate(patterns):
        patterns[i] = ''.join(val)
    for val in patterns:
        if k - coincidence(pattern, val) <= d:
            res.append(val)
    return res

def appears(dna, pattern, k, d):
    N = len(dna)
    for i in range(N-k+1):
        pat = dna[i:i+k]
        if k - coincidence(pat, pattern) <= d:
            return True
    return False

def MotifEnumeration(dna, k, d):
    patterns = []
    num_of_dna = len(dna)
    N = len(dna[0])
    S = set()
    for i in range(N-k+1):
        pat = dna[0][i:i+k]
        p = buildPatterns(pat, k, d)
        for val in p:
            num_of_find = 0
            for st in dna:
                if appears(st, val,k, d):
                    num_of_find += 1
            if num_of_find == num_of_dna:
                S.add(val)
    s = ""
    for i in S:
        s += i + " "
    print(s)
        

def main():
    s = sys.stdin.read().split("\n")
    s[0] = s[0].split(" ")
    k = int(s[0][0])
    d = int(s[0][1])
    dna = []
    dna = s[1:]
    MotifEnumeration(dna, k, d)


main()


#dna = ['CACTGATCGACTTATC','CTCCGACTTACCCCAC','GTCTATCCCTGATGGC','CAGGGTTGTCTTGTCT']
#k = 4
#d = 1
#MotifEnumeration(dna, k, 1)