def DNA_strand(dna):
    DNAString = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    dna = list(dna)
    for i in range(len(dna)):
        if dna[i] in DNAString.keys(): 
            dna[i] = DNAString.get(dna[i])
    return "".join(dna)