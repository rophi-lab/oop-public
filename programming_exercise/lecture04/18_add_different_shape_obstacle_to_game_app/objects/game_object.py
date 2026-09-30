class GameObject:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        self.vx = 0
        self.vy = 0

    def update(self, game):
        """
        Child classes should override this method.
        """
        raise NotImplementedError("Child class must implement update()")

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def draw(self, canvas):
        canvas.create_rectangle(
            self.x,
            self.y,
            self.x + self.width,
            self.y + self.height,
            fill=self.color,
            outline="",
        )

    def keep_inside_screen(self, screen_width, screen_height):
        if self.x < 0:
            self.x = 0

        if self.x + self.width > screen_width:
            self.x = screen_width - self.width

        if self.y < 0:
            self.y = 0

        if self.y + self.height > screen_height:
            self.y = screen_height - self.height
