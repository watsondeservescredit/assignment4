with open("hellosweety.txt", "r") as f:
    data = f.readlines()
k = 0
#global super score
super_score= 10000000
super_motifs= []
#strand array
Dna = []
for i,line in enumerate(data):
    if i == 0:
        k = int(line.split()[0])
        t = int(line.split()[1])
    elif i > 0 and i <= t:
        Dna.append(line.rstrip())
from random import randint
def laplace_profil(motifs):
    #return profile:[[A,C,G,T],[A,C,G,T],...,repeat k times]
    k = len(motifs[0])
    p = []
    #move through columns
    for x in range(0,k):
        l= [z[x]   for z in motifs]
        p_column = [0] * 4
        #count all the bases
        for c in l:
            i = SymbolToNumber(c)
            p_column[i] += 1
        #add pseudo counts
        for i,base in enumerate(p_column):
            p_column[i] += 1
        c_sum =sum(p_column)
        #calculate probability
        for i,base in enumerate(p_column):
            p_column[i] = float(base)/c_sum
        p.append(p_column)
        count_list = []

    return p
def calc_prob(profile,kmer):
    prob_ges = 1 
    for i, c in enumerate(kmer):
        prob_c = profile[i][SymbolToNumber(c)]
        prob_ges *= prob_c
    return prob_ges
def most_prob_kmer(k,Dna, profile):
    best_prob = 0
    closest_kmer=""
    probest_kmer = ""
    for i in range(0, len(Dna) -k):
        # extract current kmer 
        kmer = Dna[i:i+k]
        #omnomnonoonmnonoomm
        new_prob = calc_prob(profile, kmer)
        if new_prob > best_prob:
            best_prob = new_prob
            probest_kmer = kmer
    return probest_kmer

def SymbolToNumber(s):
	if s == 'A':
       		return 0
    	elif s == 'C':
        	return 1
    	elif s == 'G':
        	return 2
    	elif s == 'T':
        	return 3
def most_prob_motifs(k,Dna_strands, profile):
    motifs = []
    #select kmer Motifs in each strand in Dna_strands strand array based on profile  
    for strand in Dna_strands:
        motifs.append(most_prob_kmer(k,strand,profile))
    return motifs
from collections import Counter

def Most_Common(lst):
    data = Counter(lst)
    return data.most_common(1)[0][0]
def score(motifs):
    k = len(motifs[0])
    score = 0
    for x in range(0,k):
        l= [z[x]   for z in motifs]
        mc = Most_Common(l)
        score += len([bla for bla in l if bla != mc])
    return score
            

def randy_motif_search(Dna_strands,k):
    global super_score
    global super_motifs
    best_motifs = []
    #randomly select kmer Motifs in each strand in Dna_strands strand array    
    for strand in Dna_strands:
        kmer_index = randint(0, len(strand) -k)
        best_motifs.append(strand[kmer_index:kmer_index +k])
    #set the running motifs array equal the randomly selected best_motifs for starters
    motifs =list(best_motifs)
    while True:
        #create profile(with pseudocounts) from the motifs array 
        profil = laplace_profil(motifs)
        #find most_prob_motifs from this profile
        motifs = most_prob_motifs(k,Dna_strands,profil)
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
        else:
            return best_motifs
#run randy_motif a thousand miles
for i in range(0,1000):
    motifs = randy_motif_search(Dna,k)
    if score(motifs) < super_score:
        super_motifs = motifs
        super_score = score(motifs)
print "\n".join(super_motifs)
        
