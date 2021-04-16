class Team():

    def __init__(self, id, name, players = None, scores = None):
        self.id = id
        self.name = name
        if players is None:
            self.players = []
        else:
            self.players = players
        if scores is None:
            self.scores = []
        else:
            self.scores = scores

