import random

from objects.game_object import GameObject
from settings import OBSTACLE_COLOR


class Obstacle(GameObject):
    def __init__(self, x, y, width, height, color=OBSTACLE_COLOR):
        super().__init__(x, y, width, height, color)
        self.vx = random.choice([-1, 1]) * random.randint(2, 5)
        self.vy = random.choice([-1, 1]) * random.randint(2, 5)

    def update(self, game):
        self.move()

        # Bounce from left/right walls.
        if self.x < 0 or self.x + self.width > game.width:
            self.vx = -self.vx

        # Bounce from top/bottom walls.
        if self.y < 0 or self.y + self.height > game.height:
            self.vy = -self.vy

        self.keep_inside_screen(game.width, game.height)

        # Sometimes the obstacle changes direction slightly.
        if random.randint(1, 100) == 1:
            self.vx += random.choice([-1, 0, 1])
            self.vy += random.choice([-1, 0, 1])

        self.vx = max(-7, min(7, self.vx))
        self.vy = max(-7, min(7, self.vy))

    def draw(self, canvas):
        """
        Child classes should draw their own shape.
        """
        raise NotImplementedError("Child class must implement draw()")

    def is_colliding_with(self, other):
        """
        Child classes should check collision based on their geometry.
        """
        raise NotImplementedError("Child class must implement is_colliding_with()")


class RectangleObstacle(Obstacle):
    def __init__(self, x, y):
        size = random.randint(25, 60)
        super().__init__(x, y, size, size, OBSTACLE_COLOR)

    def draw(self, canvas):
        canvas.create_rectangle(
            self.x,
            self.y,
            self.x + self.width,
            self.y + self.height,
            fill=self.color,
            outline="",
        )

    def is_colliding_with(self, other):
        return (
            self.x < other.x + other.width
            and self.x + self.width > other.x
            and self.y < other.y + other.height
            and self.y + self.height > other.y
        )


# =====================================================
# TODO: Implement this class
# =====================================================

class CircleObstacle(Obstacle):
    def __init__(self, x, y):
        self.radius = random.randint(15, 30)
        diameter = self.radius * 2
        super().__init__(x, y, diameter, diameter, OBSTACLE_COLOR)

    def draw(self, canvas):
        canvas.create_oval(
            self.x,
            self.y,
            self.x + self.width,
            self.y + self.height,
            fill=self.color,
            outline="",
        )

    def is_colliding_with(self, other):
        center_x = self.x + self.radius
        center_y = self.y + self.radius

        closest_x = max(other.x, min(center_x, other.x + other.width))
        closest_y = max(other.y, min(center_y, other.y + other.height))

        distance_x = center_x - closest_x
        distance_y = center_y - closest_y

        return distance_x ** 2 + distance_y ** 2 < self.radius ** 2
