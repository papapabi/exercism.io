from math import log, floor


def rebase(input_base, digits, output_base):
    if output_base < 2:
        raise ValueError("output_base must be greater than 2")
    base_10_digits = _to_base10(input_base, digits)
    if output_base == 10:
        return base_10_digits

    base_10 = sum(base_10_digits)
    highest_output_base_exp = floor(log(base_10, output_base))
    output_base_digits = []
    
    for exp in range(highest_output_base_exp, -1, -1):
        intermediary = output_base ** exp
        # if intermediary > base_10, append 0 and continue
        if intermediary > base_10:
            output_base_digits.append(0)
            continue
        output_base_digits.append(base_10 // intermediary)
        base_10 -= intermediary

    return output_base_digits


def _to_base10(input_base, digits):
    """Return a list of base 10 digits."""
    return [d * input_base**exp 
            for d, exp in zip(digits, reversed(range(len(digits))))]
