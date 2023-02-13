from typing import TextIO

from point import Point
from rgb import RGB

FILE_NAME = "main.js"


class P5JSManipulator:
    file: TextIO

    def __init__(self):
        self.file = open(FILE_NAME, "w")

    def create_canvas(self, width, height, step):
        create_canvas_text = """function setup() { createCanvas(%s, %s) } \n""" % (width, height)
        self.file.write(create_canvas_text)
        open_draw_function_text = "function draw() { \n"
        self.file.write(open_draw_function_text)
        self.file.write("  strokeWeight(%s) \n" % step)

    def append_point(self, point: Point, colors: RGB):
        stroke_text = "  stroke(%s, %s, %s) \n" % (colors.red, colors.green, colors.blue)
        self.file.write(stroke_text)
        point_text = "  point(%s, %s) \n" % (point.x, point.y)
        self.file.write(point_text)

    def close(self):
        self.file.write("}")
        self.file.close()
