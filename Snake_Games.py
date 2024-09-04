import pygame
import random

# Initialize Pygame
pygame.init()

window_width = 800  
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")  # Set the title of the window

# Set up the game clock to control the frame rate
clock = pygame.time.Clock()

running = True

snake = [{'x': 10, 'y': 10}, {'x': 9, 'y': 10}, {'x': 8, 'y': 10}]
snake_direction = 'RIGHT'
snake_color = (0, 255, 0)

# Function to generate food
def generate_food():
    food_x = random.randint(0, (window_width // 20) - 1)
    food_y = random.randint(0, (window_height // 20) - 1)
    return {'x': food_x, 'y': food_y}

food = generate_food()

score = 0  # Initialize the score

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_direction = 'UP'
            elif event.key == pygame.K_DOWN:
                snake_direction = 'DOWN'
            elif event.key == pygame.K_LEFT:
                snake_direction = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                snake_direction = 'RIGHT'

    # Update the snake's position based on its current direction
    if snake_direction == 'UP':
        new_head = {'x': snake[0]['x'], 'y': snake[0]['y'] - 1}
    elif snake_direction == 'DOWN':
        new_head = {'x': snake[0]['x'], 'y': snake[0]['y'] + 1}
    elif snake_direction == 'LEFT':
        new_head = {'x': snake[0]['x'] - 1, 'y': snake[0]['y']}
    elif snake_direction == 'RIGHT':
        new_head = {'x': snake[0]['x'] + 1, 'y': snake[0]['y']}

    # Insert the new head at the beginning of the snake list
    snake.insert(0, new_head)

    # Check for collisions with the game boundaries or the snake's own body
    if (snake[0]['x'] < 0 or snake[0]['x'] >= window_width // 20 or
        snake[0]['y'] < 0 or snake[0]['y'] >= window_height // 20 or
        new_head in snake[1:]):
        running = False
    if new_head == food:
        snake.append({'x': snake[-1]['x'], 'y': snake[-1]['y']})
        food = generate_food()
        score += 1
    del snake[-1]

    # Render graphics (draw everything on the screen)
    window.fill((0, 0, 0))
    for segment in snake:
        pygame.draw.rect(window, snake_color, (segment['x'] * 20, segment['y'] * 20, 20, 20))
    pygame.draw.rect(window, (255, 0, 0), (food['x'] * 20, food['y'] * 20, 20, 20))

    # Render the score text
    score_font = pygame.font.Font(None, 24)
    score_text = score_font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(score_text, (10, 10))

    pygame.display.flip()  # Update the display

    clock.tick(6)

# Display the game over message and final score
game_over_font = pygame.font.Font(None, 36)
game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))
score_text = score_font.render("Final Score: " + str(score), True, (255, 255, 255))
window.blit(game_over_text, (window_width // 2 - game_over_text.get_width() // 2, window_height // 2 - game_over_text.get_height() // 2 - 50))
window.blit(score_text, (window_width // 2 - score_text.get_width() // 2, window_height // 2 - score_text.get_height() // 2 + 50))

pygame.display.flip()  # Update the display

pygame.time.wait(5000)

pygame.quit()
