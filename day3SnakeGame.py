
#Cell = Node, SnakeLinkedList = Linked-list_print
#[] -> [] -> [] -> None
#Each '->' is point to another Cell 
#

class Cell:
    def __init__(self, cord=None):
        self.cord = cord
        self.next_cell = None 

class SnakeLinkedList:
    def __init__(self):
        self.head_cell = None 
 
    def list_print(self):
        print_val = self.head_cell 
        while print_val is not None:
            print(print_val.cord)
            print_val = print_val.next_cell

    def AtEnd(self, new_cell): 
        NewCell = Cell(new_cell)
        if self.head_cell is None:
            self.head_cell = NewCell 
            return 
        last_cell = self.head_cell
        while(last_cell.next_cell):
            last_cell = last_cell.next_cell
        last_cell.next_cell= NewCell  





Snake = SnakeLinkedList()

Snake.head_cell = Cell([120,200])
Snake2 = Cell([130,200]) 
Snake3 = Cell([140,200])


Snake.head_cell.next_cell = Snake2
Snake2.next_cell = Snake3

Snake.AtEnd([150,200])
Snake.list_print()
    
