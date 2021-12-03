import random

class RockPaperScissors:
    def __init__(self, player, computer, computerChoices, playerpoints, computerpoints, playagain):
        self.player = player
        self.computer = computer
        self.computer_choices = computerChoices
        self.playerpoints = playerpoints
        self.computerppoints = computerpoints
        self.playagain = playagain
    
    
    def choose(self):
        global player, computer, computerChoices
        
        while True:
            computer = random.choice(computerChoices)
            player = input("Please enter your choice of either, 'rock, paper, scissors': ")
            player = player.lower()
            if player == "rock":
                rps.calculateWinner()

            elif player == "paper":
                print("test2")
                rps.calculateWinner()

            elif player == "scissors":
                print("test3")
                rps.calculateWinner()

            else:
                print(player, " is not a correct choice") 
    
    def calculateWinner(self):
        global player, computer, playerpoints, computerpoints
        if player == computer:
            print("Tie! you both chose " + player)
        elif player == "rock":
            if computer == "paper":
                print("You lose! " + computer + " beats " + player)
                computerpoints += 1
            else:
                print("You win! " + player + " beats " + computer)
                playerpoints += 1

        elif player == "paper":
            if computer == "scissors":
                print("You lose! " + computer + " beats " + player)
                computerpoints += 1
            else:
                print("You win! " + player + " beats " + computer)
                playerpoints +=1

        elif player == "scissors":
            if computer == "rock":
                print("You lose! " + computer + " beats " + player)
                computerpoints += 1
            else:
                print("You win! " + player + " beats " + computer)
                playerpoints += 1
        rps.displayGameWinner()

        
    
    def displayGameWinner(self):
        global playagain, playerpoints, computerpoints
        if computerpoints == 3:
            print("Computer has gotten 3 points! Computer wins")
            playagain = input("Please enter 'Yes' to play again or 'No' to stop: ")
            playagain = playagain.lower()
            if playagain == "yes" or playagain == "y":
                computerpoints = 0
                playerpoints = 0
                return
            
            elif playagain == "no" or playagain == "n":
                exit()
            
            else:
                print("Please enter either yes or no")

            
        
        elif playerpoints == 3:
            print("Player has gotten 3 points! Player wins")
            playagain = input("Please enter 'Yes' to play again or 'No' to stop: ")
            playagain = playagain.lower()
            if playagain == "yes" or playagain == "y":
                computerpoints = 0
                playerpoints = 0
                return
            
            elif playagain == "no" or playagain == "n":
                exit()
            
            else:
                print("Please enter either yes or no")
        
        print("The Player has: " + str(playerpoints))
        print("The Computer has: " + str(computerpoints))
        print("First to 3 points wins\n\n")
        return

computerChoices = ["rock", "paper", "scissors"]
player = ""
playerpoints = 0
computer = ""
computerpoints = 0
playagain = ""

rps = RockPaperScissors(player, computer, computerChoices, playerpoints, computerpoints, playagain)

rps.displayGameWinner()
while playerpoints or computerpoints != 3:
    rps.choose()



