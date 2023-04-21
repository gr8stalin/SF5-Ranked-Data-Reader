from json import JSONEncoder

from datatypes import RankedSession, RankedMatch, GameResult


class RankedSessionEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, RankedSession):
            return o.__dict__
        elif isinstance(o, RankedMatch):
            return o.__dict__
        elif isinstance(o, GameResult):
            return o.name
        else:
            return JSONEncoder.default(self, o)
