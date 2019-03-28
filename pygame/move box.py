import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))  # create window. oh no flashbacks to tkinter

pygame.display.set_caption("Test") # its more of a title than a caption

# sprite attributes
x = 250
y = 250  # i assume these are the possition
width = 30
height = 30  # dimensions of sprite i assume
vel = 5  # velocity of sprite

run = True
while run:  # main loop
    pygame.time.delay(int((1/30)*1000))  # i guess this is a bit like sleep to slow things down (in ms)

    # check for events (user interactions)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if close button pressed
            run = False

    keys = pygame.key.get_pressed()  # get list of pressed keys

    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and x > vel:
        x -= vel
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and x < 500 - width - vel:
        x += vel
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and y > vel:
        y -= vel
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and y < 500 - height - vel:
        y += vel
    if keys[pygame.K_SPACE]:
        if vel < 50:  # limit velocity
             vel *= 1.1  # inrease velocity
    if not keys[pygame.K_SPACE]:  # if not speeding up
        if vel > 5:
            vel *= 0.8

    win.fill((0,0,0))  # clear the screen
    # draw sprite
    # first window to add to, then colour (rgb), then a 'rect'
    pygame.draw.rect(win, (255, 0, 0), (x,y,width,height))  # rect changes depending on shape

    pygame.display.update()  # update screen with new stuffs

pygame.quit()  # end program
