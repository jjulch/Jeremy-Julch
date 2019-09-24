#Drawing with turtle
#24SEPT2019
#CTI-110 P2HW2- Turtle Graphic
#Jeremy Julch
#


import turtle
 
t = turtle.Turtle()
for i in range(3):
  t.penup()
  t.goto(i*110, 0)
  t.pendown()
  t.circle(50)
 
for i in range(1, 4, 2):
  t.penup()
  t.goto(i*55, -50)
  t.pendown()
  t.circle(50)


