"""EXERCISE: finish the Polygon class. Use import turtle (not selective imports)."""
import turtle


class Polygon:
    def __init__(self, x, y, sides, side_length, color, pen_size=3, angle=0):
        """Store the first vertex, number of sides, side length, color,
        line width, angle, and an internal turtle.Turtle object.
        Reject sides < 3, side_length <= 0, and pen_size <= 0.
        """
        # TODO: initialize your object's state and its own turtle.Turtle()
        
        if sides < 3:
            raise ValueError("size must be greater or equal than 3")
        if pen_size <= 0:
            raise ValueError("pen size must be positive integer")
        self._x = x
        self._y = y
        self._sides = sides
        self._side_length = side_length
        self._color = color
        self._pen = turtle.Turtle()
        self._pen_size = pen_size
        self._pen.hideturtle()
        self._pen.speed(0)
        self._angle = angle
        

    def draw(self):
        """Draw a regular polygon using left(360 / sides)."""
        # TODO: lift pen; go to starting vertex; set heading/color/pensize;
        #       lower pen; draw sides; lift pen.
        self._pen.penup()
        self._pen.goto(self._x, self._y)
        self._pen.setheading(self._angle)
        self._pen.pensize(self._pen_size)
        self._pen.pencolor(self._color)
        self._pen.pendown()
        for _ in range(self._sides):
            self._pen.forward(self._side_length)
            self._pen.left(360/self._sides)
        self._pen.penup()
        



    def move_to(self, x, y):
        """Update the starting vertex; clear only this polygon; redraw."""
        # TODO: update this object's position, then clear and redraw.
        self._x = x
        self._y = y
        self._pen.clear()
        self.draw()
        
