
import pygame, asyncio, random

# Constants
GRAVITY = 3
W_WIDTH = 800
W_HEIGHT = 600
PIPE_SPEED = 150

# initialize pygame
pygame.init()
screen = pygame.display.set_mode((W_WIDTH, W_HEIGHT))
pygame.display.set_caption("Cube Dash")
ticks = pygame.time.get_ticks()
fontL = pygame.font.Font('Font.ttf', 64)
fontS = pygame.font.Font('Font.ttf', 32)

# prerender text
txt_GameTitle = fontL.render('Cube Dash', True, (255, 255, 255))
txt_Instructions = [
    fontS.render(a, True, (255, 255, 255)) for a in [
        'Your goal is to get to the other',
        '  side of the screen.',
        'Tap any button to jump.',
        'When you pass a pipe, you move',
        '  forwards.',
        'Press any key to start!'
    ]
]
txt_YouWin = fontL.render('You have won!', True, (255, 255, 255))
txt_ReplayInstructions = fontS.render('To replay, press any key.', True, (255, 255, 255))

# Is the app running?
running = True

# Player input
key = False
will_dash = False

# Create the player entity
player = pygame.Rect(0, 200, 40, 40)
yvel = 0
player_x = 0
died = False

# Game state
gs = 2

# "pipes"
pipes = []
pipe_timer = 0

# Pipe class
class Pipe():
    def __init__(self, y):
        self.x = W_WIDTH
        self.y = y
        self.r1 = pygame.Rect(self.x, 0, 80, y - 130)
        self.r2 = pygame.Rect(self.x, y + 130, 80, W_HEIGHT - y - 130)
        self.counted = False
    def render(self):
        self.r1.x = self.x
        self.r2.x = self.x
        pygame.draw.rect(screen, (255, 0, 0), self.r1)
        pygame.draw.rect(screen, (255, 0, 0), self.r2)
    def collides(self,pl)->bool:
        return pygame.Rect.colliderect(pl,self.r1) or pygame.Rect.colliderect(pl,self.r2)

# spawn a pipe
def spawn_pipe():
    global pipes
    p = Pipe(random.randint(80, W_HEIGHT - 80))
    pipes.append(p)
    print(p.y)

# Update the game
async def main():
    global running, will_dash, key, yvel, ticks, gs, pipe_timer, died

    # While it is running
    while running:

        ###########
        ### DT calc
        t = pygame.time.get_ticks()
        dt = (t - ticks) / 1000.0
        ticks = t

        # spawn a pipe
        pipe_timer -= dt
        if pipe_timer <= 0:
            spawn_pipe()
            pipe_timer = 2

        # input
        key = False
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.KEYDOWN:
                key = True

        #################################
        ### Update if the game is running
        if gs == 1:
            
            if not died:
                # gravity
                yvel += GRAVITY

                # key press
                if key:
                    yvel = -500
                
                # update position
                player.y += yvel * dt

                # check y death
                if player.y > W_HEIGHT-20 or player.y < -20:
                    died = True

                # update pipes
                for p in pipes:
                    p.x -= PIPE_SPEED * dt
                    if p.x < player.x - p.r1.width and not p.counted:
                        player.x += 40
                        p.counted = True
                    if p.collides(player):
                        died = True
    
        ################
        ### Clear screen
        screen.fill((0, 0, 0))

        ##################
        ### Render in-game
        if gs == 1:

            # Player
            pygame.draw.rect(screen, (255, 255, 255), player)

            # Render pipes
            for p in pipes:
                p.render()
        
        ####################
        ### Render main menu
        elif gs == 0:
            screen.blit(txt_GameTitle, (40, 40))
            i = 0
            for t in txt_Instructions:
                screen.blit(t, (40, 108 + 40 * i))
                i+=1
        
        #############
        ## Win screen
        elif gs == 2:
            screen.blit(txt_YouWin, (40, 40))
            screen.blit(txt_ReplayInstructions, (40, 108))

        ###########
        ### Flip and await (since this will run in the browser)
        pygame.display.flip()
        await asyncio.sleep(0)

# Run!
asyncio.run(main())