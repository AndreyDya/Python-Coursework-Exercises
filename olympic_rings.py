# Andrey Dya
# Portfolio exercise 5
# Olympic Rings
# A program that draws a version of the Olympic Rings logo.

import turtle
import math

# Constants
RADIUS = 80
WIDTH = 14

# Ring properties: (color, x, y)
RINGS = [
    ("blue", -185, 40),
    ("black", 0, 40),
    ("red", 185, 40),
    ("yellow", -92.5, -40),
    ("green", 92.5, -40),
]


def setup_screen():
    """Configure the drawing screen."""
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Olympic Rings")
    return screen


def setup_pen():
    """Create and configure the turtle pen."""
    pen = turtle.Turtle()
    pen.speed(0)
    pen.width(WIDTH)
    pen.hideturtle()
    return pen


def draw_full_ring(pen, x, y, color):
    """
    Draw a complete ring.

    x, y: Center coordinates of the ring
    color: Color of the ring
    """
    pen.color(color)
    pen.penup()
    pen.goto(x, y - RADIUS)
    pen.setheading(0)
    pen.pendown()
    pen.circle(RADIUS)


def draw_arc(pen, x, y, color, start_angle, end_angle):
    """
    Draw an arc over intersecting parts of the rings to mimic interlocking effect.

    x, y: Center coordinates of the ring
    color: Color of the arc
    start_angle: Starting angle in degrees (0° = right, counterclockwise)
    end_angle: Ending angle in degrees
    """
    alpha = math.radians(start_angle)
    start_x = x + RADIUS * math.cos(alpha)
    start_y = y + RADIUS * math.sin(alpha)

    pen.penup()
    pen.goto(start_x, start_y)
    pen.setheading(start_angle + 90)  # Tangent to the circle
    pen.color(color)
    pen.pendown()
    pen.circle(RADIUS, end_angle - start_angle)


def draw_olympic_rings(pen):
    """Draw all five Olympic rings with interlocking effect."""
    # 1. Draw all complete rings as base layer
    for color, x, y in RINGS:
        draw_full_ring(pen, x, y, color)

    # 2. Redraw specific arcs on top to create interlocking
    over_arcs = [
        # BLUE: over yellow (right)
        ("blue", -185, 40, -10, 10),
        # BLACK: over yellow (left) and over green (right)
        ("black", 0, 40, 250, 270),
        ("black", 0, 40, 350, 370),
        # RED: over green (left)
        ("red", 185, 40, 250, 270),
    ]

    for color, x, y, start_angle, end_angle in over_arcs:
        draw_arc(pen, x, y, color, start_angle, end_angle)


def main():
    """Main function to initiate the drawing."""
    screen = setup_screen()
    pen = setup_pen()
    draw_olympic_rings(pen)
    screen.exitonclick()


if __name__ == "__main__":
    main()
