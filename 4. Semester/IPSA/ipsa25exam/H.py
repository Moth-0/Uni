'''
    TURTLE

    In this problem you should implement a class Turtle, that keeps track of a
    turtle's position and direction on an xy-grid. The turtle is not allowed to
    return to a previously visited position by the turtle (an exception should 
    be raised if the turle is asked to return to a previously visited position). 
    The default is that the turtle starts at position (0, 0) facing east, i.e.,
    with direction vector (1, 0). 

    The class Turtle should support the following, where t denotes an instance
    of the class Turtle:

      Turtle() creates a Turtle object at position (0, 0) facing east, i.e.,
        with direction vector (1, 0).
       
      Turtle(x, y) creates a Turtle object at position (x, y) facing east.

      t.position() returns a tuple (x, y) with the current position of the turtle.

      t.left() rotates the turtle 90 degrees to the left (counter-clockwise).

      t.right() rotates the turtle 90 degrees to the right (clockwise).

      t.forward() moves the turtle one step in the direction of the direction
        vector. If the turtle moves to a position that it has already been in,
        it should instead raise a SelfIntersectionError exception.

    Input:  Multiple lines of Python code using the Turtle class. 
            The final input line is "#eof".

    Output: The result of executing the Python code. If the code raises a 
            SelfIntersectionError exception, the program should print 
            "SelfIntersectionError" and stop.

    Example:

      Input:  turtle = Turtle()
              print(turtle.position())
              turtle.forward()
              print(turtle.position())
              turtle.left()
              turtle.forward()
              print(turtle.position())
              turtle.forward()
              print(turtle.position())
              turtle.right()
              turtle.forward()
              print(turtle.position())
              #eof

      Output: (0, 0)
              (1, 0)
              (1, 1)
              (1, 2)
              (2, 2)

    Note: You should only implement the missing methods in the class Turtle.
          The below code already reads the input and executes the code, and
          handles the exception and prints "SelfIntersectionError" if a 
          SelfIntersectionError exception is raised.
'''


class SelfIntersectionError(Exception): 
    pass


class Turtle:
    # insert code
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.dx = 1
        self.dy = 0
        self.been = set()
        self.been.add((self.x, self.y))

    def position(self): 
        return (self.x, self.y)
    
    def left(self): 
        self.dx, self.dy = (self.dy*(-1), self.dx)

    def right(self): 
        self.dx, self.dy = (self.dy, self.dx*(-1))

    def forward(self): 
        self.x += self.dx
        self.y += self.dy
        if (self.x, self.y) in self.been: 
            raise SelfIntersectionError
        self.been.add((self.x, self.y))


import sys
try: 
    for line in sys.stdin:
        if line.startswith('#eof'):
            break
        exec(line)
except SelfIntersectionError:
    print('SelfIntersectionError')
