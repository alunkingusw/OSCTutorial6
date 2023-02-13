import pygame
import socket

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (400, 300)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("PyGame Counter")

# Set the font for the counter
font = pygame.font.Font(None, 50)

# Initialize the counter
counter = 0

# Set the initial position of the counter
counter_pos = (200, 150)

# Set the color of the counter
counter_color = (255, 255, 255)

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind(("127.0.0.1", 12345))

# Start listening for incoming connections
server_socket.listen(1)

# Accept a connection
connection, address = server_socket.accept()

# Start the main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Receive data from the connection
    data = connection.recv(1024)

    # Decode the data
    data = data.decode()

    # Split the data into x and y coordinates
    x, y = map(int, data.split(","))

    # Set the position of the counter based on the received coordinates
    counter_pos = (x, y)

    # Clear the screen
    screen.fill((0, 0, 0))

    # Render the counter
    text = font.render(str(counter), True, counter_color)
    screen.blit(text, counter_pos)

    # Update the display
    pygame.display.update()

# Close the connection
connection.close()

# Quit Pygame
pygame.quit()
