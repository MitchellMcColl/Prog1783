import random

class RockPaperScissors:
    def __init__(self, player,computer, computerChoices, playerpoints, computerpoints):
        self.player = player
        self.computer = computer
        self.computer_choices = computerChoices
        self.playerpoints = playerpoints
        self.computerppoints = computerpoints
    
    
    def choose(self):
        global player, computer, computerChoices
       
        computer = random.choice(computerChoices)

        while True:
            player = input("Please enter your choice of either, 'rock, paper, scissors': ")
            if player == "rock" or player == "Rock" or player == "paper" or player == "Paper" or player == "scissors" or player == "Scissors":
                rps.calculateWinner()
            else:
                print(player + " is not a correct choice.") 
    
    def calculateWinner(self):
        return
    
    def displayResults(self):
        return

computerChoices = ["Rock", "Paper", "Scissors"]
player = ""
playerpoints = 0
computer = ""
computerpoints = 0

rps = RockPaperScissors(player, computer, computerChoices, playerpoints, computerpoints)

while playerpoints or computerpoints != 3:
    rps.choose()



