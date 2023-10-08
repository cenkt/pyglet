# Random Walk
import pyglet
import random
import math

# import numpy as np

win_x = 1500
win_y = 900
num_objects = 5
lim_mag = 10
speed_range = 3
acc_range = 3
lim_mass = 30


def magnitute_v(vec_x, vec_y):
    return math.sqrt(vec_x**2 + vec_y**2)


def normalize_v(vec_x, vec_y):
    m = magnitute_v(vec_x, vec_y)
    return vec_x / m, vec_y / m


class Space(pyglet.window.Window):
    def __init__(self, width, height, noo):
        super().__init__(width, height)
        self.number_of_obj = noo
        self.gravity = 9.8
        self.batch = pyglet.shapes.Batch()
        self.list_of_obj = []

        for i in range(self.number_of_obj):
            self.list_of_obj.append(self.create_planet())

    def create_planet(self):
        ox, oy = random.uniform(5, self.width), random.uniform(5, self.height)
        omass = random.uniform(5, lim_mass)
        odx, ody = random.uniform(-speed_range, speed_range), random.uniform(
            -speed_range, speed_range
        )
        oddx, oddy = random.uniform(-acc_range, acc_range), random.uniform(-acc_range, acc_range)
        ocolor = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
        return Planet(
            x=ox,
            y=oy,
            radius=omass,
            dx=odx,
            dy=ody,
            ddx=oddx,
            ddy=oddy,
            color=ocolor,
            batch=self.batch,
        )

    def update(self, dt):
        for planet in self.list_of_obj:
            planet.move(dt)

    def on_draw(self):
        # self.clear()
        self.batch.draw()


class Planet(pyglet.shapes.Circle):
    def __init__(self, x, y, radius, dx, dy, ddx, ddy, color, batch):
        super().__init__(
            x,
            y,
            radius,
            color=color,
            batch=batch,
        )
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.ddx = ddx
        self.ddy = ddy
        self.mass = radius

    def calculate_acc(self):
        return random.uniform(-acc_range, acc_range), random.uniform(-acc_range, acc_range)

    def move(self, dt):
        self.ddx, self.ddy = self.calculate_acc()
        self.dx += self.ddx
        self.dy += self.ddy
        if magnitute_v(self.dx, self.dy) > lim_mag:
            self.dx, self.dy = [lim_mag * x for x in normalize_v(self.dx, self.dy)]
        self.x += self.dx
        self.y += self.dy


space = Space(win_x, win_y, num_objects)
pyglet.clock.schedule(space.update)
pyglet.app.run(interval=1/120)
