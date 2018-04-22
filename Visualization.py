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
        self.data = []

    def insert_sorted_data(self, fq_data):
        w, h = pygame.display.get_surface().get_size()
        for i in range(len(fq_data)):
            self.data.append(WordRect(
                self.font.render("{0} : {1}".format(fq_data[i][0], fq_data[i][1]), True, (0, 0, 0)),
                h / len(fq_data) * i,
                h / len(fq_data),
                w * (fq_data[i][1] / fq_data[0][1])
            ))

    def draw_data(self):
        for w in self.data:
            w.draw(self.display)

    def run(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        for w in self.data:
            w.widen()

        self.display.fill((255, 255, 255))
        self.draw_data()
        pygame.display.update()


class WordRect:
    def __init__(self, key_font, y, height, width):
        self.target_len = width
        self.velocity = self.target_len / 60
        self.body = pygame.Rect(0, y, 1, height)
        self.text = key_font
        self.color = (random.randrange(50, 200), random.randrange(50, 200), random.randrange(50, 200))

    def widen(self):
        if self.body.width < self.target_len:
            self.body.width += self.velocity

    def draw(self, display):
        pygame.draw.rect(display, self.color, self.body)
        display.blit(self.text, (10, self.body.top + self.body.height / 2))

    def mouse_over(self):
        pass
