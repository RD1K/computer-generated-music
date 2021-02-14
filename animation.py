'''
This file is for the animation of the pianist.
'''

import pygame, sys

# path to animation frames
path = "/home/siddh/Documents/HackathonProject/AnimationFrames/"

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        for x in range(1,19):
            self.sprites.append(pygame.transform.scale((pygame.image.load(path + ("New Piskel-" + str(x) + ".png.png"))), (640, 360)))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]

    def animate(self):
        self.is_animating = True

    def update(self):
        if self.is_animating == True:
            self.current_sprite += 0.2
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
            self.image = self.sprites[int(self.current_sprite)]

# sets the main things up
pygame.init()
clock = pygame.time.Clock()

# sets up dimensions and other window properties
screen_width = 960
screen_height = 540
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Virtual Pianist")

moving_sprites = pygame.sprite.Group()
player = Player(100,100)
moving_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((122,122,122))
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()
    clock.tick(60)
