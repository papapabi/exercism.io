from collections import namedtuple
from itertools import cycle, dropwhile, islice


CHROMATIC_SHARPS = "C C# D D# E F F# G G# A A# B".split()
CHROMATIC_FLATS = "C Db D Eb E F Gb G Ab A Bb B".split()

USES_SHARPS = ('G', 'D', 'A', 'E', 'B', 'F#' 'e', 'b', 'f#', 'c#', 'g#', 'd#')
USES_FLATS = ('F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'd', 'g', 'c', 'f', 'bb', 'eb')

INTERVAL_TO_SEMITONE_VALUE = {'m': 1, 'M': 2, 'A': 3}


class Scale(object):
    @staticmethod
    def __generate_chromatic(tonic):
        """Generates the chromatic scale for a given tonic."""
        if tonic in USES_FLATS:
            tones = CHROMATIC_FLATS
        else:
            tones = CHROMATIC_SHARPS
        cycled = cycle(tones)
        start_at_tonic = dropwhile(lambda x: x != tonic, cycled)
        chromatic_tones = islice(start_at_tonic, 12)
        return list(chromatic_tones)

    def __init__(self, tonic, intervals=None):
        if intervals is None:
            self.pitches = self.__generate_chromatic(tonic)
        else:
            available_pitches = self.__generate_chromatic(tonic)
            self.pitches = [tonic]
            for interval in intervals:
                self.pitches.append(
                    available_pitches[
                        (available_pitches.index(self.pitches[-1]) 
                        + INTERVAL_TO_SEMITONE_VALUE[interval])
                        % 12])
            self.pitches.pop()
