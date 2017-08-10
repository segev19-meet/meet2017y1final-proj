import turtle
import random
turtle.tracer(1,0)



turtle.bgcolor("light blue")
turtle.penup()
turtle.goto(-140,-150)
turtle.pendown()
turtle.write("Fubbles",font=("Ariel",50,"normal"))



turtle.penup()
SIZE_X=800
SIZE_Y=500
turtle.tracer(1,)
turtle.setup(SIZE_X,SIZE_Y)
food_pos_list = []
food_stamps=[]
type_shape=[]
pics_pos_list = []
pics_stamps=[]
type_shape2=[]
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
turtle.register_shape("meat2.gif")
turtle.register_shape("pepper.gif")
turtle.register_shape("apple.gif")
turtle.register_shape("dairy_prod.gif")
turtle.register_shape("carbs.gif")
turtle.register_shape("amir.gif")
turtle.register_shape("alex.gif")
turtle.register_shape("doudou.gif")
turtle.register_shape("key1.gif")
turtle.register_shape("lorenzo.gif")
turtle.register_shape("yun.gif")
turtle.register_shape("abdalla.gif")
turtle.register_shape("musa.gif")

def make_food():
    min_x=-int(SIZE_X/2/55)+1
    max_x=int(SIZE_X/2/55)-1
    min_y=-int(SIZE_Y/2/55)+1
    max_y=int(SIZE_Y/2/55)-1
    food_x = random.randint(min_x,max_x)*55
    food_y = random.randint(0,max_y)*55
    food.goto(food_x,food_y)
    
    
    food_type = random.randint(1,5)
    if food_type == 1:
        food.shape("apple.gif")
    elif food_type==2:
        food.shape("pepper.gif")
    elif food_type==3:
        food.shape("meat2.gif")
    elif food_type==4:
        food.shape("dairy_prod.gif")
    else:
        food.shape("carbs.gif")
    

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
    kind=random.randint(1,5)
    #print(kind)

    if kind==1:
        ball.shape("apple.gif")
    elif kind==2:
        ball.shape("pepper.gif")
    elif kind==3:
        ball.shape("meat2.gif")
    elif kind==4:
        ball.shape("dairy_prod.gif")
    else:
        ball.shape("carbs.gif")

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
s2nd_level = False
def pop_shape(x,y):
    global ball, score, kind, s2nd_level
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
    if len(food_stamps) == 0:
        s2nd_level = True
########################################################

point2=turtle.clone()
turtle.hideturtle()
point2.penup()
point2.hideturtle()
point2.goto(-300,-270)



pics=turtle.clone()
turtle.penup()
pics.penup()
pics.hideturtle()
turtle.hideturtle()
turtle.register_shape("amir.gif")
turtle.register_shape("alex.gif")
turtle.register_shape("doudou.gif")
turtle.register_shape("key1.gif")
turtle.register_shape("lorenzo.gif")
turtle.register_shape("yun.gif")
turtle.register_shape("abdalla.gif")
turtle.register_shape("musa.gif")
def make_food2():
    min_xa=-int(SIZE_X/2/55)+1
    max_xa=int(SIZE_X/2/55)-1
    min_ya=-int(SIZE_Y/2/55)+1
    max_ya=int(SIZE_Y/2/55)-1
    pics_x = random.randint(min_xa,max_xa)*55
    pics_y = random.randint(0,max_ya)*55
    pics.goto(pics_x,pics_y)
    
    
    pics_type = random.randint(1,8)
    if  pics_type == 1:
        pics.shape("amir.gif")
    elif pics_type==2:
        pics.shape("alex.gif")
    elif pics_type==3:
        pics.shape("doudou.gif")
    elif pics_type==4:
        pics.shape("key1.gif")
    elif pics_type==5:
        pics.shape("lorenzo.gif")
    elif pics_type==6:
         pics.shape("yun.gif")
    elif pics_type==7:
        pics.shape("abdalla.gif")
    elif pics_type==8:
        pics.shape("musa.gif")
    

    if (pics_x,pics_y) not in pics_pos_list:   
        #food.stamp()
        pics_pos_list.append((pics_x,pics_y))
        pics_stamps.append(pics.stamp())
        type_shape2.append(pics_type)
        
    

    


face=turtle.clone()
kind2 = 1

def face_appear():
    global kind2
    kind2=random.randint(1,8)

    if   kind2==1:
        face.shape("amir.gif")
    elif kind2==2:
        face.shape("alex.gif")
    elif kind2==3:
        face.shape("doudou.gif")
    elif kind2==4:
        face.shape("key1.gif")
    elif kind2==5:
        face.shape("lorenzo.gif")
    elif kind2==6:
        face.shape("yun.gif")
    elif kind2==7:
        face.shape("abdalla.gif")
    elif kind2==8:
        face.shape("musa.gif")
    print(kind2)
        

    face.goto(0,-200)
    face.showturtle()

def pop_pics(x,y):
    global face, score, kind2
    face.goto(x,y)
    if (face.pos()[0]>200 and face.pos()[0]<350 and face.pos()[1]<(-100) and face.pos()[1]>(-200)):
        face_appear()
    else:
        target=turtle.pos()
        templist2 = pics_pos_list[:]
        for current in templist2:
            fax = current[0]
            fay = current[1]
            distance2 = ((x-fax)**2+(y-fay)**2)**0.5
            pics_ind=pics_pos_list.index(current)
            if distance2 <= 25:
                if type_shape2[pics_ind]== kind2:
                    #print("compliments")
                    pics.clearstamp(pics_stamps[pics_ind])
                    pics_pos_list.pop(pics_ind)
                    pics_stamps.pop(pics_ind)
                    type_shape2.pop(pics_ind)
                    face.hideturtle()
                    face.goto(0,-200)
                    face.showturtle()
                    score+=5
                    compliments()
                    face_appear()
                    
                else:
                    turtle.clear()
                    turtle.goto(-100,-50)
                    turtle.write("You lost!!!", font=("Ariel",40,"normal"))
##                    turtle.sleep(1)
##                    quit()
###############################



level2_1st_time = False

def check_level(x,y):
    global level2_1st_time
    if s2nd_level:
        if not(level2_1st_time):
            for i in range(70):
                make_food2()
            level2_1st_time = True
            face_appear()
        else:
            pop_pics(x,y)
    else:
        pop_shape(x,y)

                    
turtle.onscreenclick(check_level)
turtle.listen()

    





