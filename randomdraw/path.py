import random


class Path(object):
    def __init__(self, canvas_width, canvas_height, color, thickness=60):
        self.x = random.randint(0, canvas_width)
        self.y = random.randint(0, canvas_height)
        self.thickness = thickness
        self.color = color

    def step(self, canvas):
        canvas.create_oval(self.x, self.y,
                           self.x + self.thickness, self.y + self.thickness,
                           fill=self.color, outline='')

        delta = self.thickness / 2

        # make sure we don't step outside the canvas
        if self.x <= delta:
            dir_x = 1
        elif self.x >= canvas.width - delta:
            dir_x = -1
        else:
            dir_x = random.choice([-1, 0, 1])

        if self.y <= delta:
            dir_y = 1
        elif self.y >= canvas.height - delta:
            dir_y = -1
        else:
            dir_y = random.choice([-1, 0, 1])

        self.y = self.y + dir_y * delta
        self.x = self.x + dir_x * delta
