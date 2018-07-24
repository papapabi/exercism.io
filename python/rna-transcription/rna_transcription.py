import re

DNA_TO_RNA_MAPPING = str.maketrans('GCTA', 'CGAU')

def to_rna(dna):
    """Returns the RNA complement of a given DNA strand.

    :param dna (str): the DNA strand.
    :returns: the RNA complement.
    :raises ValueError: if the argument dna contains characters other than
    [GCTA]
    """
    not_dna_chars = re.compile(r'[^GCTA]|^$')
    if not_dna_chars.search(dna):
        raise ValueError(f'cannot contain characters other than [GCTA]')
    return dna.translate(DNA_TO_RNA_MAPPING)
