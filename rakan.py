import turtle
import random#we will need this later in the final-proj
SIZE_X=800
SIZE_Y=500









turtle.penup()
turtle.register_shape("meat.gif")
food = turtle.clone()
food.shape("meat.gif")
food.goto(100,100)


turtle.register_shape("pepper.gif")
food = turtle.clone()
food.shape("pepper.gif")
food.goto(100,150)


turtle.register_shape("apple.gif")
food = turtle.clone()
food.shape("apple.gif")
food.goto(150,100)


turtle.register_shape("dairy_prod.gif")
food = turtle.clone()
food.shape("dairy_prod.gif")
food.goto(120,100)



turtle.register_shape("carbs.gif")
food = turtle.clone()
food.shape("carbs.gif")
food.goto(150,150)



#write code that will set some_shape = to a random filename


    
def make_food():
    min_x=-int(SIZE_X/2)+1
    max_x=int(SIZE_X/2)-1
    min_y=-int(SIZE_Y/2)-1
    max_y=int(SIZE_Y/2)+1
    food_x = random.randint(0,max_x)
    food_y = random.randint(-100,max_y)
    food.goto(food_x,food_y)
    
    food_type = random.randint(1,5)
    if food_type == 1:
        food.shape('apple.gif')
    elif food_type==2:
        food.shape('pepper.gif')
    elif food_type==3:
        food.shape('meat.gif')
    elif food_type==4:
        food.shape('dairy_prod.gif')
    else:
        food.shape('carbs.gif')
        

        
    food.stamp()
make_food()

    









