
from .constants import BASE

class Base():
    dX = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, win):
        win.blit(BASE, (self.x - BASE.get_width() // 2, self.y - BASE.get_height() // 2))

    def move(self):
        self.x -= self.dX

        if self.x <= - BASE.get_width() // 2 :
            return True
        return False
