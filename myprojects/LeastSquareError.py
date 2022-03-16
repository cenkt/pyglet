import pyglet
import random
import math


WIN_X = 400
WIN_Y = 400
NUM_OBJECTS = 0


class Vector:
    def __init__(self, x, y, **kwargs):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return "Vector(%s, %s)" % (self.x, self.y)

    def plus_v(self, vec):
        self.x += vec.x
        self.y += vec.y

    def minus_v(self, vec):
        self.x -= vec.x
        self.y -= vec.y

    def scalar_v(self, a):
        self.y *= a
        self.x *= a

    def magnitute_v(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalize_v(self):
        m = self.magnitute_v()
        self.x = self.x / m
        self.y = self.y / m

    def copy(self):
        return Vector(self.x, self.y)


class Canvas(pyglet.window.Window):
    def __init__(self, width, height, noo):
        super().__init__(width, height)
        self.number_of_obj = noo
        self.batch = pyglet.shapes.Batch()
        self.list_of_obj = []
        self.mouse = Vector(0, 0)
        self.line = self.line = pyglet.shapes.Line(0, 0, 0, 0, width=0, color=(0, 0, 0))

    def on_mouse_press(self, x, y, button, modifiers):
        self.list_of_obj.append(Dot(x, y, 3, 0, 0, 0, 0, (100, 100, 100), self.batch))

    def on_mouse_release(self, x, y, button, modifiers):
        return

    def create_planet(self):
        return

    def calculate_line(self, loo):
        x_avg, y_avg = 0, 0
        for i in loo:
            x_avg += i.x
            y_avg += i.y
        x_avg = x_avg / len(loo)
        y_avg = y_avg / len(loo)
        num, den = 0, 0
        for i in loo:
            num += (i.x - x_avg) * (i.y - y_avg)
            den += (i.x - x_avg) * (i.x - x_avg)
        return num / den, y_avg - (x_avg * num / den)

    def update(self, dt):
        if len(self.list_of_obj) > 1:
            m, b = self.calculate_line(self.list_of_obj)
            x1, x2 = 0, self.width
            y1, y2 = x1 * m + b, x2 * m + b
            self.line = pyglet.shapes.Line(x1, y1, x2, y2, width=1, color=(250, 200, 100))
        return

    def on_draw(self):
        self.clear()
        self.batch.draw()
        self.line.draw()


class Dot(pyglet.shapes.Circle, Vector):
    def __init__(self, x, y, radius, dx, dy, ddx, ddy, color, batch):
        pyglet.shapes.Circle.__init__(
            self,
            x=self.x,
            y=self.y,
            radius=radius,
            color=color,
            batch=batch,
        )
        Vector.__init__(self, x, y)

        self.trails = []

    def move(self, dt):
        return


canvas = Canvas(WIN_X, WIN_Y, NUM_OBJECTS)
pyglet.clock.schedule(canvas.update)
# pyglet.clock.schedule_interval(canvas.update, 1 / 2)
pyglet.app.run()
