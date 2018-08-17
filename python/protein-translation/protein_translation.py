from itertools import takewhile, zip_longest


CODON_MAP = (
        (('AUG',),'Methionine'),
        (('UUU', 'UUC'),'Phenylalanine'),
        (('UUA', 'UUG'),'Leucine'),
        (('UCU', 'UCC', 'UCA', 'UCG'),'Serine'),
        (('UAU', 'UAC'),'Tyrosine'),
        (('UGU', 'UGC'),'Cysteine'),
        (('UGG',),'Tryptophan'),
        (('UAA', 'UAG', 'UGA'),'STOP'))


PROTEINS = { codon: name for codons, name in CODON_MAP for codon in codons }


def _grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def proteins(rna_strand):
    codons = (''.join(nucleotides) for nucleotides in _grouper(rna_strand, 3))
    proteins = takewhile(lambda x: x != 'STOP',
                         (PROTEINS[codon] for codon in codons))
    return list(proteins)
