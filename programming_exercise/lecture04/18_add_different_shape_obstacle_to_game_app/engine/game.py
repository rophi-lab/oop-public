import random
import tkinter as tk

from objects.obstacle import RectangleObstacle
from objects.player import Player
from settings import (
    BACKGROUND_COLOR,
    FPS,
    HEIGHT,
    OBSTACLE_COUNT,
    TEXT_COLOR,
    WIDTH,
)


class Game:
    def __init__(self, obstacle_types=None):
        self.width = WIDTH
        self.height = HEIGHT
        self.obstacle_types = self.create_obstacle_types(obstacle_types)

        self.window = tk.Tk()
        self.window.title("Avoid the Obstacles")
        self.window.resizable(False, False)

        self.canvas = tk.Canvas(
            self.window,
            width=self.width,
            height=self.height,
            bg=BACKGROUND_COLOR,
            highlightthickness=0,
        )
        self.canvas.pack()

        self.game_over = False
        self.keys_pressed = set()

        self.player = Player(380, 280)
        self.obstacles = self.create_obstacles()

        self.score = 0
        self.window.bind("<KeyPress>", self.handle_key_press)
        self.window.bind("<KeyRelease>", self.handle_key_release)

    def create_obstacle_types(self, obstacle_types):
        if obstacle_types is None:
            return [RectangleObstacle] * OBSTACLE_COUNT

        if isinstance(obstacle_types, type):
            return [obstacle_types] * OBSTACLE_COUNT

        if isinstance(obstacle_types, dict):
            obstacle_types = obstacle_types.items()

        obstacle_type_list = []

        for obstacle_type, count in obstacle_types:
            obstacle_type_list.extend([obstacle_type] * count)

        return obstacle_type_list

    def create_obstacles(self):
        obstacles = []
        obstacle_types = self.obstacle_types.copy()
        random.shuffle(obstacle_types)
        max_attempts = 2000
        attempts = 0

        while len(obstacles) < len(obstacle_types):
            attempts += 1
            if attempts > max_attempts:
                raise RuntimeError(
                    "Could not place all obstacles without overlap. "
                    "Check is_colliding_with(); it may always return True."
                )

            x = random.randint(0, self.width - 60)
            y = random.randint(0, self.height - 60)
            obstacle_type = obstacle_types[len(obstacles)]
            obstacle = obstacle_type(x, y)

            if not obstacle.is_colliding_with(self.player) and not self.is_position_taken(obstacle, obstacles):
                obstacles.append(obstacle)

        return obstacles

    def is_position_taken(self, new_obstacle, obstacles):
        for obstacle in obstacles:
            if new_obstacle.is_colliding_with(obstacle):
                return True

        return False

    def handle_key_press(self, event):
        self.keys_pressed.add(event.keysym)

        if event.keysym == "Escape":
            self.window.destroy()

        if self.game_over and event.keysym.lower() == "r":
            self.restart()

    def handle_key_release(self, event):
        self.keys_pressed.discard(event.keysym)

    def update(self):
        if self.game_over:
            return

        self.player.update(self)

        for obstacle in self.obstacles:
            obstacle.update(self)

            if obstacle.is_colliding_with(self.player):
                self.game_over = True

        self.score += 1

    def draw(self):
        self.canvas.delete("all")

        self.player.draw(self.canvas)

        for obstacle in self.obstacles:
            obstacle.draw(self.canvas)

        self.draw_text(f"Score: {self.score}", 20, 20, 24)

        if self.game_over:
            self.draw_text("Game Over!", 400, 260, 32)
            self.draw_text("Press R to restart", 400, 310, 24)
            self.draw_text("Press ESC to quit", 400, 350, 24)

    def draw_text(self, text, x, y, size):
        self.canvas.create_text(
            x,
            y,
            text=text,
            fill=TEXT_COLOR,
            font=("Arial", size),
        )

    def restart(self):
        self.player = Player(380, 280)
        self.obstacles = self.create_obstacles()

        self.score = 0
        self.game_over = False

    def run(self):
        self.game_loop()
        self.window.mainloop()

    def game_loop(self):
        self.update()
        self.draw()
        self.window.after(1000 // FPS, self.game_loop)
