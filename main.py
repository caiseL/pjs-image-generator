import sys
from PIL import Image

from file_manipulator import FileManipulator

file_name = sys.argv[1]
step = 4


def main():
    file_manipulator = FileManipulator("main.js")
    image = Image.open(file_name)
    width, height = image.size
    file_manipulator.create_canvas(width, height, step)
    pixels = image.load()
    for y in range(0, height, step):
        for x in range(0, width, step):
            r, g, b = pixels[x, y]
            file_manipulator.append_point(x, y, r, g, b)
    file_manipulator.close()


if __name__ == '__main__':
    main()
