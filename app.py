
import pygame

class App():
    def __init__(self, x, y, scale, title) -> 'App':
        self.x = x
        self.y = y
        self.scale = scale
        self.title = title
        self.window = pygame.Surface((self.x, self.y))
        self.running = True
        pygame.init()
        self.screen = pygame.display.set_mode((self.x * self.scale, self.y * self.scale))
        pygame.display.set_caption(self.title)

        self.keys_down = []
        self.keys_just_down = []
        self.keys_just_up = []
    
    def update(self) -> None:
        self.keys_just_down = []
        self.keys_just_up = []
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.running = False
            elif e.type == pygame.KEYDOWN:
                self.keys_down.append(pygame.key.name(e.key))
                self.keys_just_down.append(pygame.key.name(e.key))
            elif e.type == pygame.KEYUP:
                self.keys_down.remove(pygame.key.name(e.key))
                self.keys_just_up.append(pygame.key.name(e.key))
    
    def render(self) -> None:
        self.screen.blit(pygame.transform.scale(self.window, (self.x * self.scale, self.y * self.scale)), (0, 0))
        pygame.display.flip()
        self.window.fill((0, 0, 0))