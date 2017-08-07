import turtle
SIZE_X=900
SIZE_Y=600

turtle.setup(SIZE_X, SIZE_Y)

turtle.clone()
turtle.goto(-50,0)
points_counter=30
def point_counter(): 
    global points_counter
    if points_counter==10:
        turtle.clear()
        turtle.color("blue")
        turtle.write("keep going!",font=("Ariel",26,"normal"))
    elif points_counter==20:
        turtle.clear()
        turtle.write("you are doing great!")
    elif points_counter==30:
        turtle.clear()
        turtle.write("nice work!,you on fire!!!",font=("Ariel",26,"normal"))
        
point_counter()

turtle.mainloop
