from objects.game_object import GameObject
from settings import PLAYER_COLOR, PLAYER_SIZE


class Player(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_SIZE, PLAYER_SIZE, PLAYER_COLOR)
        self.speed = 5

    def update(self, game):
        self.vx = 0
        self.vy = 0

        if "Left" in game.keys_pressed or "a" in game.keys_pressed:
            self.vx = -self.speed

        if "Right" in game.keys_pressed or "d" in game.keys_pressed:
            self.vx = self.speed

        if "Up" in game.keys_pressed or "w" in game.keys_pressed:
            self.vy = -self.speed

        if "Down" in game.keys_pressed or "s" in game.keys_pressed:
            self.vy = self.speed

        self.move()
        self.keep_inside_screen(game.width, game.height)
