# Part 1 A -- Make a Line

lineLength = int(input("Choose the length of a line: "))

def makeLine(lineSize):
    p = ''
    for i in range(lineSize):
        p += "#"
    return p

print(makeLine(lineLength))



# Part 1 B -- Make a Square5
# create a function using your make_line function to code a square
chosenSquare = int(input("Choose the size of the square: "))
def makeSquare(squareSize):
    zeroStart = 0
    squareString = ''
    while zeroStart < squareSize-1:
        zeroStart += 1
        squareString += makeLine(squareSize) + "\n"
    squareString += makeLine(squareSize)
    return squareString

print(makeSquare(chosenSquare))

# Part 1 C -- Make a Rectangle
chosenRectWidth = int(input("Choose rectangle width: "))
chosenRectHeight = int(input("Choose rectangle height: "))
def makeRectangle(rectLength, rectHeight):    
    zeroHeight = 0
    rectString = ''
    while zeroHeight < rectHeight-1:
        zeroHeight += 1
        rectString += makeLine(rectLength) + "\n"
    rectString += makeLine(rectLength)
    return rectString

print(makeRectangle(chosenRectWidth, chosenRectHeight))



# Part 2 A -- Make a Stairs
downStairBottomWidth = int(input("Choose the length of the flight of stairs: "))
def makeDownwardStairs(bottomWidth):
    stairString = ''
    i = 1
    while i < bottomWidth:
        stairString += makeLine(i) + "\n"
        i += 1
    stairString += makeLine(i)
    return stairString

print(makeDownwardStairs(downStairBottomWidth))

# Part 2 B -- Make Space-Line 

def makeEmptyLine(lineSize):
    p = ''
    for i in range(lineSize):
        p += " "
    return p

chosenSpaces = int(input("Choose the number of spaces before and after the characters: "))
chosenChars = int(input("Choose the amount of characters: "))
def makeSpaceLine(numSpaces, numChars):
    spaceLineString = '' 
    spaceLineString += makeEmptyLine(numSpaces)
    spaceLineString += makeLine(numChars)
    spaceLineString += makeEmptyLine(numSpaces)
    return spaceLineString

print(makeSpaceLine(chosenSpaces, chosenChars))


# Part 2 C -- Make Isosceles Triangle

chosenIsoscelesSize = int(input("Choose the size of the isosceles triange: "))

def makeIsosceles(isoscelesSize):
    isoscelesString = '' 
    i = 1
    spaceSize = int((isoscelesSize-1)/2)
    if isoscelesSize % 2 == 0:
        print("Try again and choose an odd number if you want to witness the glory of the triangle. Otherwise please leave.")
    else:
        while i < isoscelesSize:
            isoscelesString += makeSpaceLine(spaceSize, i) + "\n"
            i += 2
            spaceSize -= 1
        isoscelesString += makeLine(i)
    return isoscelesString

print(makeIsosceles(chosenIsoscelesSize))




# Part 3 -- Make a Diamond
chosenDiamondSize = int(input("Choose the width of the diamond: "))

def makeDiamond(diamondSize):
    diamondString = '' 
    i = 1
    diamondSpace = int((diamondSize-1)/2)
    if diamondSize % 2 == 0:
        print("Try again and choose an odd number if you want to witness the glory of the diamond. Otherwise please leave.")
    else:
        while i < diamondSize:
            diamondString += makeSpaceLine(diamondSpace, i) + "\n"
            i += 2
            diamondSpace -= 1
        diamondString += makeLine(i) + "\n"
        i -= 2
        diamondSpace += 1
        while i > 0:
            diamondString += makeSpaceLine(diamondSpace, i) + "\n"
            i -= 2
            diamondSpace += 1

    return diamondString

print(makeDiamond(chosenDiamondSize))





