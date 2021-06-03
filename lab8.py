##############################################
# APS106 Winter 2020 - Lab 8 - Maze Solver   #
##############################################

##############################################
# Helper functions
#
# These are provided to help you complete
# the lab. 
#
# YOU DO NOT NEED TO EDIT THIS FUNCTION 
##############################################

def print_maze(maze):
    """
    (tuple) -> None
    
    Input is a nested tuple representing a
    maze. Function prints the maze.
    
    """
    
    for row in maze:
        print("".join(row))
    

###########################################
# PART 1 - Read the maze from csv file    #
###########################################

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
    
    >>> load_maze_from_file(maze_file)
    ((('X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'), 
    ('X', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'E'), 
    ('X', 'O', 'O', 'O', 'X', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'X', 'X'), 
    ('X', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'), 
    ('X', 'O', 'O', 'O', 'O', 'O', 'X', 'X', 'O', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'), 
    ('X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'X', 'X', 'X'), 
    ('X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'X', 'O', 'X', 'X', 'X', 'X', 'X'), 
    ('X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'S', 'X', 'X', 'X', 'X', 'X')), 
    (7, 12), (1, 17))
        
    
    You may assume the following:
        1. Each line of the csv file has the same number of columns
        2. Each file will contain one and only one starting location ("S")
        3. Each file will contain one and only one exit location ("E")
        4. Each cell of the csv file will contain a single character
        
    """
    
    ## TODO - YOUR CODE HERE
    #create list of rows
    maze_rows = list()
    with open(filename, 'r') as csvfile:
        maze = csv.reader(csvfile)
        row_counter = 0            
        #for each line in maze
        for line in maze:
            maze_row = tuple()
            #counter set up to find row of "S" and "E"
            if "S" in line:
                S_row = row_counter
            elif "E" in line:
                E_row = row_counter
            row_counter += 1
            #add each element of line to LINE(tuple)
            column_counter = 0
            for element in line:
                maze_row += (element),
                if element == "S":
                    S_column = column_counter
                elif element == "E":
                    E_column = column_counter
                column_counter += 1
            #returning tuple contains the the all of the lines
            maze_rows.append(maze_row)
        S_coords = (S_row, S_column)
        E_coords = (E_row, E_column)
        #convert list of rows to tuples of rows
        maze_rows = tuple(maze_rows)
    return maze_rows, S_coords, E_coords
                
###########################################
# PART 2 - Recursively solve the maze     #
###########################################

def solve_maze(maze,path,end):
    """
    (tuple,list,tuple) -> bool
    
    maze - a 2D tuple containing the characters defining the maze indexed by
            row and column
    path - a list of coordinates defining the current search path
    end  - the coordinate of the maze exit

    Recursively solve the maze stored as a 2D tuple of ASCII characters.
    Characters have the following meanings:
        X - Wall
        O - Passage
        S - Starting location (i.e. where to enter the maze)
        E - Exit location 
    
    You may only move in horizontal or vertical directions. That is, the
    solution path, if it exists, should not contain any diagonal movements.
    
    The solution path, if it exists, should begin at the current location
    and end at the exit point.
    
    If no path exists, the path should be empty and the function should
    return "False"
    """
    
    ## TODO: YOUR CODE HERE
    new_maze = list()
    for line in maze:
        new_line = list()
        new_line = list(line)
        new_maze.append(new_line)
    a, b = path[0]
    path.clear()
    def search_maze(x, y):
        if new_maze[x][y] == "E":
            path.append((x,y))
            return True
        elif new_maze[x][y] == "X":
            return False
        elif new_maze[x][y] == "XX":
            return False
        
        new_maze[x][y] = "XX"
        
        if ((x > 0 and search_maze(x-1, y)) 
            or (y < len(new_maze[x])-1 and search_maze(x, y+1))
            or (x < len(new_maze)-1 and search_maze(x+1, y)) 
            or (y > 0 and search_maze(x, y-1))):
            path.append((x,y))
            return True
        
        return False
    
    solvable = search_maze(a,b)
    path.reverse()
    return solvable