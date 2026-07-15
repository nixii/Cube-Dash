
import pygame, app

class Entity():
    def __init__(self, x, y, w, h, col):
        self.rect = pygame.Rect(x, y, w, h)
        self.col = col
        self.velocity = (0, 0)
    
    def update(self, ) -> None:
        pass

    def render(self, a: app.App) -> None:
        pygame.draw.rect(a.window, self.col, self.rect)