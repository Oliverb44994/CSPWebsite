#import turtle module
import turtle as trtl
wn = trtl.Screen()
wn.tracer(0,0)
#create turtle object
painter = trtl.Turtle()




#make background grid
painter.speed(1000)
painter.pensize(2)
painter.hideturtle()
painter.penup()
i=0
c=0
while (i < 13):
  painter.goto(-300,300-c)
  painter.pendown()
  painter.setheading(0)
  painter.forward(600)
  painter.penup()
  i=i+1
  c=c+50




a=0
b=0
while (a<13):
  painter.goto(-300+b,-300)
  painter.pendown()
  painter.setheading(90)
  painter.forward(600)
  painter.penup()
  a=a+1
  b=b+50




#start location
painter.goto(-350,-275)
painter.pendown()
painter.setheading(0)
painter.forward(40)
painter.setheading(225)
painter.forward(15)
painter.goto(-310,-275)
painter.setheading(135)
painter.forward(15)




wn = trtl.Screen()
enemy1 = "ene1.GIF"
wn.addshape(enemy1)
enemy2 = "ene2.GIF"
wn.addshape(enemy2)
enemy3 = "ene3.GIF"
wn.addshape(enemy3)
enemy4 = "ene4.GIF"
wn.addshape(enemy4)
enemy5 = "ene5.GIF"
wn.addshape(enemy5)
enemy6 = "ene6.GIF"
wn.addshape(enemy6)
enemy7 = "ene7.GIF"
wn.addshape(enemy7)
enemy8 = "ene8.GIF"
wn.addshape(enemy8)
enemy9 = "ene9.GIF"
wn.addshape(enemy9)
enemy10 = "ene10.GIF"
wn.addshape(enemy10)




enemies = []
enemies1 = []
enemies2 = []
enemy_shapes = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8, enemy9, enemy10]
for s in enemy_shapes:
  t = trtl.Turtle(shape=s)
  t.speed(8)
  enemies.append(t)
for s in enemy_shapes:
  t = trtl.Turtle(shape=s)
  t.speed(8)
  enemies1.append(t)
for s in enemy_shapes:
  t = trtl.Turtle(shape=s)
  t.speed(8)
  enemies2.append(t)




startx=-225
starty=-225
i=0
for t in enemies:
  t.penup()
  t.goto(startx, starty)
  if (i%2 == 0):
    startx = startx + 100
    starty = starty- 50
  else:
    starty = starty + 150
    startx = startx - 50
  i=i+1




stax=225
stay=-225
u=0
for t in enemies1:
  t.penup()
  t.goto(stax, stay)
  if (u%2 == 0):
    stax = stax - 100
  else:
    stay = stay + 100
  u=u+1




starx=-225
stary=225
e=0
for t in enemies2:
  t.penup()
  t.goto(starx, stary)
  if (e < 4):
    starx = starx + 100
  else:
    stary = stary - 100
  e=e+1




enemy4 = trtl.Turtle(shape=enemy4)
enemy4.penup()
enemy4.speed(8)
enemy4.goto(-175,275)
enemy6 = trtl.Turtle(shape=enemy6)
enemy6.penup()
enemy6.speed(8)
enemy6.goto(25,275)
enemy8 = trtl.Turtle(shape=enemy8)
enemy8.penup()
enemy8.speed(8)
enemy8.goto(275,125)
enemy9 = trtl.Turtle(shape=enemy9)
enemy9.penup()
enemy9.speed(8)
enemy9.goto(275,-25)




#cheese
cheese = trtl.Turtle()
def makecheese():
    global cheese
    cheese.penup()
    cheese.pencolor("orange")
    cheese.fillcolor("yellow")
    cheese.goto(260,275)
    cheese.setheading(0)
    cheese.pendown()
    cheese.begin_fill()
    cheese.forward(30)
    cheese.setheading(135)
    cheese.forward(25)
    cheese.setheading(200)
    cheese.circle(18, 75)
    cheese.setheading(270)
    cheese.forward(15)
    cheese.setheading(0)
    cheese.forward(30)
    cheese.setheading(90)
    cheese.forward(15)
    cheese.end_fill()
    cheese.penup()
    cheese.goto(285,270)
    cheese.pendown()
    cheese.circle(2)
    cheese.penup()
    cheese.goto(275,265)
    cheese.pendown()
    cheese.circle(2)
    cheese.penup()
    cheese.goto(260,270)
    cheese.pendown()
    cheese.setheading(320)
    cheese.circle(3, 270)
    cheese.penup()
    cheese.goto(267,288)
    cheese.pendown()
    cheese.setheading(280)
    cheese.circle(3, 210)
    cheese.penup()
    cheese.goto(280,275)
    cheese.pendown()
    cheese.setheading(90)
    cheese.circle(3, 180)
   
makecheese()




def uncheese():
   global cheese
   for i in range(40):
      cheese.undo()










#setting up mouse
mouse_image = "Mouse.gif"
wn.addshape(mouse_image)
mouse = trtl.Turtle(shape=mouse_image)


mouse.color("black")
mouse.pencolor("black")
mouse.penup()
mouse.setheading(90)
mouse.goto(-325, -275)
mouse.speed(1)
mouse.color('black')  
mouse.speed(0)  
mouse.width(1)  
 
#initializing move variable
move = 0
mouse.right(90)
for move in range(3800):
    #cosntant speed for the mouse
    mouse.forward(0.5)
  #if statements to say when to turn
    if (move == 300):
        mouse.left(90)
    if (move == 500):
        mouse.left(90)
    if (move == 700):
       mouse.right(90)
    if (move == 1100):
       mouse.right(90)
    if (move == 1600):
         mouse.left(90)
    if (move == 1700):
       mouse.right(90)
    if (move == 1800):
       mouse.left(90)
    if (move == 2000):
       mouse.right(90)  
    if (move == 2200):
       mouse.right(90)
    if (move == 2600):
       mouse.left(90)
    if (move == 2800):
       mouse.left(90)
    if (move == 3200):
       mouse.right(90)
    if (move == 3300):
       mouse.left(90)
    if (move == 3500):
       mouse.left(90)
       uncheese()
    if (move == 3700):
       mouse.left(90)
    if (move == 3800):
       #used to hide turtle after reaching monster
       mouse.hideturtle()
   
    wn.update()




if (move == 3500):
  painter.pencolor("black")
  painter.penup()
  painter.fillcolor("white")
  painter.goto(250,250)
  painter.begin_fill()
  painter.setheading(0)
  painter.forward(50)
  painter.setheading(90)
  painter.forward(50)
  painter.setheading(180)
  painter.forward(50)
  painter.setheading(270)
  painter.forward(50)
  painter.end_fill()


#create screen object and make it persist


wn.mainloop()
