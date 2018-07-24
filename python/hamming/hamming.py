def distance(strand_a, strand_b):
    """Returns the hamming distance between two DNA strands.
    
    :param strand_a (str): the first DNA string.
    :param strand_b (str): the second DNA string.
    :returns: the hamming distance.
    """
    if len(strand_a) != len(strand_b):
        raise ValueError("strings are of unequal length")
    return sum(1 for a, b in zip(strand_a, strand_b) if a != b) 
