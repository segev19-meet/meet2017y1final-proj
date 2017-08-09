import turtle
SIZE_X=900
SIZE_Y=600

turtle.setup(SIZE_X, SIZE_Y)

points=turtle.clone()
turtle.hideturtle()
points.penup()
points.hideturtle()
points.goto(-300,-270)
score=20
def compliments():
    global score
    points.write(score, font=("Ariel",20,"normal"))
    if score==10:
        turtle.clear()
        points.goto(-70,-50)
        points.color("blue")
        points.write("keep going!",font=("Ariel",20,"normal"))
    elif score==20:
        turtle.clear()
        points.goto(-120,-50)
        points.color("green")
        points.write("you are doing great!",font=("Ariel",20,"normal"))
    elif score==30:
        turtle.clear()
        points.goto(-140,-50)
        points.color("red")
        points.write("nice work!you're on fire!!!",font=("Ariel",20,"normal"))
        
compliments()









turtle.mainloop()


