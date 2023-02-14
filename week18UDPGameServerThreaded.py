import pygame
import socket

# import the threading module
import threading

mutex = threading.Semaphore(value=1)
 
# Initialize the counter
running = True

counters = {}

#create the UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#set up the thread to start listening
class thread(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)

        # Bind the socket to a specific address and port
        sock.bind(("127.0.0.1", 12345))
        
        # helper function to execute the threads
    def run(self):
        while running:
            # Receive data from the socket
            data, address = sock.recvfrom(1024)
            # Decode the received data
            coordinates = data.decode().split(",")
            #print(data.decode())
            # Update the position of the counter based on the received coordinates
            mutex.acquire()
            counters[address] = (int(coordinates[0]), int(coordinates[1]))
            mutex.release()
 
socketListener = thread()
socketListener.daemon = True
 


 

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (400, 300)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("PyGame UDP Server Threaded")

# Set the font for the counter
font = pygame.font.Font(None, 50)


# Set the color of the counters
counter_color = (255, 255, 255)

socketListener.start()

# Start the main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Render the counter
    mutex.acquire()
    for i, counter_pos in enumerate(counters):
        text = font.render(str(i), True, counter_color)
    
        screen.blit(text, counters[counter_pos])
    mutex.release()
    
    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
