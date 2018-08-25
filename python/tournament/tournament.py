import operator
from collections import defaultdict
from functools import total_ordering


@total_ordering
class Team(object):
    def __init__(self, name=None, wins=0, draws=0, losses=0):
        self.name = name
        self.wins, self.draws, self.losses = wins, draws, losses

    def __eq__(self, other):
        return self.name == other.name
        
    def __repr__(self):
        return '{} | {}/{}/{}/{}/{}'.format(
            self.name, self.matches, self.wins, self.draws, self.losses,
            self.points)

    def __lt__(self, other):
        return self.points < other.points
    
    def __add__(self, other):
        return Team(other.name, self.wins + other.wins,
                    self.draws + other.draws, self.losses + other.losses)
    
    @property
    def points(self):
        return 3*self.wins + self.draws

    @property
    def matches(self):
        return self.wins + self.draws + self.losses


def tally(tournament_results):
    teams = defaultdict(Team)
    table = []
    for line in tournament_results.splitlines():
        home, away, res = line.split(';')
        if res == 'win':
            teams[home] += Team(name=home, wins=1)
            teams[away] += Team(name=away, losses=1)
        elif res == 'loss':
            teams[home] += Team(name=home, losses=1)
            teams[away] += Team(name=away, wins=1)
        else:
            teams[home] += Team(name=home, draws=1)
            teams[away] += Team(name=away, draws=1)
    header = '{:30s} | MP |  W |  D |  L |  P'.format('Team')
    table.append(header)
    teams_alphabetical = reversed(
        sorted(teams.values(), key=operator.attrgetter('name')))
    for team in reversed(sorted(teams_alphabetical)):
        table.append('{:30s} | {:2} | {:2} | {:2} | {:2} | {:2}'.format(
            team.name, team.matches, team.wins, team.draws, team.losses,
            team.points))
    return '\n'.join(table)
