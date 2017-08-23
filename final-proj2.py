import turtle, random, time

turtle.tracer(9,0)
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
        
    

    
for i in range(70):
    make_food2()


face=turtle.clone()


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

        

    face.goto(0,-200)
    face.showturtle()

face_appear()

def compliments2():
    global score2
    point2.goto(-100,-200)
    point2.clear()
    point2.write(score2, font=("Ariel",20,"normal"))
    if score2==60:
        turtle.clear()
        point2.goto(-70,-50)
        point2.color("blue")
        point2.write("Keep going!",font=("Ariel",20,"normal"))
    elif score2==70:
        turtle.clear()
        point2.goto(-120,-50)
        point2.color("green")
        point2.write("You are doing great!",font=("Ariel",20,"normal"))
    elif score2==80:

        turtle.clear()
        point2.goto(-140,-50)
        point2.color("red")
        point2.write("Nice work!You're on fire!!!",font=("Ariel",20,"normal"))


score2=0
def pop_pics(x,y):
    global face
    global score2
    global kind2
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
                if type_shape2[pics_ind]==kind2:
                    #print("compliments")
                    pics.clearstamp(pics_stamps[pics_ind])
                    pics_pos_list.pop(pics_ind)
                    pics_stamps.pop(pics_ind)
                    type_shape2.pop(pics_ind)
                    face.hideturtle()
                    face.goto(0,-200)
                    face.showturtle()
                    score2+=5
                    compliments2()
                    face_appear()
                    
                else:
                    turtle.clear()
                    turtle.goto(-100,-50)
                    turtle.write("You lost!!!", font=("Ariel",40,"normal"))
                    time.sleep(1)
                    quit()
                    



        


turtle.onscreenclick(pop_pics)
turtle.listen()

    





