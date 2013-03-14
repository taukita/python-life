import pygame
from model import *

class View:
    def __init__(self, screen):
        self.screen = screen
        self.grid_surface = pygame.Surface(screen.get_size())
        self.grid_surface = self.grid_surface.convert()
        self.cell_surface = pygame.Surface(screen.get_size(), flags = pygame.SRCALPHA)
        self.cell_surface = self.cell_surface.convert_alpha()
        self.length = 10
        self.grid_color = (189, 183, 107)
        self.cell_color = (50, 205, 50)
        self.x0 = -25
        self.y0 = -25

    def draw_grid(self):
        self.grid_surface.fill((255, 255, 255))
        w, h = self.grid_surface.get_width(), self.grid_surface.get_height()
        x = 0
        while x < w:
            pygame.draw.line(self.grid_surface, self.grid_color, (x, 0), (x, h))
            x += self.length
        y = 0
        while y < h:
            pygame.draw.line(self.grid_surface, self.grid_color, (0, y), (w, y))
            y += self.length

    def draw_cell(self, posn):
        x, y = posn
        x -= self.x0
        y -= self.y0
        pygame.draw.rect(self.cell_surface, self.cell_color, (x*self.length + 1, y*self.length + 1, self.length - 1, self.length - 1))

    def draw_model(self, model):
        self.cell_surface.fill((255, 255, 255, 0))
        for posn in iter(model.cells):
            c1, c2 = model.cells[posn]
            if c1:
                self.draw_cell(posn)

    def draw(self):
        self.screen.blit(self.grid_surface, (0, 0))
        self.screen.blit(self.cell_surface, (0, 0))
        pygame.display.flip()        
