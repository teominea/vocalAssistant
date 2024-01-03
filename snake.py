import pygame
import time
import random

def main():
    pygame.init()
    # Constants
    WIDTH, HEIGHT = 800, 600
    GRID_SIZE = 20
    SNAKE_SIZE = 20
    FPS = 5

    # Colors
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)

    # Initialize the display
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")

    # Snake initialization
    snake = [(WIDTH / 2, HEIGHT / 2)]
    snake_direction = (1, 0)

    # Food initialization
    food = (random.randrange(0, WIDTH, GRID_SIZE), random.randrange(0, HEIGHT, GRID_SIZE))

    # Score
    score = 0

    # Game loop
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != (0, 1):
                    snake_direction = (0, -1)
                elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                    snake_direction = (0, 1)
                elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                    snake_direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                    snake_direction = (1, 0)

        # Move the snake
        new_head = (snake[0][0] + snake_direction[0] * GRID_SIZE, snake[0][1] + snake_direction[1] * GRID_SIZE)
        snake.insert(0, new_head)

        # Check for collisions with the walls
        if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
            running = False

        # Check for collision with the food
        if new_head == food:
            score += 1
            food = (random.randrange(0, WIDTH, GRID_SIZE), random.randrange(0, HEIGHT, GRID_SIZE))
        else:
            # Remove the last part of the snake
            snake.pop()

        # Check for collision with itself
        if len(snake) != len(set(snake)):
            running = False

        # Draw everything
        screen.fill(WHITE)

        # Draw the snake
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

        # Draw the food
        pygame.draw.rect(screen, RED, (food[0], food[1], SNAKE_SIZE, SNAKE_SIZE))

        # Display the score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

        # Control the frame rate
        clock.tick(FPS)

    pygame.quit()

