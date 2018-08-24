from collections import defaultdict


class Team(object):
    def __init__(self, name, wins=0, draws=0, losses=0):
        self.name = name
        self.wins, self.draws, self.losses = wins, draws, losses
        self._points = None

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        """Return the name and W/D/L/P."""
        return f'{self.name}; ' \
                f'{self.wins}/{self.draws}/{self.losses}/{self.points}'
    
    def __lt__(self, other):
        return self.points < other.points
    
    def __add__(self, other):
        return Team(self.name, self.wins + other.wins,
                    self.draws + other.draws, self.losses + other.losses)
    
    @property
    def points(self):
        if _points is None:
            _points = 3*self.wins + self.draws
        return _points


def tally(tournament_results):
    table = defaultdict(Team)
    for line in tournament_results.splitlines():
        home, away, res = line.split(';')
        home_team = Team(name=home)
        away_team = Team(name=away)
        pass

