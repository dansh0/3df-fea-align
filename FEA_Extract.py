from math import *

#Extract Data

report = open('test.rpt','r') #Open file

lines = [] #Array of all lines of file
data = [] #
flag = 0
while flag == 0: #Read each line of file and return array of lines
    lines.append(report.readline())
    if lines[-1] == '':
        flag = 1 #end of file

report.close()

#Process Data

for i in range(len(lines)): #Break each line into array of values
    lineData = [] #each data item of current line
    startIndex = [] #list of the start position of each value in current line
    endIndex = [] #list of the end position of each value in current line
    prevLetterFlag = 0
    for j in range(len(lines[i])-2): #Index data values
        if lines[i][j] != ' ':
            letterFlag = 1
        else:
            letterFlag = 0
        if prevLetterFlag != letterFlag:
            if letterFlag == 1:
                startIndex.append(j)
            if letterFlag == 0:
                endIndex.append(j)
        prevLetterFlag = letterFlag
    endIndex.append(len(lines[i])-1)
    for j in range(len(startIndex)):
        lineData.append(lines[i][startIndex[j]:endIndex[j]])
    data.append(lineData) #put current line data into full data

nodes = 490 #last line of section 1 (xyz coordinates)

xCoord = []
yCoord = []
e11 = [] #x strain
e22 = [] #y strain
e12 = [] #shear strain
pAngle = [] #Principal Angle
eMax = [] #Princial Strain Max

for i in range(nodes): #get x/y coordinates, strain values, solve principal angle at each node
    xPos = float(data[i+16][2]) #X Position
    yPos = float(data[i+16][3]) #Y Position
    xCoord.append(xPos)
    yCoord.append(yPos)

    # Assign global max/min for x and y
    if i == 0: #Initialize
        xMax = xPos
        xMin = xPos
    elif xPos > xMax: #Replace with new max
        xMax = xPos
    elif xPos < xMin: #Replace with new min
        xMin = xPos
    if i == 0:
        yMax = yPos
        yMin = yPos
    elif yPos > yMax:
        yMax = yPos
    elif yPos < yMin:
        yMin = yPos
        
    e11.append(float(data[i+nodes+21][3])) #X Strain
    e22.append(float(data[i+nodes+21][4])) #Y Strain
    e12.append(float(data[i+nodes+21][6])) #Shear Strain
    pA = atan(e12[-1]/(e11[-1]-e22[-1]))/2 #Principal Angle
    pE = (e11[-1]+e22[-1])/2 + sqrt(pow(((e11[-1]-e22[-1])/2),2)+pow((e12[-1]/2),2)) #Principal Strain
    pAngle.append(pA)
    eMax.append(pE)

#Map principal angle to a grid
#for i in range(int(ceil((xMax-xMin)))):
 #   for j in range(int(ceil((yMax-yMin)))):
        #find closest value in each quandrant
        #average values
