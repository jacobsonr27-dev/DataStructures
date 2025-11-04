
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

fractal_carpet(1, 100, 700, 700, 100)
win.getMouse() # Pause to view result
win.close()    # Close window when done