class Team:
    def __init__(self, name="name", origin="origin"):
        self.Name = name
        self.Origin = origin

    def setName(self, name):
        self.Name = name

    def setOrigin(self, origin):
        self.Origin = origin

#Abstract class
class Player(Team):
    def __init__(self, playerName, playerPoints, teamName, teamOrigin):
        Team.__init__(self, teamName, teamOrigin) #The parameters are required if there are not default values
        self.pName = playerName
        self.Points = playerPoints

    def scorePoint(self):
        self.Points += 1

    def setPName(self, name):
        self.pName = name

    def print(self):
        print(f"{self.pName} is from team {self.Name} from {self.Origin} and has {self.Points} points")

    def __str__(self):
        return self.pName + " has scored " + str(self.Points)

Team1 = Team("Tigers", "Chicago")
Team2 = Team("Hawks", "NY")
Team3 = Team()
print(Team1.Name)
print(Team1.Origin)
print(Team2.Name)
print(Team2.Origin)
print(Team3.Name)
print(Team3.Origin)
print("---------Division---------")

Player1 = Player("Sid", 0, "Sharks", "Chicago")
Player1.print()
Player1.scorePoint()
Player1.print()
print(Player1)




