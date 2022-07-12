from utils.DateFormat import DateFormat


class Team():

    def __init__(self, id, name=None, duration=None, released=None) -> None:
        self.id = id
        self.name = name
        self.duration = duration
        self.released = released

    def to_JSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'duration': self.duration,
            'released': DateFormat.convert_date(self.released)
        }
