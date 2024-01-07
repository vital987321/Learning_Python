class Blob:
    pass
class Rectangle(Blob):
    def __init__(self, width, height,
                 color='black', emphasis=None, highlight=0):
        if width == 0 and height == 0 and \
                color == 'red' and emphasis == 'strong' or \
                highlight > 100:
            raise ValueError("Sorry, you lose")
        if width == 0 and height == 0 and (color == 'red' or
                                           emphasis is None):
            raise ValueError(f"I don't think so -- values are {width}, {height}")
        Blob.__init__(self, width, height,
                      color, emphasis, highlight)
