import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Glowing Orb Animation")

# Colors
BLACK = (0, 0, 0)
BASE_COLOR = (50, 200, 255)

# Orb properties
CENTER = (WIDTH // 2, HEIGHT // 2)
MAX_RADIUS = 150
PULSE_SPEED = 0.05  # Controls the speed of pulsing

# Helper function to generate glowing colors
def glowing_color(base_color, intensity):
    return tuple(min(255, max(0, int(channel * intensity))) for channel in base_color)

# Main loop
running = True
clock = pygame.time.Clock()
frame_count = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Calculate pulsating radius and color
    radius = MAX_RADIUS + int(20 * math.sin(frame_count * PULSE_SPEED))
    intensity = 0.7 + 0.3 * math.sin(frame_count * PULSE_SPEED * 1.5)
    color = glowing_color(BASE_COLOR, intensity)

    # Draw the orb
    pygame.draw.circle(screen, color, CENTER, radius)

    # Add glowing effect with smaller circles
    for i in range(1, 10):
        fade_radius = radius - i * 10
        if fade_radius > 0:
            fade_color = glowing_color(color, 0.8 - i * 0.08)
            pygame.draw.circle(screen, fade_color, CENTER, fade_radius)

    # Update the display
    pygame.display.flip()
    frame_count += 1
    clock.tick(60)  # Maintain 60 FPS

# Quit Pygame
pygame.quit()
