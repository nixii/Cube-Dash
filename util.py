
import pygame

def sign(n):
    if n<0: return -1
    if n>0: return 1
    return 0

def move_and_collide(ra: Rect, rb: Rect, movement: (int, int)) -> (int, int):
    horiz, vert = 0, 0
    ra.x += movement[0]
    if ra.colliderect(rb):
        horiz = sign(movement[0])
        if horiz == -1:
            ra.left = rb.right
        elif horiz == 1:
            ra.right = rb.left
    ra.y += movement[1]
    if ra.colliderect(rb):
        vert = sign(movement[1])
        if vert == -1:
            ra.top = rb.bottom
        elif vert == 1:
            ra.bottom = rb.top
    return (horiz, vert)