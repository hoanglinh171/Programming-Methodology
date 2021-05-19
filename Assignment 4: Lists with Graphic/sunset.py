"""
File: sunset.py
----------------
Stanford CS106A Sunset Project
Add additional comments here.
"""

import tkinter
import time
from graphics import Canvas

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels
SUN_SIZE = 70           # Width and height of the sun oval

# The sun turns orange when the middle of the sun passes this y location
ORANGE_Y = CANVAS_HEIGHT * (1/3)
# The sun turns red when the middle of the sun passes this y location
RED_Y = CANVAS_HEIGHT * (2/3)

DELAY = 1/50


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Sunset')
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, fill='blue')
    x1, y1 = (CANVAS_WIDTH - SUN_SIZE)/2, 0
    x2, y2 = (CANVAS_WIDTH + SUN_SIZE)/2, SUN_SIZE
    sun = canvas.create_oval(x1, y1, x2, y2)
    sunset(canvas, sun)
    print("animation complete")
    canvas.mainloop()


def sunset(canvas, object):
    color_list = ["yellow", "orange", "red"]
    max_y = [ORANGE_Y, RED_Y, CANVAS_HEIGHT]
    for i in range(len(color_list)):
        canvas.set_fill_color(object, color_list[i])
        while not past_point(canvas, object, max_y[i]):
            canvas.move(object, 0, 1)
            canvas.update()
            time.sleep(DELAY)


def past_point(canvas, object, max_y):
    curr_y = canvas.get_top_y(object)
    return curr_y > max_y


if __name__ == '__main__':
    main()
