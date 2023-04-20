from enum import Enum


class GameResult(Enum):
    """
    Denotes whether the match was won or lost
    """
    # Default condition should be victory!
    WIN = 0,
    LOSS = 1

    @staticmethod
    def from_str(val: str):
        if val.lower() == "w":
            return GameResult.WIN
        elif val.lower() == "l":
            return GameResult.LOSS
        else:
            raise NotImplementedError


class RankedMatch:
    """
    Represents the core data of a ranked match
    """
    def __init__(self, points: int, result: GameResult, opponent: str, replay_id: str):
        self.points = points
        self.result = result
        self.opponent = opponent
        self.replay_id = replay_id


class RankedSession:
    """
    Represents a ranked session
    """
    def __init__(self, points_start: int, points_end: int, matches: list[RankedMatch]):
        self.points_start = points_start
        self.points_end = points_end
        self.matches = matches

    @property
    def delta(self):
        """
        The change in lp (league points) for the session
        :return:
        """
        return abs(self.points_start - self.points_end)

    @property
    def total_games_played(self):
        """
        The total number of games played for the session
        :return:
        """
        return len(self.matches)

    @property
    def wins(self):
        """
        The total winning matches in the session
        :return:
        """
        return len([x for x in self.matches if x.result == GameResult.WIN])

    @property
    def losses(self):
        """
        The total losing matches in the session
        :return:
        """
        return len([x for x in self.matches if x.result == GameResult.LOSS])

