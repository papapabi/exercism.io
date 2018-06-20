def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("strings are of unequal length")
    distance = 0
    zipped_strands = zip(strand_a, strand_b)
    for a, b in zipped_strands:
        if a != b: 
            distance += 1
    return distance
