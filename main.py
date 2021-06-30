
import pygame
from fb.constants import WIDTH, HEIGHT
from fb.game import Game

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird v1.0 by AW')
FPS = 30

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.bird.jump()

        game.update()
        game.render()

main()
pygame.quit()
