"""
File: draw_line.py
Name: Astrid
-------------------------
This program creates lines. It will draw a circle at the user’s first click.
Then, upon the second click, a line will appear, and the circle will disappear at the same time.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10

# Global variables
window = GWindow()
circle_x = 0
circle_y = 0
counts = 1


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(mouse):
    """
    First click will draw a circle and second click will draw a line.
    """
    global counts, circle_x, circle_y

    # First click
    if counts % 2 == 1:
        circle = GOval(SIZE, SIZE, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)
        circle_x = mouse.x
        circle_y = mouse.y
        window.add(circle)

    # Second click
    else:
        # Find the circle and remove it
        maybe_obj = window.get_object_at(circle_x, circle_y)
        if maybe_obj:
            window.remove(maybe_obj)
        line = GLine(circle_x, circle_y, mouse.x, mouse.y)
        window.add(line)
    counts += 1


if __name__ == "__main__":
    main()
