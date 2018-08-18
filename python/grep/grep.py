import re


def _match(line, regex, flags):
    '''Returns true if a line matches according to the given flags.'''
    match = regex.search(line) # Default behavior

    if '-x' in flags:
        match = regex.fullmatch(line)

    if '-v' in flags:
        match = not match 
        
    return match


def grep(pattern, files, flags=''):
    '''Function that emulates UNIX grep.

    Flags:
        -i: ignorecase
        -x: match entire lines, instead of lines that contain a match
        -v: inverse; collect lines that fail to match the pattern
        -l: print only the names of files that has at least one matching line
        -n: print the line numbers of each matching line
    '''
    compile_flag = 0
    if '-i' in flags:
        compile_flag = compile_flag | re.IGNORECASE
    pattern_regex = re.compile(pattern, re_compile_flag)
    for filename in files:
        dirty_matches = [] # Pre-formatted output
        for line_number, line in enumerate(open(filename).readlines(), 1):
            if _match(line, pattern_regex, flags):
                if '-l' in flags:
                    break
                dirty_matches.append((line_number, line))
        dirty_matches.append(filename)
