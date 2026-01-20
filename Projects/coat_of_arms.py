# Section 1 - Your code
from utils import *
set_background("Sunset2.gif")

s1 = create_sprite("Sunset3.gif", 100, 100)
s2 = create_sprite("light.gif", -100, 100)
s3 = create_sprite("dove1.gif", -100, -100)
s4 = create_sprite("dance.gif", 100, -100)

message1 = create_sprite("alien",-130,180)
message1.color("white")
message1.write("Ellie Epstein",font = ("comicbd.ttf", 30, "normal"))
message1.hideturtle()

message2 = create_sprite("alien",-200,-240)
message2.color("white")
message2.write("you are your home",font = ("comicbd.ttf", 30, "normal"))
message2.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()