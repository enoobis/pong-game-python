import pygame

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (400, 300)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Pong")

# Set the dimensions of the game objects
paddle_width = 15
paddle_height = 60
ball_radius = 5

# Set the initial positions of the game objects
paddle1_pos = [0, (300 - paddle_height) / 2]
paddle2_pos = [385, (300 - paddle_height) / 2]
ball_pos = [200, 150]

# Set the initial velocities of the game objects
paddle1_vel = [0, 0]
paddle2_vel = [0, 0]
ball_vel = [5, 5]

# Set the initial scores
score1 = 0
score2 = 0

# Set the maximum score to end the game
max_score = 5

# Set the frame rate
frame_rate = 60

# Set the colors
black = (0, 0, 0)
white = (255, 255, 255)

# Run the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the keys pressed
    keys = pygame.key.get_pressed()

    # Move the paddles based on the keys pressed
    if keys[pygame.K_w]:
        paddle1_vel[1] = -5
    elif keys[pygame.K_s]:
        paddle1_vel[1] = 5
    else:
        paddle1_vel[1] = 0

    if keys[pygame.K_UP]:
        paddle2_vel[1] = -5
    elif keys[pygame.K_DOWN]:
        paddle2_vel[1] = 5
    else:
        paddle2_vel[1] = 0

    # Update the positions of the game objects
    paddle1_pos[1] += paddle1_vel[1]
    paddle2_pos[1] += paddle2_vel[1]
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # Keep the paddles on the screen
    if paddle1_pos[1] < 0:
        paddle1_pos[1] = 0
    elif paddle1_pos[1] > 300 - paddle_height:
        paddle1_pos[1] = 300 - paddle_height

    if paddle2_pos[1] < 0:
        paddle2_pos[1] = 0
    elif paddle2_pos[1] > 300 - paddle_height:
        paddle2_pos[1] = 300 - paddle_height

    # Keep the ball on the screen and change its velocity if it hits a wall
    if ball_pos[1] < 0 or ball_pos[1] > 300 - ball_radius * 2:
        ball_vel[1] = -ball_vel[1]
    
    # Check if the ball hits a paddle and change its velocity
    if ball_pos[0] < paddle_width and paddle1_pos[1] < ball_pos[1] < paddle1_pos[1] + paddle_height:
        ball_vel[0] = -ball_vel[0]
    elif ball_pos[0] > 400 - paddle_width - ball_radius * 2 and paddle2_pos[1] < ball_pos[1] < paddle2_pos[1] + paddle_height:
        ball_vel[0] = -ball_vel[0]
    
    # Check if the ball goes off the screen and update the scores
    if ball_pos[0] < 0:
        score2 += 1
        ball_pos = [200, 150]
        ball_vel = [5, 5]
    elif ball_pos[0] > 400 - ball_radius * 2:
        score1 += 1
        ball_pos = [200, 150]
        ball_vel = [-5, -5]
    
    # Check if either player has reached the maximum score and end the game if one of them has
    if score1 == max_score or score2 == max_score:
        game_over = True
        break
    
    # Clear the screen
    screen.fill(black)
    
    # Draw the paddles and the ball
    pygame.draw.rect(screen, white, (paddle1_pos[0], paddle1_pos[1], paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (paddle2_pos[0], paddle2_pos[1], paddle_width, paddle_height))
    pygame.draw.circle(screen, white, (int(ball_pos[0] + ball_radius), int(ball_pos[1] + ball_radius)), ball_radius)
    
    # Draw the scores
    font = pygame.font.Font(None, 36)
    text = font.render(str(score1), 1, white)
    screen.blit(text, (150, 10))
    text = font.render(str(score2), 1, white)
    screen.blit(text, (250, 10))
    
    # Update the screen
    pygame.display.flip()
    
    # Set the frame rate
    clock = pygame.time.Clock()
    clock.tick(frame_rate)

# Display the game over screen
if game_over:
    screen.fill(black)
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over", 1, white)
    screen.blit(text, (150, 150))
    pygame.display.flip()

# Wait for the user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()