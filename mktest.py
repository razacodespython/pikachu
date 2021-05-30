import turtle

t = turtle.Turtle()

import turtle
tn = turtle.Screen()
tn.bgpic("pikachu.gif")

def get_mouse_click_coor(x, y):
    print(str("t.goto(") + str(int(x)) +"," + str(y) + str(")"))
#print(x,y)
turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()

turtle.done()