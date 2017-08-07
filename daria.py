import turtle


def pop_shape(x,y):
    turtle.goto(x,y)
    hit=turtle.pos()
    if hit in food_pos:
        food_ind=food_pos.index(turtle.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        turtle.hideturtle()
        turtle.goto(0,-200)
        start_again()
    else:
        quit()
        
turtle.onscreenclick(pop_shape)
turtle.listen()
