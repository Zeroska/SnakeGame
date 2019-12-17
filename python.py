import pygame
import time
import random


#Cell is a node in snake body (the head is also a node in snakebody)
#If the snake hit the body 
#Snake Node = Cell
class Cell: 
    def __init__(self, Xcord,Ycord):
        self.Xcord = Xcord
        self.Ycord = Ycord
        self.next_cell = None

class SnakeLinkedList:
    def __init__(self):
        self.head_cell = None 

    def list_print(self):
        print_val = self.head_cell 
        while print_val is not None:
            print(print_val.Xcord)
            print(print_val.Ycord)
            print_val = print_val.next_cell

    #check snake status, one is None second is how many cell??? 
    #def check_whether_the_snake_status(self, someSnakeList):
    #    if self.head_cell == None:
    
    #def count_the_cell(self): 
    #    while self.head_cell != None:        
                            
    def count_cell(self, list):
        count = 0
        temp = self.head_cell
        while temp is not None:
            count += 1
            temp = temp.next_cell
        return count 


    def at_beginning(self, new_cell):
        NewCell = Cell(new_cell)
        self.head_cell = NewCell
         
    def at_end(self, new_Xcord, new_Ycord): 
        NewCell = Cell(new_Xcord,new_Ycord)
        if self.head_cell is None:
            self.head_cell = NewCell 
            return 
        last_cell = self.head_cell
        while(last_cell.next_cell):
            last_cell = last_cell.next_cell
        last_cell.next_cell= NewCell 

pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
dis_width = 800
dis_height = 600
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Python')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 20

 
font_style = pygame.font.SysFont("None", 25)
score_font = pygame.font.SysFont("None", 35)



#our snake consist of block(x,y) of the linked_list I have make
def our_snake(snake_block, snake_list): 
    temp = snake_list.head_cell
    
    while temp is not None:
        pygame.draw.rect(dis, green, [temp.Xcord, temp.Ycord, snake_block, snake_block])
        temp = temp.next_cell
    
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


#Read every Cell in SnakeLinkedList and took it cord to create a snake 
#
def createSnakeList(snake_block, snake):
    temp = snake.head_cell 
    while(temp.next_cell != None):  
        pygame.draw.rect(dis, green,[snake.cord[0],snake.cord[1],snake_block,snake_block])
         

#initial value for the snake 
#list = [[200,190],[200,180],[200,170]]
#



#Keep the game run until you lose 
def gameLoop():
    game_over = False  
    game_close = False
    
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
    #snake_cell = Cell(x1 , y1)
     
    snake_List = SnakeLinkedList() #it used to be snake_List = []  
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
        #while game is over choose whether play again or quit 
        # 
        while game_close == True:
            dis.fill(black)
            message("You Lost! Press C-Play Again or Q-Quit", red) 
            pygame.display.update()
        #pygame.event.get(): listen to key stroke and act upon it
        #event.type: what event is that in this mean KEYDOWN (Press down) 
        #event.key : key in your keyboard
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        #for event 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        #boundary checker if hit game close 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        #change the postion of the snake base on key pressed 
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        #draw the food 
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        #create a snakehead with plain 

        #snake_Head = [] This should replace using linked_listSnake 
        #X_cord , Y_cord for the snake 
        #Create first snake cell and add it to the end of snake list 
        snake_cell = Cell(x1 , y1)

        snake_List.at_end(snake_cell.Xcord, snake_cell.Ycord)
        


        #print out for track the head of the snake(Xcord, Ycord)
        snake_List.list_print()
        
        #snake_Head.append(x1) 
        #snake_Head.append(y1)

        #add snake_head with X_cord and Y_cord to the snake_List
        #snake_List.append(snake_Head)


        #if snake_list is bigger the len of snake 
        #if count_the_cell(snake_List) > Length_of_snake:
        #   del 
         
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        #our snake first block
        our_snake(snake_block, snake_List)
 
        #render all the thing we draw include our stupid snake 
        pygame.display.update()
        

        #If the snake hit the food it add one more cell the snake  
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            #keep trak of the snake lenght
            Length_of_snake += 1



        #Frame per second 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 


#Initial the game 
#Note: Should have try implement OOP stuff 
gameLoop()

