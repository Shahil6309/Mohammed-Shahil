from turtle import *
import time
time.time()
t=Turtle()
wn=Screen()
wn.title("analog clock")
wn.bgcolor("black")
wn.setup(600,600)
t.speed(1)
t.pensize(3)
t.hideturtle()
wn.tracer(0)

def draw_clock(h,m,s,t):
    t.penup()
    t.goto(0,210)
    t.setheading(180)
    t.pencolor("green")
    t.pendown()
    t.circle(210)

    t.penup()
    t.goto(0,0)
    t.setheading(90)
    for _ in range(12):
        t.forward(170)
        t.pendown()
        t.fd(40)
        t.penup()
        t.goto(0,0)
        t.right(30)
    
    t.penup()
    t.goto(0,0)
    t.setheading(90)
    for _ in range(60):
        t.forward(200)
        t.pendown()
        t.fd(10)
        t.penup()
        t.goto(0,0)
        t.right(6)

    t.pu()
    t.goto(0,0)
    t.pencolor("red")
    t.setheading(90)
    angle=(h/12)*360
    t.rt(angle)
    t.pendown()
    t.fd(80)

    t.pu()
    t.goto(0,0)
    t.pencolor("blue")
    t.setheading(90)
    angle=(m/60)*360
    t.rt(angle)
    t.pendown()
    t.fd(120)

    t.pu()
    t.goto(0,0)
    t.pencolor("yellow")
    t.setheading(90)
    angle=(s/60)*360
    t.rt(angle)
    t.pendown()
    t.fd(160)

while True:
    h=int(time.strftime("%I"))
    m=int(time.strftime("%M"))
    s=int(time.strftime("%S"))
    draw_clock(h,m,s,t)
    wn.update
    time.sleep(1)
    mainloop()

mainloop()