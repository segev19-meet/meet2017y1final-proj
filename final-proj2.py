import turtle
import random

turtle.tracer(1,0)
turtle.penup()
SIZE_X=800
SIZE_Y=500
turtle.tracer(1,)
turtle.setup(SIZE_X,SIZE_Y)
food_pos_list = []
food_stamps=[]
type_shape=[]
box=turtle.clone()
box.goto(200,-100)
box.pendown()
box.goto(200,-200)
box.goto(350,-200)
box.goto(350,-100)
box.goto(200,-100)
box.up()
box.goto(210,-160)
box.write("Donation",font=("Ariel",20))
box.ht()
points=turtle.clone()
turtle.hideturtle()
points.penup()
points.hideturtle()
points.goto(-300,-270)



food=turtle.clone()
turtle.penup()
food.penup()
food.hideturtle()
turtle.hideturtle()
turtle.register_shape("amir.gif")
turtle.register_shape("alex.gif")
turtle.register_shape("doudou.gif")
turtle.register_shape("key1.gif")
turtle.register_shape("lorenzo.gif")
turtle.register_shape("yun.gif")
turtle.register_shape("abdalla.gif")

def make_food():
    min_x=-int(SIZE_X/2/55)+1
    max_x=int(SIZE_X/2/55)-1
    min_y=-int(SIZE_Y/2/55)+1
    max_y=int(SIZE_Y/2/55)-1
    food_x = random.randint(min_x,max_x)*55
    food_y = random.randint(0,max_y)*55
    food.goto(food_x,food_y)
    
    
    food_type = random.randint(1,7)
    if  food_type == 1:
         food.shape("amir.gif")
    elif food_type==2:
        food.shape("alex.gif")
    elif food_type==3:
        food.shape("doudou.gif")
    elif food_type==4:
         food.shape("key1.gif")
    elif food_type==5:
        food.shape("lorenzo.gif")
    elif food_type==6:
         food.shape("yun.gif")
    elif food_type==7:
        food.shape("abdalla.gif")
    

    if (food_x,food_y) not in food_pos_list:   
        #food.stamp()
        food_pos_list.append((food_x,food_y))
        food_stamps.append(food.stamp())
        type_shape.append(food_type)
        
    

    
for i in range(70):
    make_food()


ball=turtle.clone()


def ball_appear():
    global kind
    kind=random.randint(1,7)
    print(kind)

    if   kind==1:
        ball.shape("amir.gif")
    elif kind==2:
        ball.shape("alex.gif")
    elif kind==3:
        ball.shape("doudou.gif")
    elif kind==4:
        ball.shape("key1.gif")
    elif kind==5:
        ball.shape("lorenzo.gif")

    elif kind==6:
        ball.shape("yun.gif")
    elif kind==7:
        ball.shape("abdalla.gif")

        

    ball.goto(0,-200)
    ball.showturtle()

ball_appear()

def compliments():
    global score
    points.goto(-100,-200)
    points.clear()
    points.write(score, font=("Ariel",20,"normal"))
    if score==60:
        turtle.clear()
        points.goto(-70,-50)
        points.color("blue")
        points.write("Keep going!",font=("Ariel",20,"normal"))
    elif score==70:
        turtle.clear()
        points.goto(-120,-50)
        points.color("green")
        points.write("You are doing great!",font=("Ariel",20,"normal"))
    elif score==80:
        turtle.clear()
        points.goto(-140,-50)
        points.color("red")
        points.write("Nice work!You're on fire!!!",font=("Ariel",20,"normal"))

score=0
def pop_shape(x,y):
    global ball
    global score
    global kind
    ball.goto(x,y)
    if (ball.pos()[0]>200 and ball.pos()[0]<350 and ball.pos()[1]<(-100) and ball.pos()[1]>(-200)):
        ball_appear()
    else:
        hit=turtle.pos()
        templist = food_pos_list[:]
        for current in templist:
            fx = current[0]
            fy = current[1]
            distance = ((x-fx)**2+(y-fy)**2)**0.5
            food_ind=food_pos_list.index(current)
            if distance <= 25:
                if type_shape[food_ind]==kind:
                    #print("compliments")
                    food.clearstamp(food_stamps[food_ind])
                    food_pos_list.pop(food_ind)
                    food_stamps.pop(food_ind)
                    type_shape.pop(food_ind)
                    ball.hideturtle()
                    ball.goto(0,-200)
                    ball.showturtle()
                    score+=5
                    compliments()
                    ball_appear()
                    
                else:
                    turtle.clear()
                    turtle.write("You lost!!!", font="100")

                    quit()



        


turtle.onscreenclick(pop_shape)
turtle.listen()

    





