import turtle, time, random
from utils import *

# Section 1 - Variables
x1 = -200
y1 = 200
x2 = -200
y2 = 100
x3 = -200
y3 = 0
x4 = -200
y4 = -100


# Section 2 - Setup
set_background("castle")
bob = create_sprite("boby.gif",x1,y1)
kevin = create_sprite("kevin.gif",x2,y2)
gerald = create_sprite("gerald.gif",x3,y3)
dave = create_sprite("dave.gif",x4,y4)


# # Section 3 - Racing
# Bob is the fastest because he moves at 16 speed, Kevin is second fastest because he moves at 13 speed, Gerald gets last place and moves really slow at 5 speed, Dave just sticks in the middle of the pack and moves at 10 speed
for i in range(30):
     x1 += 16
     x2 += 13
     x3 += 5
     x4 += 10

     bob.goto(x1, y1)
     kevin.goto(x2, y2)
     gerald.goto(x3, y3)
     dave.goto(x4, y4)

     window.update()
     time.sleep(0.1)


# # Section 4 - Winner

for i in range(3):
    print("Hello!")
print("I hope you liked the minion race!")
print("")
print("Who do you think won?")
print("Bob in lane 1")
print("Kevin in lane 2")
print("Gerald in lane 3")
print("Or Dave in lane 4?")
name = input("")
print(f"{name}??????")
print("")

if x1 >= x2 and x1 >= x3 and x1 >= x4:
     print("Bob won!")
     if name == 'Bob':
          print("Good job guessing correctly!")
     else:
          print("I hope you are still happy for Bob even though you guessed wrong!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
     print("Kevin won!")
     if name == 'Kevin':
          print("Good job guessing correctly!")
     else:
          print("I hope you are still happy for Kevin even though you guessed wrong!")
elif x3 >= x2 and x3 >= x1 and x3 >= x4:
     print("Gerald won!")
     if name == 'Gerald':
          print("Good job guessing correctly!")
     else:
          print("I hope you are still happy for Gerald even though you guessed wrong!")
elif x4 >= x2 and x4 >= x3 and x4 >= x1:
     print("Dave won!")
     if name == 'Dave':
          print("Good job guessing correctly!")
     else:
          print("I hope you are still happy for Dave even though you guessed wrong!")

turtle.exitonclick()