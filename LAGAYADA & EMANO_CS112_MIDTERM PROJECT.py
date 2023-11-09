import turtle
import random

# Setting up Screen
screen = turtle.Screen()
screen.setup(690, 690)
screen.title("Race Game! Player Vs Computer by Lagayada & Emano")
screen.bgcolor("cyan")

# Character of the game
# Color Red Player 1
player1 = turtle.Turtle()
player1.color("red")
player1.shape("turtle")
player1.penup()
player1.goto(-200, 80)

# Color Blue Computer
computer = player1.clone()
computer.color("blue")
computer.penup()
computer.goto(-200, -100)

# Creating Starting Line
start = turtle.Turtle()
start.penup()
start.goto(-170,-1)
start.shape("square")
start.color("green")
start.shapesize(stretch_wid = 40, stretch_len = 1)

# Finish line or Home for the 1st Player
player1.goto(277, 242) #creating triangle
player1.pendown()
player1.right(180)
player1.begin_fill()
player1.color("red")
player1.circle(50, steps=3)
player1.penup()
player1.end_fill()
player1.goto(320, 88) #creating square
player1.pendown()
player1.begin_fill()
player1.color("violet")
player1.forward(85.6)
player1.right(90)
player1.forward(80)
player1.right(90)
player1.forward(85.6)
player1.right(90)
player1.forward(80)
player1.penup()
player1.left(90)
player1.end_fill()
player1.penup()
player1.goto(278.5,169) #Labelling Player 1 Home
player1.color("white")
player1.write("PLAYER 1", align = "center", font = ("Arial", 12, "bold"))
player1.color("red")
player1.goto(-200, 100)


# Finish line or Home for the Computer
computer.goto(277, 40) #creating triangle
computer.pendown()
computer.right(180)
computer.begin_fill()
computer.color("blue")
computer.circle(50, steps=3)
computer.penup()
computer.end_fill()
computer.goto(320, -115) #creating square
computer.pendown()
computer.begin_fill()
computer.color("pink")
computer.forward(85.6)
computer.right(90)
computer.forward(80)
computer.right(90)
computer.forward(85.6)
computer.right(90)
computer.forward(80)
computer.penup()
computer.left(90)
computer.end_fill()
computer.penup() #Labelling Computer Home
computer.goto(278.5,-35)
computer.color("white")
computer.write("COMPUTER", align = "center", font = ("Arial", 12, "bold"))
computer.color("blue")
computer.goto(-200, -100)

while player1.xcor() < 250 and computer.xcor() < 250: #looping until the players reach the 250 x coordinate or home
    # Prompt the player 1 to enter a choice
    print("****************************")
    print("Please Enter a Choice!")
    print("[1] Rock")
    print("[2] Paper")
    print("[3] Scissors")
    print("****************************")
    player1_choice = int(input("Player 1 choose: "))

    # computer randomly chooses
    computer_choice = random.randint(1, 3) #player 2 or computer randomly select choice
    print("Computer choose: ", computer_choice)

    # Determine the Winner for this round
    if player1_choice not in [1, 2, 3]:
        print("Invalid Choice! Please enter 1 for Rock, 2 for Paper, or 3 for Scissors")
    elif player1_choice == computer_choice:
        player1.forward(0)
        computer.forward(0)
        print("It's a Tie!")
    else:
        steps = 50  # Number of steps for a win
        if (
            (player1_choice == 1 and computer_choice == 3)
            or (player1_choice == 2 and computer_choice == 1)
            or (player1_choice == 3 and computer_choice == 2)
        ):
            player1.forward(steps)
            print("Player 1 Wins!")
        else:
            computer.forward(steps)
            print("Computer Wins!")

# Determine the overall winner
winner = " "
if player1.xcor() >= 250:
    winner = "Player 1 Wins!"
elif computer.xcor() >= 250:
    winner = "Computer Wins!"

# Display the winner on the screen
turtle.penup()
turtle.goto(0,0)
turtle.color("black")
turtle.write(winner, align = "center", font = ("Arial", 70, "bold"))

turtle.hideturtle()
turtle.done()





