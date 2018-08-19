import re


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
    pattern_regex = re.compile(pattern, compile_flag)

    # Pre-formatted output; contains a 2-tuple of the filename and its matches
    # as a list.
    dirty_matches = []

    for file_name in files:
        matches_in_file = []
        for line_number, line in enumerate(open(file_name).readlines(), 1):
            line = line.rstrip('\n') # So re.fullmatch can work
            if _match(line, pattern_regex, flags):
                matches_in_file.append((line_number, line))
                if '-l' in flags:
                    break
        dirty_matches.append((file_name, matches_in_file))
    return _format(dirty_matches, flags)


def _match(line, regex, flags):
    '''Returns true if a line matches according to the given flags.'''
    match = regex.search(line) # Default behavior
    if '-x' in flags:
        match = regex.fullmatch(line)
    if '-v' in flags:
        match = not match
    return match


def _format(matches, flags):
    output = []
    format_s = ''

    if len(matches) > 1:
        format_s = '{file_name}:'

    if '-l' in flags:
        format_s = '{file_name}'
    elif '-n' in flags:
        format_s += '{line_number}:{line}'
    else:
        format_s += '{line}'

    format_s += '\n' # Add back rstripped line break.

    for file_name, lines in matches:
        for line_number, line in lines:
            output.append(format_s.format(file_name=file_name,
                                          line_number=line_number,
                                          line=line))
    return ''.join(output)
