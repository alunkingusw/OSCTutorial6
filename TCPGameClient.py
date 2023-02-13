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
counter_pos = (200, 150)

# Set the color of the counter
counter_color = (255, 255, 255)

# Set the speed of the counter
counter_speed = 5

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(("127.0.0.1", 12345))

# Start the main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current key state
    keys = pygame.key.get_pressed()

    # Move the counter based on the arrow keys
    if keys[pygame.K_UP]:
        counter_pos = (counter_pos[0], counter_pos[1] - counter_speed)
    if keys[pygame.K_DOWN]:
        counter_pos = (counter_pos[0], counter_pos[1] + counter_speed)
    if keys[pygame.K_LEFT]:
        counter_pos = (counter_pos[0] - counter_speed, counter_pos[1])
    if keys[pygame.K_RIGHT]:
        counter_pos = (counter_pos[0] + counter_speed, counter_pos[1])

    # Send the position of the counter to the PyGame program
    data = f"{counter_pos[0]},{counter_pos[1]}"
    client_socket.send(data.encode())

    # Clear the screen
    screen.fill((0, 0, 0))

    # Render the counter
    text = font.render(str(counter), True, counter_color)
    screen.blit(text, counter_pos)

    # Update the display
    pygame.display.update()

# Close the connection
client_socket.close()

# Quit Pygame
pygame.quit()
