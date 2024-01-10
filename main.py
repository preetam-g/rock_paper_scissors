import turtle as tt
import shapes
import time

screen = tt.Screen()
screen.title("Rock Paper Scissors' Simulator")
screen.setup(width = shapes.WIDTH, height = shapes.HEIGHT)
screen.tracer(0)

#countdown
count = tt.Turtle()
count.hideturtle()
count.penup()
count.goto(0,0)
for no in range(3,0,-1):
    time.sleep(1)
    count.write(arg = f"Starting in {no}", font = shapes.FONT, align = "center")
    screen.update()
    count.clear()

time.sleep(1)
count.goto(0, (shapes.HEIGHT/2) - 50)
count.write("🪨 vs 📜 vs ✂️", font= shapes.FONT, align = "center")
#creating bits
while shapes.create_bits():
    s = shapes.Player()
    if s.shape() == shapes.scissors: shapes.all_scissors.append(s)
    elif s.shape() == shapes.stone: shapes.all_stones.append(s)
    else: shapes.all_papers.append(s)
    s.too_close()
    screen.update()
    time.sleep(0.1)

game_on = True
while game_on:

    time.sleep(0.02)

    for x in shapes.on_screen: 
        x.fd(shapes.MOVE)
        x.y_bounce()
        x.x_bounce()
        x.collision()
        x.too_close()
        screen.update()
    
    if shapes.got_winner():
        game_on = False

screen.exitonclick()