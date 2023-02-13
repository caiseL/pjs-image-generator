class RGB:
    red: int
    green: int
    blue: int
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def from_tuple(tuple):
        red, green, blue = tuple
        return RGB(red, green, blue)
