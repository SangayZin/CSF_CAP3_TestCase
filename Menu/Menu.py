import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

Screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')

#load button images
start_img = pygame.image.load('/home/sangay/Desktop/Survival Shootout/Menu/Start-Button-Vector-PNG.png').convert_alpha() 
exit_img = pygame.image.load('/home/sangay/Desktop/Survival Shootout/Menu/Untitled.png').convert_alpha()


#button class
class Button:
    def __init__(self, x, y, image, scale, callback, callback_args=None):
        width, height = image.get_width(), image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.callback = callback
        self.callback_args = callback_args

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_clicked(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.clicked = True
            if self.callback:
                if self.callback_args is not None:
                    self.callback(*self.callback_args)
                else:
                    self.callback()
            return True
        return False



        #get mouse position
        pos = pygame.mouse.get_pos()
    

        #check mouseover and clicked conditions
        if self.rect.collidepoint (pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:              
                self.clicked = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False    


       
       
        #draw button on screen
        Screen.blit(self.image,(self.rect.x, self.rect.y))

        return action

#create button instances
start_button = Button(100, 100, start_img, 0.5)
exit_button = Button(400, 100, exit_img, 0.5)


#game loop
run = True
x = 100  # Initial x position of the rectangle
y = 100  # Initial y position of the rectangle


def game_logic():
    # Replace this function with your actual game logic
    print("The game has started!")

while run:

    Screen.fill((0, 0, 0))

    if start_button.draw():
        print('START')

    if start_button.draw():
        game_logic()  # Call the game logic function when the "START" button is clicked    


    if  exit_button.draw():
        run = False
        print('EXIT')

    # Render and display the welcome message
    font = pygame.font.Font(None, 56)
    welcome_text = font.render("WellCome to Survival Shootout ", True, (255, 255, 255))
    welcome_rect = welcome_text.get_rect()
    welcome_rect.center = (SCREEN_WIDTH // 2, 450)
    Screen.blit(welcome_text, welcome_rect)



    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

   # Update the display
    pygame.display.update()

pygame.quit()