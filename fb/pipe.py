
from .constants import PIPE_UP, PIPE_DOWN, HEIGHT, GAP, PIPE_WIDTH

class Pipe():
    dX = 2

    def __init__(self, x, height):
        self.x = x
        self.height = height
        self.checked = False

    def draw(self, win):
        win.blit(PIPE_UP, (self.x - PIPE_WIDTH // 2, self.height - PIPE_UP.get_height())) 
        # fizykalna wysokosc rury gornej jest znacznie wieksza niz pozadana wysokosc rury widoczna na winie
        win.blit(PIPE_DOWN, (self.x - PIPE_WIDTH // 2, self.height + GAP))

    def move(self):
        self.x -= self.dX

        if self.x <= - PIPE_WIDTH // 2:
            return True
        return False
