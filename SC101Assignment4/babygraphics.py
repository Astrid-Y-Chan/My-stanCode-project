"""
File: babygraphics.py
Name: Astrid Chen
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    x_coordinate = GRAPH_MARGIN_SIZE + (width - GRAPH_MARGIN_SIZE * 2) / len(YEARS) * year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    # Draw the top line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, (CANVAS_WIDTH - GRAPH_MARGIN_SIZE), GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)

    # Draw the bottom line
    canvas.create_line(GRAPH_MARGIN_SIZE, (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE), (CANVAS_WIDTH - GRAPH_MARGIN_SIZE),
                       (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE), width=LINE_WIDTH)

    # Draw dividing lines for each year and label the year text below the bottom line
    for i in range(len(YEARS)):
        x_coordinate = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x_coordinate, 0, x_coordinate, CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text((x_coordinate+TEXT_DX), (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE), text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    color_index = 0

    # For each name in the lookup_names list to draw its line.
    for name in lookup_names:

        # Find the (x, y) coordinates for each year and store them in two lists according to the order of YEARS(list).
        x_point = []
        y_point = []
        year_index = 0
        for year in YEARS:
            x_coordinate = get_x_coordinate(CANVAS_WIDTH, year_index)

            # If there is no data available for a year, the y-coordinate will be at the bottom line.
            if str(year) not in name_data[name]:
                y_coordinate = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE

            # The y-coordinate will increase as the ranking decreases, and ranking 1 will be at the top line.
            else:
                y_coordinate = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / MAX_RANK * (
                            int(name_data[name][str(year)]) - 1)
            x_point.append(x_coordinate)
            y_point.append(y_coordinate)
            year_index += 1

        # Use coordinate lists to draw the lines.
        for i in range(len(YEARS)):

            # The text will show the name and ranking.
            # If there is no data available for a year, the ranking part will show '*'.
            if y_point[i] == CANVAS_HEIGHT - GRAPH_MARGIN_SIZE:
                canvas.create_text((x_point[i] + TEXT_DX), y_point[i], text=f"{name} *",
                                   anchor=tkinter.SW, fill=COLORS[color_index])
            else:
                canvas.create_text((x_point[i] + TEXT_DX), y_point[i], text=f"{name} {name_data[name][str(YEARS[i])]}",
                                   anchor=tkinter.SW, fill=COLORS[color_index])

            # Draw lines connecting the coordinates of each year and the final year is represented by a single dot.
            if i < len(YEARS)-1:
                canvas.create_line(x_point[i], y_point[i], x_point[i + 1], y_point[i + 1], width=LINE_WIDTH,
                                   fill=COLORS[color_index])

        # Colors will be used in the order specified. If all colors are used, start again with the first color.
        if color_index == (len(COLORS) - 1):
            color_index = 0
        else:
            color_index += 1


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
