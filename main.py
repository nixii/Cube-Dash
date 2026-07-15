
import pygame, asyncio
import app, util

app = app.App(800, 600, 1, "oo")
player = pygame.Rect(0, 0, 40, 40)
e = pygame.Rect(60, 60, 40, 40)

async def main():
    global app
    while app.running:
        app.update()
        app.render()
        await asyncio.sleep(0)

asyncio.run(main())