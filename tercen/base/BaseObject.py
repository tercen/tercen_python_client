class BaseObject:
    def __init__(self, m=None):
        self.subKind = None

    def fromJson(self, m):
        pass

    def toJson(self):
        return dict()

    # def to_json(self):
    #     return self.toJson()
