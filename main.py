import pygame
import imageio
import numpy as np
import math
(width, height) = (500, 500)
pygame.init()
screen = pygame.display.set_mode((width, height))
gif_path = "kop.gif"
gif_reader = imageio.get_reader(gif_path)
gif_frames = [np.array(frame)[:, :, :3] for frame in gif_reader]
triangle_side = 300
center_x, center_y = width // 2, height // 2
triangle_height = (math.sqrt(3) / 2) * triangle_side
triangle_top = (center_x, center_y - triangle_height / 2)
triangle_left = (center_x - triangle_side / 2, center_y + triangle_height / 2)
triangle_right = (center_x + triangle_side / 2, center_y + triangle_height / 2)
polygon = [triangle_top, triangle_right, triangle_left]
clock = pygame.time.Clock()
frame_index = 0
running = True
paused = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
    if not paused:
        frame = pygame.surfarray.make_surface(gif_frames[frame_index])
        screen.blit(frame, (0, 0))
        white_color = (255, 255, 255)
        mask_surface = pygame.Surface((width, height))
        pygame.draw.polygon(mask_surface, white_color, polygon)
        pygame.draw.aalines(mask_surface, white_color, True, polygon)
        screen.blit(mask_surface, (0, 0), None, pygame.BLEND_RGBA_MULT)
        pygame.display.flip()
        frame_index = (frame_index + 1) % len(gif_frames)
    clock.tick(50)
pygame.quit()
