from enum import Enum
NUM_ACTIONS = 5


class Action(Enum):
    SpecifyInfo = 0
    SearchDatabase = 1
    AddToChart = 2
    SearchMemory = 3
    Nothing = 4

    @classmethod
    def length(cls):
        return NUM_ACTIONS

    @classmethod
    def from_str(cls, action):
        if action == "SearchDatabase":
            return cls.SearchDatabase.value
        elif action == "SpecifyInfo":
            return cls.SpecifyInfo.value
        elif action == "AddToCart":
            return cls.AddToChart.value
        elif action == "SearchMemory":
            return cls.SearchMemory.value
        else:
            return cls.Nothing.value

    @classmethod
    def from_number(cls, value):
        if value == cls.SpecifyInfo.value:
            return "SpecifyInfo"
        elif value == cls.SearchDatabase.value:
            return "SearchDatabase"
        elif value == cls.AddToChart.value:
            return "AddToCart"
        elif value == cls.SearchMemory.value:
            return "SearchMemory"
        else:
            return "None"