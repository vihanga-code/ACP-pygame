import pygame

pygame.init()

# Set screen dimensions

screen_width, screen_height = 500,500

screen = pygame.display.set_mode((screen_width, screen_height))

# Set window caption

pygame.display.set_caption("Adding Images")

# Load and scale images

background = pygame.transform.scale(pygame.image.load("download.jpg").convert(), (300,300))


# Get the panda's rectangle and position it in the center


done = False

clock = pygame.time.Clock()

# Main loop

while not done:

   for event in pygame.event.get():

         if event.type == pygame.QUIT:

           done = True

# Blit images onto the screen

   screen.blit(background, (0, 0))

   

# Update the display

   pygame.display.flip()

# Control the frame rate

   clock.tick(30)

# Quit pygame

pygame.quit()