# this file consists of all the variables, classes with methods that are being used in the main.py to run the simulation

import turtle as tt
import random
scissors = "scissors.gif"
paper = "paper.gif"
stone = "stone.gif"

tt.register_shape("scissors.gif")
tt.register_shape("paper.gif")
tt.register_shape("stone.gif")

shapes = [scissors, paper, stone]
HEIGHT = 600
WIDTH = int(0.9*HEIGHT)
BUFF = int(WIDTH/10)
BITS = int(HEIGHT*WIDTH/20000)
MOVE = min(int(HEIGHT/150),3)
BACK = MOVE+3
FONT = ("Baskiville", 20, "normal")

on_screen = []
all_scissors = []
all_papers = []
all_stones = []

class Player(tt.Turtle):

    def __init__(self):
        super().__init__()
        self.shape(random.choice(shapes))
        self.speed(3)
        self.penup()
        self.goto( (random.randint(-(WIDTH/2 - BUFF)+30, WIDTH/2 - BUFF-30), random.randint(-(HEIGHT/2 - BUFF)+30, HEIGHT/2 - BUFF)-30) )
        self.setheading(random.randrange(0,360,5))
        on_screen.append(self)
    
    def y_bounce(self):
        if self.ycor() >= (HEIGHT/2 - BUFF) or self.ycor() <= -(HEIGHT/2 - BUFF):
            self.bk(BACK+5)
            h = self.heading()
            self.seth(h+135)
    
    def x_bounce(self):
        if self.xcor() >= (WIDTH/2 - BUFF) or self.xcor() <= -(WIDTH/2 - BUFF):
            self.bk(BACK+5)
            h = self.heading()
            self.seth(h+135)

    def collision(self):
        for s in on_screen:
            if abs(self.xcor() - s.xcor()) <= 10 and abs(self.ycor() - s.ycor()) <= 10 and self != s:
                
                a = self.heading()
                b = s.heading()
                
                self.back(BACK)
                s.back(BACK)

                if a != b: 

                    self.seth(b)
                    s.seth(a)

                elif abs(a-b) <= 10: 
                    
                    self.seth(a-45)
                    s.seth(b+45)
                
                self.shape_change(s)

    
    def too_close(self):
        for s in on_screen:
            if abs(self.xcor() - s.xcor()) <= 8 and abs(self.ycor() - s.ycor()) <= 8 and self != s:
                
                self.seth(0)
                self.fd(30)

                s.seth(90)
                s.fd(30)

    
    def shape_change(self,x):
        shape_a = self.shape()
        shape_b = x.shape()

        if shape_a == scissors and shape_b == stone: 
            self.shape(stone)
            all_scissors.remove(self)
            all_stones.append(self)
        elif shape_a == paper and shape_b == scissors: 
            self.shape(scissors)
            all_papers.remove(self)
            all_scissors.append(self)
        elif shape_a == stone and shape_b == paper: 
            self.shape(paper)
            all_stones.remove(self)
            all_papers.append(self)

        if shape_b == scissors and shape_a == stone: 
            x.shape(stone)
            all_scissors.remove(x)
            all_stones.append(x)
        elif shape_b == paper and shape_a == scissors: 
            x.shape(scissors)
            all_papers.remove(x)
            all_scissors.append(x)
        elif shape_b == stone and shape_a == paper: 
            x.shape(paper)
            all_stones.remove(x)
            all_papers.append(x)


def create_bits():
    if len(all_scissors) > BITS or len(all_stones) > BITS or len(all_papers) > BITS or len(on_screen) > 2*BITS: return False
    else: return True

winner = tt.Turtle()
winner.hideturtle()
def got_winner():
    if len(all_stones) == len(on_screen) or len(all_papers) == 0:
        win = "🪨 won"
        winner.write(arg = win, align = "center", font = FONT)
        return True
    elif len(all_papers) == len(on_screen) or len(all_scissors) == 0:
        win = "📜 won"
        winner.write(arg = win, align = "center", font = FONT)
        return True
    elif len(all_scissors) == len(on_screen) or len(all_stones) == 0:
        win = "✂️ won"
        winner.write(arg = win, align = "center", font = FONT)
        return True
    else: return False
        
