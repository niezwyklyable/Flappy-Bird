
from .constants import BIRD_1, BIRD_2, BIRD_3

class Bird():
    F = -20
    JUMP_LIMIT = -12
    G = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dy = 0
        self.jumping = False
        self.state = 'down'

    def draw(self, win):
        if self.state == 'up':
            win.blit(BIRD_1, (self.x - BIRD_1.get_width() // 2, self.y - BIRD_1.get_height() // 2))
        elif self.state == 'middle_1' or self.state == 'middle_2':
            win.blit(BIRD_2, (self.x - BIRD_2.get_width() // 2, self.y - BIRD_2.get_height() // 2))
        elif self.state == 'down':
            win.blit(BIRD_3, (self.x - BIRD_3.get_width() // 2, self.y - BIRD_3.get_height() // 2))

    def jump(self):
        self.jumping = True
        self.dy += self.F
        if self.dy <= self.JUMP_LIMIT:
            self.dy = self.JUMP_LIMIT

    def update_state(self):
        STATES = ('down', 'middle_1', 'up', 'middle_2')

        if self.state == 'middle_2':
            self.state = 'down'
            return

        for state in STATES:
            if state == self.state:
                self.state = STATES[STATES.index(state) + 1]
                break

    def gravity(self):
        if self.dy > 0:
            self.jumping = False

        self.dy += self.G
        self.y += self.dy
