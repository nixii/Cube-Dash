
import pygame, asyncio

pygame.init()
screen = pygame.display.set_mode((800, 600))

running = True

async def main():
    global running
    while running:

        # event handling
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        await asyncio.sleep(0)

asyncio.run(main())