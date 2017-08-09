import turtle
import random

turtle.penup()
turtle.goto(0,-200)
ball=turtle.clone()


for i in range(50):
    kind=random.randint(1,5)
    if kind==1:
        ball.shape("apple.gif")
    elif kind==2:
        ball.shape("pepper.gif")
    elif kind==3:
        ball.shape("meat.gif")
    elif kind==4:
        ball.shape("dairy_prod.gif")
    else:
        ball.shape("carbs.gif")

    



score=0
def pop_shape(x,y):
    global score
    ball.goto(x,y)
    hit=turtle.pos()
    if hit in food_pos:
        food_ind=food_pos.index(ball.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        ball.hideturtle()
        ball.goto(0,-200)
        ball.showturtle()
        score+=1
        start_again()
    else:
        quit()
        
turtle.onscreenclick(pop_shape)
turtle.listen()
