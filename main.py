
import pygame, asyncio
import app, util

app = app.App(800, 600, 1, "oo")
player = pygame.Rect(0, 0, 40, 40)
e = pygame.Rect(60, 60, 40, 40)

async def main():
    global app
    while app.running:
        app.update()

        mov = [0, 0]
        if 'a' in app.keys_down:
            mov[0] = -1
        if 'd' in app.keys_down:
            mov[0] = 1
        if 'w' in app.keys_down:
            mov[1] = -1
        if 's' in app.keys_down:
            mov[1] = 1
    
        dirs = util.move_and_collide(player, e, mov)

        pygame.draw.rect(app.window, (255, 0, 255), player)
        pygame.draw.rect(app.window, (255, 0, 255), e)
        app.render()
        await asyncio.sleep(0)

asyncio.run(main())