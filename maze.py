import turtle
import random

# Screen
wn = turtle.Screen()
wn.title("Maze game by Ana Majstor")
wn.setup(width=700, height=700)
wn.bgcolor("black")
wn.tracer(0)

# Add pictures
wn.register_shape("ghost.gif")
wn.register_shape("coins.gif")
wn.register_shape("wall.gif")
wn.register_shape("rightwizard.gif")
wn.register_shape("leftwizard.gif")
wn.register_shape("splash.gif")
wn.register_shape("gameover.gif")

# Create Pen which draws the maze


class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("wall.gif")
        self.penup()
        self.speed(0)


class Score(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("white")
        self.penup()
        self.speed(0)
        self.goto(0, 300)
        self.write("Player has 0 gold.", align="center",
                   font=("Courier", 24, "bold"))


class GameWin(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("white")
        self.penup()
        self.speed(0)
        self.goto(0, 0)
        self.write("You Won!", align="center",
                   font=("Courier", 24, "bold"))


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("rightwizard.gif")
        # self.color("green")
        self.penup()
        self.speed(0)
        self.gold = 0

    def go_down(self):
        player_xcoord = self.xcor()
        player_ycoord = self.ycor()-24
        if (player_xcoord, player_ycoord) not in walls:
            self.goto(player_xcoord, player_ycoord)

    def go_up(self):
        player_xcoord = self.xcor()
        player_ycoord = self.ycor()+24
        if (player_xcoord, player_ycoord) not in walls:
            self.goto(player_xcoord, player_ycoord)

    def go_left(self):
        self.shape("leftwizard.gif")
        player_xcoord = self.xcor()-24
        player_ycoord = self.ycor()
        if (player_xcoord, player_ycoord) not in walls:
            self.goto(player_xcoord, player_ycoord)

    def go_right(self):
        self.shape("rightwizard.gif")
        player_xcoord = self.xcor()+24
        player_ycoord = self.ycor()
        if (player_xcoord, player_ycoord) not in walls:
            self.goto(player_xcoord, player_ycoord)

    def isColission(self, other):
        if self.xcor() == other.xcor() and self.ycor() == other.ycor():
            return True
        else:
            return False

    def dissapear(self):
        self.goto(2000, 2000)
        self.hideturtle()
        


class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("coins.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def spawn(self):
        new_treasure_xcor = random.randrange(-288, 288, 24)
        new_treasure_ycor = random.randrange(-288, 288, 24)
        if (new_treasure_xcor, new_treasure_ycor) not in walls:
            self.goto(new_treasure_xcor, new_treasure_ycor)
            
        else:
            return self.spawn()

    def dissapear(self):
        self.goto(2000, 2000)
        self.clear()
        


class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("ghost.gif")
        self.color("red")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])

    # Is the enemy close to the player
    def isClose(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        if a < 72 or b < 72:
            return True
        else:
            return False

    # Move the enemy
    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
        elif self.direction == "right":
            dx = 24
            dy = 0
        else:
            dx = 0
            dy = 0

        # If the enemy is close to the player to towords the player
        if self.isClose(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            if player.xcor() > self.xcor():
                self.direction = "right"
            if player.ycor() < self.ycor():
                self.direction = "down"
            if player.ycor() > self.ycor():
                self.direction = "up"

        # Calculate the spot to move to
        move_to_x = self.xcor()+dx
        move_to_y = self.ycor()+dy
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            self.direction = random.choice(["up", "down", "left", "right"])
        # set timer to move next time
        turtle.ontimer(self.move, random.randint(100, 300))

    def dissapear(self):
        self.goto(2000, 2000)
        self.hideturtle()
        



levels = [""]
walls = []
treasures = []
enemies = []

level1 = ["XXXXXXXXXXXXXXXXXXXXXXXXX",
          "XXP  XXXXXXXXXX      XXXX",
          "XXX  XXXXXXXE   XXXX XXXX",
          "XXXX   XXXXX  XXXXXX    X",
          "X    XXXXXX  XXXXXXXXXX X",
          "X   XXXXX   XXXXXXX   XXX",
          "XX    XXXX XXXXXXXX   XXX",
          "XX  XXXXXX   XXXXXX XXXXX",
          "XXX  T  XX XXXXX    XXXXX",
          "XXX  XXXXX   XXXXX XXXXXX",
          "XXXE       XXXXXX      XX",
          "XXXXXX   XXXXXXXXX  XX XX",
          "XXXXXX  XXXXXXXXXXXX   XX",
          "XX  T     E   XXXXXXX XXX",
          "XXXXXXXXXX   XXXXX    XXX",
          "XXXX         X        XXX",
          "XX      XXXXXXXXX      XX",
          "XXXXX   XXXXXXXXXXXXX XXX",
          "XXXXX    T       XXX   XX",
          "X      XX   XXXXXXXXXX XX",
          "X XXXXX  E      XXXX   XX",
          "X   XXXXX  XXXXXXX   XXXX",
          "XX XXXXXX  T        XXXXX",
          "XX   XXXXXXX    XXXXXXXXX",
          "XXXXXXXXXXXXXXXXXXXXXXXXX"]


# add level to the list of levels
levels.append(level1)

pen = Pen()
player = Player()
score = Score()


def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            # Get the character at each x,y coordinate
            character = level[y][x]
            screen_x = -288+(x*24)
            screen_y = 288-(y*24)
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                pen.shape("wall.gif")
                walls.append((screen_x, screen_y))
            if character == "P":
                player.goto(screen_x, screen_y)
            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))
            if character == "E":
                enemies.append(Enemy(screen_x, screen_y))
                


def startGame():
    wn.bgpic("groundbg.gif")
    global game_state
    game_state = "game"
    setup_maze(levels[1])
    for enemy in enemies:
        turtle.ontimer(enemy.move, t=250)
# RESET THE GAME
# Set score to 0
# Move the player back to the starting position


def gameOver():
    pen.clear()
    wn.bgpic("gameover.gif")
    score.clear()
    
    player.shape("circle")
    player.color("blue")
    for t in treasures:
        t.shape("circle")
        t.color("green")
    for e in enemies:
        e.shape("circle")
        e.color("red")
   

    turtle.done()


# Keyboard binding
wn.listen()
wn.onkeypress(player.go_left, "Left")
wn.onkeypress(player.go_right, "Right")
wn.onkeypress(player.go_up, "Up")
wn.onkeypress(player.go_down, "Down")
wn.onkeypress(startGame, "s")
# Create level setup function
game_state = "splash"


while True:
    
    if game_state == "splash":
        wn.bgpic("splash.gif")

    elif game_state == "game":

        for treasure in treasures:
            if player.isColission(treasure):
                player.gold += treasure.gold
                score.clear()
                score.write(f"Player has {player.gold} gold.", align="center",
                            font=("Courier", 24, "bold"))
                treasure.spawn()
                if player.gold > 1000:
                    game_state = "gameover"
                    

        for enemy in enemies:
            if player.isColission(enemy):
                player.gold -= 1
                score.clear()
                score.write(f"Player has {player.gold} gold.", align="center",
                            font=("Courier", 24, "bold"))
                if player.gold > 1000:
                    game_state = "gameover"
                   
    elif game_state == "gameover":
        gameOver()

    wn.update()
