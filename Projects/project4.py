import turtle, time, random
from utils import *

x4 = -200
y4 = -100


# Section 1 - setup
set_background("alpine1.gif")
goat = create_sprite("goat.gif",x4,y4)


# the goal of the game is to keep the fast goat alive. He can only do well a certain way without getting diabeties.

age = 0
happiness = 50
cookies = 0
milks = 0
grown = False

if happiness >= 80:
    set_image(goat,"goatbig.gif")

# Section 2 - controls
# makes cookies appear on the screen to make the goat become fed
def make_cookie():
    global cookies
    cookies += 1
    x = random.randint (-200,200)
    y = -100
    c1 = create_sprite ("cookie.gif",x,y)
    time.sleep (0.2)
    c1.hideturtle()
     
window.onkeypress(make_cookie, "c")

# makes a milk on the screen and adds or subtracts from other points 
def make_milk():
    global milks, happiness, cookies
    milks += 1
    happiness += 30
    cookies -= 3
    x = random.randint (-200,200)
    y = -100
    m1 = create_sprite ("milk.gif",x,y)
    time.sleep (0.2)
    m1.hideturtle()
window.onkeypress(make_milk, "m")

def increase_age():
    global age
    age += 1
    








# Section 3 - game loop
window.listen()

message1 = create_sprite("alien",-200,160)
message1.color("black")
message1.hideturtle()
for i in range(1000000000):
    message1.clear()
    message1.write(f"age: {age}\nhappiness: {happiness}\ncookies: {cookies}\nmilks: {milks}", font=("arial", 20, "normal"))
    
    if i % 50 == 0:
        x2 = random.randint(-200, 200)
        goat.goto(x2,y4)
    
    


    time.sleep(0.01)
    if i % 200 == 0:
        cookies += 20
    if i % 200 == 0:
        milks += 1
    if i % 400 == 0:
        age += 1
    if i % 200 == 0:
        happiness -= 10
    window.update()

    if happiness == 0:
        break
    if cookies >= 500:
        break
print("Game over!")
