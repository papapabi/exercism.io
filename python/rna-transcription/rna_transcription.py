import re

complement = {'G': 'C',
              'C': 'G',
              'T': 'A',
              'A': 'U'}

def to_rna(dna):
    p = re.compile('[^GCTA]')
    if p.search(dna):
        return ''
    else:
        return ''.join(complement[nucleotide] for nucleotide in dna)
