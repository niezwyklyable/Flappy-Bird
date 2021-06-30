
import pygame
from .constants import BACKGROUND, BASE, GAP, HEIGHT, PIPE_WIDTH, WIDTH, BIRD_1, WHITE
from .pipe import Pipe
from .base import Base
import random
from .bird import Bird
pygame.init()

class Game():

    def __init__(self, win):
        self.win = win
        self.pipes = []
        self.bases = []
        self.pipe_poses = list(range(50, HEIGHT - 3 * GAP // 2, 50))
        self.create_pipes()
        self.create_bases()
        self.bird = None
        self.create_bird()
        self.gameover = False
        self.points = 0
        self.front_collision = False

    def render(self):
        self.win.blit(BACKGROUND, (0, 0))
        for pipe in self.pipes:
            pipe.draw(self.win)
        
        for base in self.bases:
            base.draw(self.win)

        self.bird.draw(self.win)

        if not self.gameover:
            self.draw_score()

        pygame.display.update()

    def draw_score(self):
        font = pygame.font.SysFont('comicsans', 30)
        text = font.render('Score: ' + str(self.points), 1, WHITE)
        self.win.blit(text, (20, 20))

    def draw_gameover(self):
        font = pygame.font.SysFont('comicsans', 40)
        text_1 = font.render('Game Over !', 1, WHITE)
        self.win.blit(text_1, (WIDTH // 2 - text_1.get_width() // 2, HEIGHT // 2 - text_1.get_height()))
        text_2 = font.render('Score: ' + str(self.points), 1, WHITE)
        self.win.blit(text_2, (WIDTH // 2 - text_2.get_width() // 2, HEIGHT // 2))
        pygame.display.update()
        pygame.time.delay(3000)

    def update(self):
        for pipe in self.pipes:
            if pipe.move():
                self.pipes.remove(pipe)
                self.pipes.append(Pipe(600 - PIPE_WIDTH // 2, random.choice(self.pipe_poses)))

        for base in self.bases:
            if base.move():
                self.bases.remove(base)
                self.bases.append(Base(3 * BASE.get_width() // 2, 835))

        if self.bird.jumping:
            self.bird.update_state()
        else:
            self.bird.state = 'middle_1'
        
        if self.gameover:
            self.draw_gameover()
            self.gameover = False
            self.create_bird()
            self.create_pipes()
            self.points = 0

        self.bird.gravity()
        self.check_collision()

    def create_pipes(self):
        START_POS = 450
        self.pipes = []
        self.pipes.append(Pipe(START_POS, random.choice(self.pipe_poses)))
        self.pipes.append(Pipe(START_POS + 300, random.choice(self.pipe_poses)))

    def create_bases(self):
        self.bases.append(Base(0, 835))
        self.bases.append(Base(BASE.get_width(), 835))

    def create_bird(self):
        self.bird = Bird(WIDTH // 2, HEIGHT // 2)

    def check_collision(self):
        if self.front_collision:
            self.gameover = True
            self.front_collision = False
            return
        
        if self.bird.y + BIRD_1.get_height() // 2 >= self.bases[0].y - BASE.get_height() // 2:
            self.bird.y = self.bases[0].y - BASE.get_height() // 2 - BIRD_1.get_height() // 2
            self.gameover = True
            return

        for pipe in self.pipes:
            if self.bird.x + BIRD_1.get_width() // 2 >= pipe.x - PIPE_WIDTH // 2 and \
                self.bird.x - BIRD_1.get_width() // 2 <= pipe.x + PIPE_WIDTH // 2:
                # upper pipe
                if self.bird.y - BIRD_1.get_height() // 2 <= pipe.height:
                    self.bird.y = pipe.height + BIRD_1.get_height() // 2
                    self.gameover = True
                    break

                # bottom pipe
                if self.bird.y + BIRD_1.get_height() // 2 >= pipe.height + GAP:
                    self.bird.y = pipe.height + GAP - BIRD_1.get_height() // 2
                    self.gameover = True
                    break
            
            # 100% front collision because of pipe.dX (1 frame before collision)
            if self.bird.x + BIRD_1.get_width() // 2 + pipe.dX >= pipe.x - PIPE_WIDTH // 2 and \
                self.bird.x - BIRD_1.get_width() // 2 <= pipe.x + PIPE_WIDTH // 2 and \
                (self.bird.y - BIRD_1.get_height() // 2 <= pipe.height or \
                    self.bird.y + BIRD_1.get_height() // 2 >= pipe.height + GAP):
                self.front_collision = True
                break

            if not pipe.checked and self.bird.x - BIRD_1.get_width() // 2 > pipe.x + PIPE_WIDTH // 2:
                pipe.checked = True
                self.points += 1
