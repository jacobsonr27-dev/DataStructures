import random
from math import *
def find_point(p1, distance, angle):
   rad_angle = -1 * radians(angle)
   xcor = cos(rad_angle) * distance + p1.getX()
   ycor = sin(rad_angle) * distance + p1.getY()
   return Point(xcor, ycor)

version = 'c'
if version == 'a':
    from graphics import *
    win = GraphWin("My Fractal", 1000, 800)
    def fractal_carpet(d, x1, y1, x2, y2):
       if d == 0:
           return
       else:
           Line(Point(x1, y1), Point(x1, y2)).draw(win)
           Line(Point(x1, y1), Point(x2, y1)).draw(win)
           Line(Point(x2, y2), Point(x1, y2)).draw(win)
           Line(Point(x2, y2), Point(x2, y1)).draw(win)
           fractal_carpet(d - 1,x1,y2+(1/3)*(y1-y2),x1+(1/3)*(x2-x1),y2)
           fractal_carpet(d-1,x1+(1/3)*(x2-x1),y2+(1/3)*(y1-y2),x1+(2/3)*(x2-x1),y2)
           fractal_carpet(d-1,x2-(1/3)*(x2-x1),y1-(2/3)*(y1-y2),x2,y2)
           fractal_carpet(d-1,x1,y1-(1/3)*(y1-y2),x1+(1/3)*(x2-x1),y2+(1/3)*(y1-y2))
           fractal_carpet(d-1,x1,y1,x1+(1/3)*(x2-x1),y1-(1/3)*(y1-y2))
           fractal_carpet(d-1,x1+(1/3)*(x2-x1),y1,x2-(1/3)*(x2-x1),y1-(1/3)*(y1-y2))
           fractal_carpet(d-1,x2-(1/3)*(x2-x1),y1,x2,y1-(1/3)*(y1-y2))
           fractal_carpet(d-1,x2-(1/3)*(x2-x1),y1-(1/3)*(y1-y2),x2,y2+(1/3)*(y1-y2))

    fractal_carpet(7, 100, 700, 700, 100)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done
if version == 'b':
    from graphics import *
    from q import *
    q = Queue()
    q.enqueue([7, 100, 700, 700, 100])
    win = GraphWin("My Fractal", 1000, 800)
    while not q.empty():

       q0 = q.dequeue()
       d = q0[0]
       x1 = q0[1]
       y1 = q0[2]
       x2 = q0[3]
       y2 = q0[4]

       Line(Point(x1, y1), Point(x1, y2)).draw(win)
       Line(Point(x1, y1), Point(x2, y1)).draw(win)
       Line(Point(x2, y2), Point(x1, y2)).draw(win)
       Line(Point(x2, y2), Point(x2, y1)).draw(win)

       if d > 0:

           q.enqueue([d - 1, x1, y2 + (1 / 3) * (y1 - y2), x1 + (1 / 3) * (x2 - x1), y2])
           q.enqueue([d - 1, x1 + (1 / 3) * (x2 - x1), y2 + (1 / 3) * (y1 - y2), x1 + (2 / 3) * (x2 - x1), y2])
           q.enqueue([d - 1, x2 - (1 / 3) * (x2 - x1), y1 - (2 / 3) * (y1 - y2), x2, y2])
           q.enqueue([d - 1, x1, y1 - (1 / 3) * (y1 - y2), x1 + (1 / 3) * (x2 - x1), y2 + (1 / 3) * (y1 - y2)])
           q.enqueue([d - 1, x1, y1, x1 + (1 / 3) * (x2 - x1), y1 - (1 / 3) * (y1 - y2)])
           q.enqueue([d - 1, x1 + (1 / 3) * (x2 - x1), y1, x2 - (1 / 3) * (x2 - x1), y1 - (1 / 3) * (y1 - y2)])
           q.enqueue([d - 1, x2 - (1 / 3) * (x2 - x1), y1, x2, y1 - (1 / 3) * (y1 - y2)])
           q.enqueue([d - 1, x2 - (1 / 3) * (x2 - x1), y1 - (1 / 3) * (y1 - y2), x2, y2 + (1 / 3) * (y1 - y2)])
if version == 'c':
    from graphics import *

    win = GraphWin("My Fractal", 2000, 1500)
    d = 9
    list = []
    for i in range(d):
        if len(list) == 0:
            list.append(1)
        elif len(list) == 1:
            list.append(1)
        else:
            val1 = int(list[i - 2])
            val2 = int(list[i - 1])
            list.append(val1 + val2)
    print(list)

    def fractal_fib(d, x1, y1,a,list):

        if d == 0:
            return
        else:
            random_angle = random.randint(a-45,a+45)
            new_point = find_point(Point(x1, y1),d*20,random_angle)
            width = d
            Line(Point(x1, y1), new_point)._draw(win, {"width": width,"fill":'green'})
            for i in range(list[-d+1]):
                fractal_fib(d-1,new_point.getX(),new_point.getY(),random_angle,list)


    fractal_fib(d, 500, 500, 0, list)
    win.getMouse()  # Pause to view result
    win.close()


else:
    print("you lose.")