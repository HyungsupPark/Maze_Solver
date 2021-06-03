###############################################
# APS106 Winter 2020 - Lab 9 - Maze Solver v2 #
###############################################

###########################################
# PART 1 - Create the Stack Class         #
###########################################

class Node:
    """
    Node object for LinkedList
    """
    
    def __init__(self,cargo=None,next=None):
        """        
        Create and initialize a Node object
        
        Note: YOU DO NOT NEED TO EDIT THIS METHOD
        """
        self.cargo = cargo
        self.next = next

    def __str__(self):
        """
        (Node) -> str
        
        Return a string representation of the node
        
        You may use this to print a visualization of a node
        
        Note: YOU DO NOT NEED TO EDIT THIS METHOD
        """

        neighbours_explored = ''
        for n in self.cargo[1]:
            if self.cargo[1][n]:
                neighbours_explored += (n + ' ')
                
        box_width = len("Neighbours Explored: ")
        pad1 = box_width - len("Coordinate Node")
        pad2 = box_width - len("Coordinate: ") - len(str(self.cargo[0]))
        pad3 = box_width - len(neighbours_explored)
        
        s = ('+' + '-'*box_width + '+\n' +
             '|' + 'Coordinate Node' + ' '*pad1 + '|\n' +
             '+' + '-'*box_width + '+\n' +
             '|' + 'Coordinate: ' + str(self.cargo[0]) + ' '*pad2 + '|\n' +
             '+' + '-'*box_width + '+\n'
             '|' + 'Neighbours Explored: ' + '|\n' +
             '|' + neighbours_explored + ' '*pad3 + '|\n' +
             '+' + '-'*box_width + '+\n')
        return s

class Stack:
    """
    LinkedList with stack behaviour
    """
    
    def __init__(self):
        """
        Create and initialize an empty stack
        
        Note: YOU DO NOT NEED TO EDIT THIS METHOD
        """
        self.size = 0
        self.top = None
        
        
    def __str__(self):
        """
        (Stack) -> str
        
        Return a string representation of the stack
        
        You may use this to print a visualization of the stack and its nodes
        
        >>> s = Stack()
        >>> s.push(((2,1),{"U":False,"D":False,"R":False,"L":False}))
        >>> s.push(((2,2),{"U":False,"D":False,"R":False,"L":False}))
        >>> print(s)
        Stack:
        size : 2
        Nodes: 
                  Top
                   |
                   V
        +---------------------+
        |Coordinate Node      |
        +---------------------+
        |Coordinate: (2, 2)   |
        +---------------------+
        |Neighbours Explored: |
        |                     |
        +---------------------+
                   |
                   V
        +---------------------+
        |Coordinate Node      |
        +---------------------+
        |Coordinate: (2, 1)   |
        +---------------------+
        |Neighbours Explored: |
        |                     |
        +---------------------+
        
        
        Note: YOU DO NOT NEED TO EDIT THIS METHOD
        """
        node = self.top
        
        if not self.is_empty():
            nodes_str = " "*9 + "Top\n" + 10*" " + "|\n" + 10*" " + "V\n"
            while node != None:
                nodes_str += str(node)
                if node.next != None:
                    # add an arrow
                    arrow = 10*" " + "|\n" + 10*" " + "V\n"
                    nodes_str += arrow
                node = node.next
        else:
            nodes_str = ""
        
        return "Stack:\nsize : " + str(self.size) + "\nNodes: \n" + nodes_str
        
    def push(self,cargo):
        """
        (Stack, tuple) -> None
        
        Creates a new Node containing cargo and adds it to the top of the
        stack.
        
        >>> s = stack()
        >>> print(s)
        Stack:
        size : 0
        Nodes:
        >>> s.push(((2,1),{"U":False,"D":False,"R":False,"L":False}))
        >>> print(s)
        Stack:
        size : 1
        Nodes: 
                  Top
                   |
                   V
        +---------------------+
        |Coordinate Node      |
        +---------------------+
        |Coordinate: (2, 1)   |
        +---------------------+
        |Neighbours Explored: |
        |                     |
        +---------------------+
        
        """
        
        # TODO: YOUR CODE HERE
        self.size += 1
        node = Node(cargo)
        if self.is_empty():
            self.top = node
        else:
            node.next = self.top
            self.top = node
    
    def pop(self):
        """
        (Stack) -> tuple
        
        Remove the top Node of the stack and return its cargo. 
        If the stack is empty, return None.
        
        >>> s = Stack()
        >>> s.push(((2,1),{"U":False,"D":False,"R":False,"L":False}))
        >>> d = s.pop()
        >>> print(d)
        ((2,1),{"U":False,"D":False,"R":False,"L":False})
        >>> print(s)
        Stack:
        size : 0
        Nodes:
        """
        # TODO: YOUR CODE HERE
        
        if self.size != 0:
            self.size -= 1
            node = self.top
            coords, direction = node.cargo
            self.top = node.next
            return coords, direction
        else:
            return None
    
    def peek(self):
        """
        (Stack) -> tuple 
        
        Return the cargo of the top node of the stack.
        If the stack is empty, return None.
        
        >>> s = Stack()
        >>> s.push(((2,1),{"U":False,"D":False,"R":False,"L":False}))
        >>> d = s.peek()
        >>> print(d)
        ((2,1),{"U":False,"D":False,"R":False,"L":False})
        >>> print(s)
        Stack:
        size : 1
        Nodes: 
                  Top
                   |
                   V
        +---------------------+
        |Coordinate Node      |
        +---------------------+
        |Coordinate: (2, 1)   |
        +---------------------+
        |Neighbours Explored: |
        |                     |
        +---------------------+
        """
        
        # TODO: YOUR CODE HERE
        top = self.top
        return top.cargo
    
    def search(self,coordinate):
        """
        (Stack, coordinate-tuple) -> bool
        
        Search the Nodes in the stack to see if a node with the input
        coordinate is already in the stack
        
        Returns True if a node with the same coordinates is found, false 
        otherwise
        
        >>> s = Stack()
        >>> s.push(((2,1),{"U":False,"D":False,"R":False,"L":False}))
        >>> s.push(((2,2),{"U":False,"D":False,"R":False,"L":False}))
        >>> print(s.search((2,1)))
        True
        >>> print(s.search((4,2)))
        False
        """
        
        # TODO: YOUR CODE HERE
        n = self.top
        while n != None:
            coords, direction = n.cargo
            if coords == coordinate:
                return True
            n = n.next
        return False
    
    def is_empty(self):
        """
        (Stack) -> bool
        
        Check if the stack is empty. Return True if the stack is empty
        (i.e. contains zero nodes). Return False otherwise.
        
        Note: YOU DO NOT NEED TO EDIT THIS METHOD
        """
        
        if self.size == 0:
            return True
        else:
            return False


##############################################
# Helper functions
#
# These are provided to help you complete
# the lab. 
#
# YOU DO NOT NEED TO EDIT THESE FUNCTIONS    
##############################################

def print_maze(maze):
    """
    (tuple) -> None
    
    Input is a nested tuple representing a
    maze. Function prints the maze.
    
    Note: YOU DO NOT NEED TO EDIT THIS FUNCTION
    """
    
    for row in maze:
        print("".join(row))


import csv

def load_maze(filename):
    """
    (str) -> Maze-Tuple, Start-Coordinate, End-Coordinate
    
    Open a csv file containing a maze represented by ascii characters
    and return a nested tuple with each element representing a different
    square within the maze.
    
    Additionally, return the location of the start and end positions of the 
    maze as tuples representing x,y coordinates.
    
    For example, for the following maze:
        
        XXXXXXXXXXXXXXXXXX
        XOXOOOOOOOOOOOXOOE
        XOOOXOOXXXXXXOOOXX
        XXXOXXXXXXXXXXXXXX
        XOOOOOXXOOXXXXXXXX
        XXXXXOOOOXOOOOOXXX
        XXXXXXXOOOOXOXXXXX
        XXXXXXXXXXXXSXXXXX
    
    Will return:
        
    
    You may assume the following:
        1. Each line of the csv file has the same number of columns
        2. Each file will contain one and only one starting location ("S")
        3. Each file will contain one and only one exit location ("E")
        4. Each cell of the csv file will contain a single character
        
        
    Note: YOU DO NOT NEED TO EDIT THIS FUNCTION
    """
    
    # start with a list of coordinates
    maze = []
    start_position = None
    exit_position = None
    
    # open the file for reading
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')
        
        row = 0
        for line in csv_reader:
            # create a tuple of the values within the row
            maze_row = tuple(line)
            
            # add the row to the maze
            maze.append(maze_row)
            
            # check if the row contains the start and/or end positions
            if "S" in maze_row:
                col = maze_row.index("S")
                start_position = (row,col)
            
            if "E" in maze_row:
                col = maze_row.index("E")
                exit_position = (row,col)
           
            row += 1
            
    # convert the maze to a tuple
    maze = tuple(maze)
    
    return maze, start_position, exit_position

def valid_path_coordinate(maze,coord):
    """
    (maze-tuple, coordinate-tuple) -> bool
    
    Checks if the input coordinate is a valid path position
    in the maze. Maze characters have the following meaning:
        X - Wall
        O - Passage
        S - Starting location (i.e. where to enter the maze)
        E - Exit location
        
    Note: YOU DO NOT NEED TO EDIT THIS FUNCTION
    """
    
    # check if the coordinate is out-of-bounds
    if (coord[0] < 0 or coord[0] >= len(maze)) or \
       (coord[1] < 0 or coord[1] >= len(maze[0])):
        return False
     
    # check if the coordinate is a wall
    if maze[coord[0]][coord[1]] == "X":
        return False
    
    # all other squares are valid
    return True
    

##############################################################
# PART 2 - Use the Stack Class to Iteratively Solve the Maze #
##############################################################
            
def solve_maze(maze,start,end):
    """
    (tuple,tuple,tuple) -> bool, Stack

    Iteratively solve the maze stored as a 2D tuple of ASCII characters.
    Characters have the following meanings:
        X - Wall
        O - Passage
        S - Starting location (i.e. where to enter the maze)
        E - Exit location 
    
    You may only move in horizontal or vertical directions. That is, the
    solution path, if it exists, should not contain any diagonal movements.
    
    The solution path, if it exists, should begin at the starting location
    and end at the exit point. The beginning of the path is the bottom node in
    the returned stack, the end position is the top node.
    
    If no path exists, the Stack should be empty.
    
    The first return value should be True if a path through the maze exits.
    If a path does not exist, this return value should be False.
    """
    
    # Code below is to help you get started
    # create the stack
    path = Stack()
    
    # push the starting point to the stack
    start_pos_data = (start, {"L":False,"R":False,"U":False,"D":False})
    path.push(start_pos_data)
    
    maze_solved = False
    
    while not maze_solved:
        
        # TODO: YOUR CODE HERE
                     
        def check_neighbours(row, column):
            neighbours = dict()   
            
            U = (row-1, column)
            D = (row+1, column)
            R = (row, column+1)
            L = (row, column-1)
            neighbours["U"] = path.search(U)
            neighbours["D"] = path.search(D)
            neighbours["R"] = path.search(R)
            neighbours["L"] = path.search(L)
            path.push(((row, column), neighbours))
            return
        
        #a)check current position
        if path.size == 0:
            return maze_solved, path
        
        curr_sqr, directions = path.peek()
        row, column = curr_sqr
        
        #print(row, column)
        if valid_path_coordinate(maze,curr_sqr):
            
            #b)check directions
            if not directions["U"]:
                row -= 1
                directions["U"] = True
                #update current stack with proper directions
                path.pop()
                path.push((curr_sqr, directions))
                #check neighbours for next square and add it to stack
                check_neighbours(row, column)
            elif not directions["R"]:
                column += 1
                directions["R"] = True
                path.pop()
                path.push((curr_sqr, directions))
                check_neighbours(row, column)
            elif not directions["D"]:
                row += 1
                directions["D"] = True
                path.pop()
                path.push((curr_sqr, directions))
                check_neighbours(row, column)
            elif not directions["L"]:
                column -= 1
                directions["L"] = True
                path.pop()
                path.push((curr_sqr, directions))
                check_neighbours(row, column)
            
            else: #when all directions have been checked
                path.pop()
                maze_solved = False
            
            #print((curr_sqr, directions))
            
            if (row,column) == end:
                maze_solved = True
            else:
                maze_solved = False  
        
        #when square is not valid, pop it from stack
        else:
            path.pop()
          
    return maze_solved, path