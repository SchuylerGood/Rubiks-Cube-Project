"""
Program:        Rubiks Cube Solver
Contributors:   Sky, Akshay, Dylan, Eric
Date:           9/12/2022
Course:         CISC 204 - Final Logic Project
"""

class Cube:
    def __init__(self, sides):
        self.sides = sides

CORESPONDING_SIDES_INT = {0:"Top",1:"Bottom",2:"Front",3:"Back",4:"Left",5:"Right"}
CORESPONDING_SIDES_STRING = {"Top":0,"Bottom":1,"Front":2,"Back":3,"Left":4,"Right":5}

def findWhiteCenter(cube):
    """
    Function:   Finds where the white center is on the cube
    Parameters: cube (of type Cube)
    Returns:    String - what side of the cube the white center is on
    """
    for i in range(len(cube.sides)):
        if cube.sides[i][1][1] == "w":
            return CORESPONDING_SIDES_INT[i]


def findWhiteMiddles(cube):
    """
    Function:   Finds the locations of all the white-middle squares
    Parameters: cube (of type Cube)
    Returns:    2D list of the 4 locations of the white-middle squares 
    """
    locations = []
    for i in range(len(cube.sides)):
        if(cube.sides[i][0][1] == "w"):
            locations.append([i,0,1])
        if(cube.sides[i][1][0] == "w"):
            locations.append([i,1,0])
        if(cube.sides[i][1][2] == "w"):
            locations.append([i,1,2])
        if(cube.sides[i][2][1] == "w"):
            locations.append([i,2,1])

    return locations


def isSideSolved(cube, side):
    """
    Function:   Determins if a side is solved
    Parameters: cube - type cube
                side - type String (corresponds to CORRESPONDING_SIDES global variable)
    Returns:    Boolean value 
    """
    sideInt = CORESPONDING_SIDES_STRING[side]
    for i in range(2):
        for j in range(len(cube.sides[sideInt][i])):
            sideColor = cube.sides[sideInt][1][1]
            if cube.sides[sideInt][i][j] != sideColor:
                return False
    return True


def isCubeSolved(cube):
    """
    Function:   Determines if the cube is solved
    Parameters: cube of type Cube
    Returns:    Boolean value
    """
    sideChecks = []
    for i in range(len(cube.sides)):
        sideChecks.append(isSideSolved(cube, CORESPONDING_SIDES_INT[i]))
    for i in sideChecks:
        if(i != True):
            return False
        else:
            return True


def main():
    cube1 = Cube(
        sides = [[["b","b","b"],["b","b","b"],["b","b","b"]], #Top
                 [["g","g","g"],["g","g","g"],["g","g","g"]], # Bottom
                 [["y","y","y"],["y","y","y"],["y","y","y"]], # Front
                 [["w","w","w"],["w","w","w"],["w","w","w"]], # Back
                 [["r","r","r"],["r","r","r"],["r","r","r"]], # Left
                 [["o","o","o"],["o","o","o"],["o","o","o"]]] # Right
    )
    print('White Center:', findWhiteCenter(cube1))
    print(isSideSolved(cube1, "Front"))
    print(findWhiteMiddles(cube1))
    print(isCubeSolved(cube1))

    
main()
    
    
