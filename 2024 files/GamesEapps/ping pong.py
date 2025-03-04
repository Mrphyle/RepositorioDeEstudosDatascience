import pygame
import sys

# Initialize pygame
pygame.init()

# Set screen dimensions
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ping Pong Game")

# Set colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set paddles and ball dimensions
paddle_width, paddle_height = 10, 100
ball_size = 20

# Set initial positions
left_paddle_x, right_paddle_x = 20, screen_width - 30
left_paddle_y, right_paddle_y = screen_height // 2, screen_height // 2
ball_x, ball_y = screen_width // 2, screen_height // 2

# Set initial velocities
left_paddle_velocity, right_paddle_velocity = 0, 0
ball_velocity_x, ball_velocity_y = 5, 5

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update paddle positions
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left_paddle_y -= 5
    if keys[pygame.K_s]:
        left_paddle_y += 5
    if keys[pygame.K_UP]:
        right_paddle_y -= 5
    if keys[pygame.K_DOWN]:
        right_paddle_y += 5

    # Update ball position
    ball_x += ball_velocity_x
    ball_y += ball_velocity_y

    # Bounce ball off top and bottom walls
    if ball_y <= 0 or ball_y >= screen_height - ball_size:
        ball_velocity_y *= -1

    # Bounce ball off paddles
    if left_paddle_y <= ball_y <= left_paddle_y + paddle_height and ball_x <= left_paddle_x + paddle_width:
        ball_velocity_x *= -1
    if right_paddle_y <= ball_y <= right_paddle_y + paddle_height and ball_x >= right_paddle_x - paddle_width:
        ball_velocity_x *= -1

    # Draw paddles and ball
    screen.fill(white)
    pygame.draw.rect(screen, black, (left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, black, (right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, black, (ball_x, ball_y), ball_size)

    # Update display
    pygame.display.flip()

    # Set frame rate
    pygame.time.Clock().tick(60)