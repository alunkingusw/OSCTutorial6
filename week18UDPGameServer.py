import pygame
import socket

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (400, 300)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("PyGame UDP Counter")

# Set the font for the counter
font = pygame.font.Font(None, 50)

# Initialize the counter
counter = 0

# Set the initial position of the counter
counter_pos = (200, 150)

# Set the color of the counter
counter_color = (255, 255, 255)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port
sock.bind(("127.0.0.1", 12345))

# Start the main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Receive data from the socket
    data, address = sock.recvfrom(1024)
    # Decode the received data
    coordinates = data.decode().split(",")

    # Update the position of the counter based on the received coordinates
    counter_pos = (int(coordinates[0]), int(coordinates[1]))

    # Clear the screen
    screen.fill((0, 0, 0))

    # Render the counter
    text = font.render(str(counter), True, counter_color)
    screen.blit(text, counter_pos)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
