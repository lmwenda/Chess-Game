print("Starting script...")
import pygame
pygame.init()
print("Pygame initialized.")

screen = pygame.display.set_mode((800, 600))
print("Window created.")

# Your main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.display.flip()

pygame.quit()
print("Exited cleanly.")
