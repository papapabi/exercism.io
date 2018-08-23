from math import log, floor


def rebase(input_base, digits, output_base):
    if input_base < 2 or output_base < 2:
        raise ValueError('bases must be greater than 2')
    if not _valid_digits(input_base, digits):
        raise ValueError(
            f'digits contains element not in [0, {input_base}): ' \
            f'digits = {digits}')

    output_base_digits = []
    if not digits or all(d == 0 for d in digits):
        return output_base_digits

    base_10 = sum(_to_lc(input_base, digits)) # The given number in base 10.
    highest_output_base_exp = floor(log(base_10, output_base))

    for exp in range(highest_output_base_exp, -1, -1):
        magnitude = output_base ** exp
        if magnitude > base_10:
            output_base_digits.append(0)
            continue
        digit = base_10 // magnitude
        output_base_digits.append(digit)
        base_10 -= digit * magnitude

    return output_base_digits


def _to_lc(input_base, digits):
    """Return the linear combination of the powers of input_base and digits."""
    return [d * input_base**exp 
            for d, exp in zip(digits, reversed(range(len(digits))))]

def _valid_digits(input_base, digits):
    """Return true if all digits are in the interval [0, input_base)."""
    return all(digit in range(0, input_base) for digit in digits)
