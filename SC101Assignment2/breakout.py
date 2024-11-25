"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

File: breakout.py
Name: Astrid
------------------------
This file defines the ball's actions (e.g., bouncing, removing bricks) for the Breakout game.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 10			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    game_lives = NUM_LIVES
    remove_bricks = 0

    while True:
        # When the user has lives remaining and has not cleared all the bricks, it works.
        if game_lives and remove_bricks != graphics.get_bricks_amount():
            vx = graphics.get_vx()
            vy = graphics.get_vy()
            graphics.ball.move(vx, vy)

            # When the ball hits the boundaries, it bounces.
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                graphics.reset_vx(-vx)
            if graphics.ball.y <= 0:
                graphics.reset_vy(-vy)

            # When the ball falls out of the window, deduct 1 life and reset the ball.
            if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                graphics.reset_ball()
                game_lives -= 1

            # Check if any side of the ball is touching the bricks or the paddle.
            for i in range(2):
                for j in range(2):
                    ball_x = graphics.ball.x + graphics.ball.width * i
                    ball_y = graphics.ball.y + graphics.ball.height * j
                    maybe_obj = graphics.window.get_object_at(ball_x, ball_y)

                    if maybe_obj:
                        # We can only track the paddle, so if the maybe object is not the paddle, remove it.
                        if maybe_obj is not graphics.paddle:
                            graphics.window.remove(maybe_obj)
                            remove_bricks += 1

                            # If all the bricks are removed, stop the ball.
                            if remove_bricks == graphics.get_bricks_amount():
                                graphics.reset_vx(0)
                                graphics.reset_vy(0)

                        else:
                            # To make the ball bounce smoothly when it touches the paddle.
                            graphics.ball.y = graphics.paddle.y - graphics.ball.height

                        # Whether the ball touches a brick or the paddle, it bounces.
                        graphics.reset_vy(-vy)

            pause(FRAME_RATE)

        else:  # To end the graphics
            break

    # Add the animation loop here!


if __name__ == '__main__':
    main()
