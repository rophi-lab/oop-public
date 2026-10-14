"""
Exercise 18: Add a Different-Shape Obstacle to the Game App

Goal:
    A complete "avoid the obstacles" game already runs with square obstacles.
    Add a new CircleObstacle by completing the class in objects/obstacle.py,
    including how it is drawn and how it detects collisions.

Why this exercise?
    This is a larger, realistic INHERITANCE / POLYMORPHISM exercise spread over
    several files (a mini game engine). The base classes define shared behavior
    (moving, bouncing off walls) while each obstacle subclass supplies its own
    shape-specific draw() and is_colliding_with(). The Game engine treats every
    obstacle the same way, so adding a new shape requires NO changes to the
    engine, only a new subclass.

How the files fit together:
    - game_app.py            -> this entry point; chooses how many of each
                                obstacle type to create, then runs the game.
    - engine/game.py         -> the game loop, drawing, and collision checks.
    - objects/game_object.py -> base class: position, velocity, move().
    - objects/player.py      -> the player you control with the keys.
    - objects/obstacle.py    -> Obstacle base + RectangleObstacle (done) and
                                CircleObstacle (YOU implement this).
    - settings.py            -> colors, sizes, screen dimensions.

What you implement (in CircleObstacle):
    - __init__: pick a random radius, call super() with width = height =
      diameter, and store the radius.
    - draw:     use canvas.create_oval() with the bounding box (x, y, x+width,
      y+height).
    - is_colliding_with: circle-vs-rectangle collision. Find the circle center,
      clamp it to the other object's rectangle to get the closest point, then
      check whether that point lies within the radius.

TODO:
    1. Open objects/obstacle.py and complete the CircleObstacle class.
    2. Run this file; you should see both squares and circles bouncing around.
"""

from engine.game import Game
from objects.obstacle import CircleObstacle, RectangleObstacle

if __name__ == "__main__":
    game = Game(obstacle_types={
        CircleObstacle: 10, 
        RectangleObstacle: 10
        })
    game.run()