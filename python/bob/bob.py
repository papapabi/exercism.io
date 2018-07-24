def hey(s):
    s = s.strip()
    if s.isupper():
        if s.endswith('?'):
            return "Calm down, I know what I'm doing!"
        return 'Whoa, chill out!'
    elif s.endswith('?'):
        return 'Sure.'
    elif s == '':
        return 'Fine. Be that way!'
    else:
        return 'Whatever.'
