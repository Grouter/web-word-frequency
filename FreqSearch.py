import pygame
import sys
import random
from pygame.locals import *


class FqVis:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((1000, 800))
        pygame.display.set_caption("Frq")
        pygame.font.init()
        self.font = pygame.font.SysFont('DejaVu', 30)
        self.clock = pygame.time.Clock()
        self.data_vis = []

    def insert_sorted_data(self, fq_data, count=10):
        my_data = fq_data[:count]
        w, h = pygame.display.get_surface().get_size()
        for i in range(len(my_data)):
            self.data_vis.append(WordRect(
                self.font.render("{0} : {1}".format(my_data[i][0], my_data[i][1]), True, (0, 0, 0)),
                (h/count) * i,
                h/count,
                w * (my_data[i][1]/my_data[0][1])
            ))

    def draw_data(self):
        for w in self.data_vis:
            w.draw(self.display)

    def update(self, delta):
        pass

    def render(self):
        pass

    def run(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # self.display.fill((125, 125, 125))
        # d = self.clock.tick_busy_loop(60)/25
        # self.update(d)
        # self.render()
        pygame.display.update()


class WordRect:
    def __init__(self, key_font, y, height, width):
        self.body = pygame.Rect(0, y, width, height)
        self.text = key_font
        self.color = (random.randrange(50, 255), random.randrange(50, 255), random.randrange(50, 255))

    def draw(self, display):
        pygame.draw.rect(display, self.color, self.body)
        display.blit(self.text, (10, self.body.top + self.body.height/2))
