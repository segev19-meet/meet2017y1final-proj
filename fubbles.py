import turtle
import random

turtle.tracer(1,0)
SIZE_X=800
SIZE_Y=500
turtle.tracer(1,)
turtle.setup(SIZE_X,SIZE_Y)

food_pos_list = []
food_stamp=[]

food=turtle.clone()
turtle.penup()
food.penup()
food.hideturtle()
turtle.hideturtle()
turtle.register_shape("meat.gif")
turtle.register_shape("pepper.gif")
turtle.register_shape("apple.gif")
turtle.register_shape("dairy_prod.gif")
turtle.register_shape("carbs.gif")

def make_food():
    min_x=-int(SIZE_X/2/55)+1
    max_x=int(SIZE_X/2/55)-1
    min_y=-int(SIZE_Y/2/55)+1
    max_y=int(SIZE_Y/2/55)-1
    food_x = random.randint(min_x,max_x)*55
    food_y = random.randint(0,max_y)*55
    food.goto(food_x,food_y)
    food_pos_list.append((food_x,food_y))
    
    food_type = random.randint(1,5)
    if food_type == 1:
        food.shape("apple.gif")
    elif food_type==2:
        food.shape("pepper.gif")
    elif food_type==3:
        food.shape("meat.gif")
    elif food_type==4:
        food.shape("dairy_prod.gif")
    else:
        food.shape("carbs.gif")

    if (food_x,food_y) not in food_pos_list[:-1]:   
        food.stamp()
        food_stamp.append(food.stamp())
        
    

    
for i in range(70):
    make_food()


ball=turtle.clone()


def ball_appear():
    
    kind=random.randint(1,5)
    print(kind)

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

    ball.goto(0,-200)
    ball.showturtle()

ball_appear()

score=0
def pop_shape(x,y):
    global ball
    global score
    ball.goto(x,y)
    hit=turtle.pos()
    if hit in food_pos_list:
        food_ind=food_pos_list.index(ball.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos_list.pop(food_ind)
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

    





