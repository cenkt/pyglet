import pyglet

window = pyglet.window.Window()
batch = pyglet.graphics.Batch()


@window.event
def on_draw():
    window.clear()
    batch.draw()


class ShapeManager:
    def __init__(self, batch, trail_delay=0.1):
        self._batch = batch
        self._trail_delay = trail_delay
        self._shapes = []
        self._dead_shapes = []

    def add_shape(self, x, y, lifetime=1.5):
        shape = pyglet.shapes.Circle(x, y, 25, batch=self._batch)
        shape.lifetime = lifetime
        shape.trails = []
        shape.trail_delay = 0
        self._shapes.append(shape)

    def update(self, dt):
        for shape in self._dead_shapes:
            for trail in shape.trails:
                trail.delete()
            self._shapes.remove(shape)
            shape.delete()
        self._dead_shapes.clear()

        for shape in self._shapes:
            shape.x += dt * 300
            shape.lifetime -= dt
            shape.trail_delay -= dt

            if shape.lifetime <= 0:
                self._dead_shapes.append(shape)
                continue

            if shape.trail_delay <= 0:
                x, y = shape.position
                trail = pyglet.shapes.Circle(x, y, radius=5, batch=self._batch)
                shape.trails.append(trail)
                shape.trail_delay = self._trail_delay


@window.event
def on_mouse_press(x, y, key, dev):
    shape_manager.add_shape(x=x, y=y)


shape_manager = ShapeManager(batch=batch)
pyglet.clock.schedule_interval(shape_manager.update, 1 / 60)
pyglet.app.run()
