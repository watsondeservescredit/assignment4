with open("hello.txt", "r") as f:
    data = f.readlines()
k = 0
dna =""
profile=[[] for i in range(5)]
for i,line in enumerate(data):
    if i == 0:
        dna = line
    elif i == 1:
        k = int(line)
        profile=[[] for i in range(k)]
    elif i > 1 and i<6: 
        for x in range(0, k):    
            words = float(line.split()[x])
            profile[x].append(words)
    
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
print most_prob_kmer(k,dna,profile)

