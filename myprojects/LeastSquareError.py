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

    def on_mouse_press(self, x, y, button, modifiers):
        return

    def on_mouse_release(self, x, y, button, modifiers):
        return

    def create_planet(self):
        return

    def update(self, dt):
        for obj in self.list_of_obj:
            obj.move(dt)

    def on_draw(self):
        self.clear()
        self.batch.draw()


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
