import random
import string
from itertools import chain

class Robot(object):
    @staticmethod
    def generate_name(letter_count=2, number_count=3):
        random.seed()
        numbers = (str(random.randint(0, 9)) for __ in range(number_count))
        letters = (random.choice(string.ascii_uppercase) for _ in
                   range(letter_count))
        return ''.join(chain(letters, numbers))

    def __init__(self):
        self.name = self.generate_name()

    def reset(self):
        self.name = self.generate_name()
