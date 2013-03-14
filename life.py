import pygame, sys, time
from model import *
from view import *

class Life:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Life')
        self.screen = pygame.display.set_mode((510, 510))

        self.model = Model()
        self.model.insert_cell((0, -1))
        self.model.insert_cell((0, 0))
        self.model.insert_cell((0, 1))

        self.view = View(self.screen)
        self.view.draw_grid()
        self.view.draw_model(self.model)

    def input(self, events):
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.view.y0 -= 1
            self.view.draw_model(self.model)
            time.sleep(0.1)
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            self.view.y0 += 1
            self.view.draw_model(self.model)
            time.sleep(0.1)
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            self.view.x0 -= 1
            self.view.draw_model(self.model)
            time.sleep(0.1)
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.view.x0 += 1
            self.view.draw_model(self.model)
            time.sleep(0.1)

        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.model = self.model.next_gen()
                self.view.draw_model(self.model)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                self.model.clean()
                self.model.save_to_file("life.dat")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_l:
                self.model = Model.load_from_file("life.dat")
                self.view.draw_model(self.model)
            elif event.type == pygame.MOUSEBUTTONUP and event.button in [1, 3]:
                x, y = event.pos
                x = x // self.view.length + self.view.x0
                y = y // self.view.length + self.view.y0
                if event.button == 1:
                    self.model.insert_cell((x, y))
                else:
                    self.model.delete_cell((x, y))
                self.view.draw_model(self.model)

    def action(self):
        while 1:
            self.input(pygame.event.get())
            self.view.draw()

def main():
    life = Life()
    life.action()

if __name__ == '__main__': main()
