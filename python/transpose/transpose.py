from itertools import zip_longest


def transpose(input_lines):
    lines = input_lines.split('\n')
    transposed_lines = (''.join(aggregate).rstrip('&').replace('&', ' ')
                        for aggregate in zip_longest(*lines, fillvalue='&'))
    return '\n'.join(transposed_lines)
