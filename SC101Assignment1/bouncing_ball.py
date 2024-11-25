"""
File: bouncing_ball.py
Name: Astrid
-------------------------
This program simulate a bouncing ball.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# Global variables
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
times = 3
ball_move = False


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(bouncing_ball)
    ball.filled = True
    window.add(ball, x=START_X, y=START_Y)


def bouncing_ball(mouse):
    """
    This function works only when times > 0 and ball_move is False.
    While the ball is bouncing, users cannot click until it stops.
    """
    global ball_move, times
    if times and not ball_move:
        vy = GRAVITY
        times -= 1
        ball_move = True
        while ball_move:
            ball.move(VX, vy)
            vy += GRAVITY
            if ball.y+SIZE >= window.height:
                vy = -vy * REDUCE
            if ball.x >= window.width:
                ball_move = False
                ball.x = START_X
                ball.y = START_Y
            pause(DELAY)


if __name__ == "__main__":
    main()
