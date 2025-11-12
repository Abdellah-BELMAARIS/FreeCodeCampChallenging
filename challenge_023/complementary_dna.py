def complementary_dna(strand):
    complement = ""
    for char in strand:
        if char == 'A':
            complement += 'T'
        elif char == 'T':
            complement += 'A'
        elif char == 'C':
            complement += 'G'
        elif char == 'G':
            complement += 'C'
    return complement

print(complementary_dna("ACGT"))
print(complementary_dna("ATGCGTACGTTAGC"))
print(complementary_dna("GGCTTACGATCGAAG"))
print(complementary_dna("GATCTAGCTAGGCTAGCTAG"))