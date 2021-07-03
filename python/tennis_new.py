class Tennis:
    def __init__(self, player1Name, player2Name) -> None:
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.player1_score = 0
        self.player2_score = 0
        self.map = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def score(self):
        if self.player1_score != self.player2_score:
            if self.player1_score > 3 or self.player2_score > 3:
                if abs(self.player1_score - self.player2_score) == 1:
                    return "Advantage " + self.get_advanced_player()
                return "Win for " + self.get_advanced_player()
            else:
                return f"{self.map[self.player1_score]}-{self.map[self.player2_score]}"
        else:
            if self.player1_score in [1, 2]:
                return self.map[self.player1_score] + "-All"
            if self.player1_score >= 3:
                return "Deuce"
        return "Love-All"

    def get_advanced_player(self):
        advanced_player = self.player1Name if self.player1_score > self.player2_score else self.player2Name
        return advanced_player
