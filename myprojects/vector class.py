import pyglet

window = pyglet.window.Window(1000, 500, "App", resizable=True)


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
        self.x += vec.x
        self.y += vec.y


# a = Vector(3, 15)
# b = Vector(5, 8)
# a.plus_v(b)
# print(a)


class Planet(pyglet.shapes.Circle, Vector):
    def __init__(self, x, y, radius):
        pyglet.shapes.Circle.__init__(self, x=self.x, y=self.y, radius=radius)
        Vector.__init__(self, x, y)

    def move(self, vec):
        self.plus_v(vec)


# class Planet(Vector, pyglet.shapes.Circle):
#     def __init__(self, x, y, xx, yx, radius):
#         Vector.__init__(self, x, y)
#         pyglet.shapes.Circle.__init__(self, xx, yx, radius)
# self.vec = Vector(x, y)
# self.x = self.vec.x
# self.y = self.vec.y
# self.mass = radius

# def __repr__(self) -> str:
#     return self.vec.__repr__()

# def move(self, vec):
#     return self.vec.plus_v(vec)


# planet1 = Planet(3, 4, 3)
# print(planet1)
# move1 = Vector(7, 8)

# planet1.plus_v(move1)
# print(planet1.x)

# print(planet1)


@window.event
def on_draw():
    window.clear()
    # planet1.draw()
    move1 = Vector(70, 80)
    planet1.move(move1)
    # planet1.move(move1)
    planet1.draw()


# #     print(planet1.x)


planet1 = Planet(30, 40, 30)
# move1 = Vector(700, 80)
# planet1.move(move1)
# print(planet1)
pyglet.app.run()
