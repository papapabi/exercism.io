import re


NANP_REGEX = re.compile(r'''
    ^
    (\+?1)?                      # Country code
    (\s)*                        # Country code separator
    ([2-9]\d{2}|\([2-9]\d{2}\))  # Area code, group 3
    (\s|-|\.)*                   # Separator
    ([2-9]\d{2}|\([2-9]\d{2}\))  # Exchange code, group 5
    (\s|-|\.)*                   # Separator
    (\d{4})                      # Subscriber number, group 7
    $
''', re.VERBOSE)

def _validate(match_object):
    if match_object is None:
        raise ValueError('invalid phone num')
    if match_object.group(3) is None:
        raise ValueError('invalid area code')
    if match_object.group(5) is None:
        raise ValueError('invalid exchange code')


def _cleanup(number):
    number = number.strip()
    mo = NANP_REGEX.search(number)
    _validate(mo)
    return (mo.group(3).strip('()'), mo.group(5), mo.group(7))


class Phone(object):
    def __init__(self, number):
        self.area_code, self.exchange_code, self.subscriber_number = (
            _cleanup(number))
        self.number = (
            self.area_code
            + self.exchange_code
            + self.subscriber_number)

    def __repr__(self):
        return \
            f'({self.area_code}) {self.exchange_code}-{self.subscriber_number}'

    pretty = __repr__
