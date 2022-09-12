# Rubiks Cube Solver


class Cube:
    def __init__(self, sides):
        self.sides = sides

CORESPONDING_SIDES_INT = {0:"Top",1:"Bottom",2:"Front",3:"Back",4:"Left",5:"Right"}
CORESPONDING_SIDES_STRING = {"Top":0,"Bottom":1,"Front":2,"Back":3,"Left":4,"Right":5}


def findWhiteCenter(cube):
    if(type(cube) == Cube):
        for i in range(len(cube.sides)):
            if cube.sides[i][1][1] == "w":
                print('White Center:', CORESPONDING_SIDES_INT[i]) # displays where the white center is

# Function:     Determins if a side is solved
# Parameters:   cube - type cube
#               side - type String (corresponds to CORRESPONDING_SIDES global variable)
# Returns:      Boolean value 
def isSideSolved(cube, side):
    sideInt = CORESPONDING_SIDES_STRING[side]
    if(type(cube) == Cube):
        for i in range(2):
            for j in range(len(cube.sides[sideInt][i])):
                sideColor = cube.sides[sideInt][1][1]
                if cube.sides[sideInt][i][j] != sideColor:
                    return False
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


    findWhiteCenter(cube1)
    print(isSideSolved(cube1, "Front"))

main()
    
    