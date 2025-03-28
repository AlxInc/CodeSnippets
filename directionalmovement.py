import pygame
from pygame import Vector2
clock = pygame.time.Clock()

def move_toward(dt):
    movement_speed = 50
    direction = Vector2(player_x, player_y) - Vector2(target_x, target_y)
    distance = direction.length()
    if distance != 0:
        direction.normalize_ip()
        target_x += direction[0] * movement_speed * dt
        target_y += direction[1] * movement_speed * dt

while True:
    dt = clock.get_time() / 1000
    move_toward(dt)

    