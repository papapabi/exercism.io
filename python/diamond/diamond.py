def _widest_point(letter):
    return 2 * (ord(letter) - ord('A')) + 1

def _make_row(letter, widest_point):
    if letter == 'A':
        spacing = (widest_point - 1) // 2
        row = ' ' * spacing + letter + ' ' * spacing
    else:
        inner = letter + (2 * (ord(letter) - ord('A')) - 1) * ' ' + letter
        spacing = (widest_point - len(inner)) // 2
        row = ' ' * spacing + inner + ' ' * spacing
    return row

def make_diamond(letter):
    result, stack = [], []
    widest_point = _widest_point(letter)
    for ascii_code in range(ord('A'), ord(letter) + 1):
        row = _make_row(chr(ascii_code), widest_point)
        result.append(row)
        stack.append(row)
    stack.pop() # Remove the widest point
    while stack:
        result.append(stack.pop())
    return '\n'.join(result) + '\n'
