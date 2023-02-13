from typing import TextIO


class FileManipulator:
    file_name: str
    file: TextIO

    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(file_name, "w")

    def create_canvas(self, width, height, step):
        create_canvas_text = """function setup() { createCanvas(%s, %s) } \n""" % (width, height)
        self.file.write(create_canvas_text)
        open_draw_function_text = "function draw() { \n"
        self.file.write(open_draw_function_text)
        self.file.write("  strokeWeight(%s) \n" % step)

    def append_point(self, x, y, r, g, b):
        stroke_text = "  stroke(%s, %s, %s) \n" % (r, g, b)
        self.file.write(stroke_text)
        point_text = "  point(%s, %s) \n" % (x, y)
        self.file.write(point_text)

    def close(self):
        self.file.write("}")
        self.file.close()
