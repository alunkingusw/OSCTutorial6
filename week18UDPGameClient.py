import pygame
import socket

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (400, 300)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("PyGame Keyboard Counter")

# Set the font for the counter
font = pygame.font.Font(None, 50)

# Initialize the counter
counter = 0

# Set the initial position of the counter
counter_pos_x = 200
counter_pos_y = 150

# Set the color of the counter
counter_color = (255, 255, 255)

# Set the speed of the counter
counter_speed = 5

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Start the main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                counter_pos_y -= counter_speed
            if event.key == pygame.K_DOWN:
                counter_pos_y += counter_speed
            if event.key == pygame.K_LEFT:
                counter_pos_x -= counter_speed
            if event.key == pygame.K_RIGHT:
                counter_pos_x += counter_speed
    
    # Encode the counter position as a string
    data = f"{counter_pos_x},{counter_pos_y}"

    # Send the data to the other program
    sock.sendto(data.encode(), ("127.0.0.1", 12345))

    # Clear the screen
    screen.fill((0, 0, 0))

    # Render the counter
    text = font.render(str(counter), True, counter_color)
    screen.blit(text, (counter_pos_x, counter_pos_y))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
