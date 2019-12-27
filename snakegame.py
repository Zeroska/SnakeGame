eximport pygame
import time
import random 


#Note for the game:
#   + setup the screen 
#   + create a dot first
#   + Detect key press
#   + make it move 
#   + adjust its speed 
#   + boudary
#   + create food for the snake (target must be random) range from the 800x600
#   dimenstion
#   + after snake eat the food, it will increase it lenght
#   + Losing condition: 
#       * Hit border
#       * Hit yourself 

def main():
    screen_width  = 800 
    screen_height = 600 
    #--------------------------------------------------------
    #Global varibles
    x1 = screen_width/2 #x and y of the snake first position 
    y1 = screen_height/2 

    x1_change = 0 #x and y change when the the player press the damn key 
    y1_change = 0
    snake_speed = pygame.time.Clock()
    #if you don't have this the snake will run like hell
    #super fast, I don't know the basesnaek  frame of this pro
    frame_per_second = 35
    #---------------------------------------------------------
    #create a list of color for later uses 
    green = (0,255,0)
    blue = (0,0,255)
    red = (255,0,0)
    black = (0,0,0)
    white = (255,255,255)
    #--------------------------------------------------------


    #linked list in python3
    #so what is linked list
#[data][pointToNextNode]





#Create a snake object 
class Snake:
    def __init__(self,x,y screen): #this is a method or constructor 
        self.x = x
        self.y = y
        self.screen = screen  
        self.nextval = None

    def grow(self,XYcord):
        snake_node = Snake(XYcord)
        snake_node.set_next(self.head)
        self.head = snake_node

class Food:
    def __init__(self, screen)
        self. 




game_font = pygame.font.SysFont(None,30)

def message(msg):    
    msg = game_font.render(msg,True,green)
    screen.blit(msg,[screen_width/3,screen_height/2])

#this look like a game loop (for me)
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over=True
        if event.type == pygame.KEYDOWN:    #listen to event "key press down" 
            if event.key == pygame.K_LEFT:  #LEFT key pressed
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT: #RIGHT key pressed 
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP: #UP key pressed  
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN: #DOWN key pressed
                x1_change = 0
                y1_change = 10
    x1 += x1_change
    y1 += y1_change
    print("x = " + str(x1))
    print("y = " + str(y1))
    screen.fill(black)
    print(snake_speed)
     
     
    pygame.draw.rect(screen,green,[x1,y1,10,10])
    pygame.draw.rect(screen,green,[x1 - x1_change ,y1 - y1_change,10,10])
    pygame.draw.rect(screen,green,[x1 - 2*x1_change ,y1 - 2*y1_change,10,10])
    #the boudary checker 
    if (x1 < screen_width and y1 > screen_height) or (x1 > screen_width and y1
< screen_height) or (x1 > screen_width and y1 > screen_height) or (x1 < 0) or (y1 < 0):
        game_over = True
    pygame.display.update()
    snake_speed.tick(frame_per_second)


message('FUCKING LOSER!')
pygame.display.update() 
time.sleep(2)
pygame.quit()
quit()
def setup_the_game():
    #setup for the screen and the board
    pygame.init()
    #screen 800x600
    screen = pygame.display.set_mode((screen_width,screen_height))
    #update the hold screen if no agrument passed
    pygame.display.update() 
    pygame.display.set_caption('Not Python') #the title for Zeroska 
    game_over = False 


def render_the_snake(snake_position):
    for position in snake_position:
        pygame.draw.rect(screen,green,[])


def collision_with_border(snake_head_cord):
    if snake_head[0] 

def collision_with_self(snake_position):
