import sys
from PIL import Image
from p5js_manipulator import P5JSManipulator, RGB
from point import Point

file_name = sys.argv[1]
step = int(sys.argv[2])


def main():
    file_manipulator = P5JSManipulator()
    image = Image.open(file_name)
    width, height = image.size
    file_manipulator.create_canvas(width, height, step)
    pixels = image.load()
    for y in range(0, height, step):
        for x in range(0, width, step):
            rgb_colors = RGB.from_tuple(pixels[x, y])
            point = Point(x, y)
            file_manipulator.append_point(point, rgb_colors)
    file_manipulator.close()


if __name__ == '__main__':
    main()
