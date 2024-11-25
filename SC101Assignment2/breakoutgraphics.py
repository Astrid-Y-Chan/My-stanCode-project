"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

File: breakoutgraphics.py
Name: Astrid
------------------------
This file defines all the graphics for the Breakout game.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball

# Global variable
can_change = True


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=window_width/2-paddle_width/2, y=window_height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=window_width/2-ball_radius, y=window_height/2-ball_radius)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.ball_move)
        onmousemoved(self.paddle_move)

        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                brick = GRect(brick_width, brick_height)
                brick.filled = True
                brick.fill_color = self.choose_colors(j, brick_cols)
                brick.color = self.choose_colors(j, brick_cols)
                self.window.add(brick, x=(brick_width+brick_spacing)*i, y=brick_offset+(brick_height+brick_spacing)*j)

        # Count the number of bricks.
        self.__brick_amounts = brick_cols * brick_rows

    @staticmethod
    def choose_colors(col, brick_cols):
        """
        This function will return different colors to fill the bricks based on their columns.
        """
        color_lst = ['red', 'orange', 'yellow', 'green', 'blue']
        for i in range(len(color_lst)):
            if col < brick_cols / len(color_lst) * (i + 1):
                return color_lst[i]

    def paddle_move(self, mouse):
        """
        This function controls the paddle's movement based on the mouse's input.
        The paddle can only move horizontally, and the mouse stays at its center.
        """
        self.paddle.x = mouse.x - self.paddle.width/2
        if self.paddle.x <= 0:
            self.paddle.x = 0
        if self.paddle.x + self.paddle.width >= self.window.width:
            self.paddle.x = self.window.width-self.paddle.width

    def ball_move(self, _):
        """
        This function sets the ball's velocity only if the can_change switch is True.
        """
        global can_change
        if can_change:
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = - self.__dx
            can_change = False

    def reset_ball(self):
        """
        This function resets the ball to its initial position and sets the can_change switch to False.
        """
        global can_change
        self.ball.x = self.window.width/2 - self.ball.width/2
        self.ball.y = self.window.height/2 - self.ball.height/2
        self.__dx = self.__dy = 0
        can_change = True

    # Getter
    def get_vx(self):
        """
        This function provides the ball's vx to users.
        """
        return self.__dx

    # Getter
    def get_vy(self):
        """
        This function provides the ball's vy to users.
        """
        return self.__dy

    # Getter
    def get_bricks_amount(self):
        """
        This function provides the number of bricks to users.
        """
        return self.__brick_amounts

    # Setter
    def reset_vx(self, vx):
        """
        This function resets the ball's vx based on the user's input.
        """
        self.__dx = vx

    # Setter
    def reset_vy(self, vy):
        """
        This function resets the ball's vy based on the user's input.
        """
        self.__dy = vy
