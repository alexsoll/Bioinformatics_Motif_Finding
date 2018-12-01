import itertools
import sys
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

def hamming_distance(pattern,text,k):
    return sum([1 for i in range(k) if pattern[i] != text[i]])

def distance(pattern,str_dna,k):
    return (pattern,min([hamming_distance(pattern,i,k) for i in correct(str_dna,k)]))

def total_distanse(dna, pattern, k):
    return sum([distance(pattern, dna_str,k)[1] for dna_str in dna])

def correct(seq,k):
    return set(seq[i:i+k] for i in range(len(seq)-k+1))

def d(pattern, dna):
    N = len(pattern)
    lenDNA = len(dna[0])
    motifs = [] 
    dist = []
    for d in dna:
        dis = 0
        bestMotifinSting = ''
        for i in range(lenDNA-N+1):
            pat = d[i:i+N]
            coin = coincidence(pat, pattern)
            if coin >= dis:
                dis = coin
                bestMotifinSting = pat
        dist.append(dis)
        motifs.append(bestMotifinSting)
    res = 0
    for val in dist:
        res += N - int(val)
    return res


def MedianString(dna, k):
    distanse = sys.maxsize
    patterns = []
    nucleotids = 'ACGT'
    Median = ''
    patterns = list(itertools.product(nucleotids, repeat=k))
    for i,val in enumerate(patterns):
        patterns[i] = ''.join(val)
    for pattern in patterns:
        #dis = total_distanse(dna, pattern, k)              #using a better solution
        dis = d(pattern, dna)
        if distanse >= dis:
            distanse = dis
            Median = pattern
    return Median


dna1 = ['AGCTTAATTGATCGCTTTCGG',
'GTTACGACCAATTGGGTTCGG',
'CGTCAGGTACGTCGCCTGCGG',
'GCTGAGCGGGCATCCCGGCGG',
'AGTACCTTCGGGAGCATGCGG']
k1 = 3


dna = ['GAAACTACGCACGTAGTGTTTTGCTACGGTTCTCA',
'TATATCCACATGACCTCGACAACGCACGGTCGAAT',
'TAGCGGGACAATCAGGTCTGAGTCGACTGTTGTGC',
'TCCTGCCGGTTGCTAACTGTAGACGTTTACCCCTT',
'TCCCTCCCTAACTCTAGGCTACTGTCGTCCGCAGT',
'AGGCAGAAAGACAACGGTAGTAATCTAGAGACCGT',
'CGCTCCACGCAGCTCATAGAACCGTGTTGTTCAAC',
'ACTGTCTCCCGGAAACCATAAACTACTTGGTTTGT',
'GGTTTTCTTGACTGTAATTACAATCCAGGAGACCA',
'ATGTCGCTCTACAGTGAACACGTAACTGTCTTCGG']   
k = 5

#-----MedianString test-----#
s = MedianString(dna1,k1)
print(s)
#---------------------------#


#--------MotifEnumerate test--------#
d('AAA', ['ttaccttAAc','gAtAtctgtc','Acggcgttcg','ccctAAAgag','cgtcAgAggt'])
dna = ['CACTGATCGACTTATC','CTCCGACTTACCCCAC','GTCTATCCCTGATGGC','CAGGGTTGTCTTGTCT']
k = 4
d = 1
MotifEnumeration(dna, k, 1)

#-----------------------------------#