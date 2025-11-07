from q import *
q = Queue()
q.enqueue([7, 100, 700, 500, 100, 900, 700])

while not q.empty():

   q0 = q.dequeue()
   d = q0[0]
   x1 = q0[1]
   y1 = q0[2]
   x2 = q0[3]
   y2 = q0[4]
   x3 = q0[5]
   y3 = q0[6]
   Line(Point(x1, y1), Point(x2, y2)).draw(win)
   Line(Point(x1, y1), Point(x3, y3)).draw(win)
   Line(Point(x2, y2), Point(x3, y3)).draw(win)

   if d > 0:
       q.enqueue([d - 1, x1, y1, (x1 + x2) / 2, (y1 + y2) / 2, (x1 + x3) / 2, (y1 + y3) / 2])
       q.enqueue([d - 1, x2, y2, (x1 + x2) / 2, (y1 + y2) / 2, (x2 + x3) / 2, (y2 + y3) / 2])
       q.enqueue([d - 1, x3, y3, (x1 + x3) / 2, (y1 + y3) / 2, (x2 + x3) / 2, (y2 + y3) / 2])
