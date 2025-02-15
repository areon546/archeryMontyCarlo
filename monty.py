import random as rng
import matplotlib.pyplot as plt
import math


def generateCoordinate(RADIAL : bool, xs, ys) -> int:
    
    if (RADIAL):
        xPos, yPos, radius = generateCoordinateRadially(xs, ys)
    else:
        xPos, yPos = generateCoordinateUniformly(xs, ys)
        radius = (xPos**2 + yPos**2)**(1/2)
    
    xs.append(xPos)
    ys.append(yPos)
    
    # print(radius)
    
    return radius

def generateCoordinateRadially(xs, ys):
    
    # generate a random angle
    theta = rng.uniform(0,2*math.pi)
    
    # generate a random distance across the radius
    radius = rng.uniform(0.0,1.0)
    
    # generate a point based on the angle and radius
    xPos = math.sin(theta) * radius
    yPos = math.cos(theta) * radius
    # print(theta, radius, xPos, yPos)
    
    return xPos, yPos, radius

def generateCoordinateUniformly(xs, ys):
    xPos = rng.uniform(-1.0, 1.0)
    yPos = rng.uniform(-1.0, 1.0)
    
    return xPos, yPos

def generateCoordinates(IS_RADIAL, loops, numberOfShots, metricArr, imperialArr):
    xs = []
    ys = []
    counter = 0
    maxR = 1
    
    while counter<loops:
        counted = False

        # here i make the random numbers
        radius = generateCoordinate(IS_RADIAL, xs, ys)      
        #print(f"x: {xPos}, y: {yPos}, r: {radius}")


        # here i check if between a certain boundary, then add to array
        for i in range(0, 10, 1):
            #print(i)
            tenthI = i/10
            
            if (radius<((tenthI+0.1)*maxR) and (not counted)):
                metricArr[i] += 1
                imperialArr[i//2] += 1
                counted=True
                #print("metric counted")
                numberOfShots+=1
        
        counter+=1
    
    return metricArr, imperialArr, xs, ys, numberOfShots

def createUniformImage():
    
    
    
    return

def makeFigure(ax):
    # Makes the rings and places them on a figure
    circles = []
    
    # outermost ring boundary
    circles.append(plt.Circle((0, 0), (1), 
                            color='black', fill=False)) # 1  outer white ring boundary
    
    # colour boundaries
    circles.append(plt.Circle((0, 0), (0.8), 
                            color='black', fill=True)) # .8  outer black ring boundary
    circles.append(plt.Circle((0, 0), (0.6), 
                            color='blue', fill=True)) # .6  outer blue ring boundary
    circles.append(plt.Circle((0, 0), (0.4), 
                            color='red', fill=True)) # .4  outer red ring boundary
    circles.append(plt.Circle((0, 0), (0.2), 
                            color='gold', fill=True)) # .2  outer gold ring boundary
    
    # outer inner ring boundaryes, only used for metric
    circles.append(plt.Circle((0, 0), (0.9), 
                            color='black', fill=False)) # .9  inner white ring boundary
    circles.append(plt.Circle((0, 0), (0.7), 
                            color='white', fill=False)) # .7
    circles.append(plt.Circle((0, 0), (0.5), 
                            color='black', fill=False)) # .5
    circles.append(plt.Circle((0, 0), (0.3), 
                            color='black', fill=False)) # .3
    circles.append(plt.Circle((0, 0), (0.1), 
                            color='black', fill=False)) # .1


    for i in range(0, 10):
        ax.add_patch(circles[i])
    return

def calculateAndPrintResults(numberOfShots, metricArr, imperialArr, loops):
    metricArrR = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    imperialArrR = [0, 0, 0, 0, 0]
    
    

    for i in range(0, 10):
        metricArrR[i] = metricArr[i]*(10-i)
        #print("metric", i, 10-i)

    for i in range(0, 5):
        imperialArrR[i] = imperialArr[i]*(9-(2*i))
        #print("imperial", i, 9-2*i)
        

    
    print("sum divided by number in circle")
    print("\nMetric")
    print(metricArr, metricArrR, ", sum: ", sum(metricArrR),
        ", avg: ", (sum(metricArrR)/numberOfShots))

    print("\nImperial")
    print(imperialArr, imperialArrR, ", sum: ", sum(imperialArrR), 
        ", avg: ", (sum(imperialArrR)/numberOfShots))

    print("\n")

    print("accounting for not including misses")
    print(metricArr, metricArrR, ", sum: ", sum(metricArrR),
        ", avg: ", (sum(metricArrR)/loops))
    print(imperialArr, imperialArrR, ", sum: ", sum(imperialArrR), 
        ", avg: ", (sum(imperialArrR)/loops))
    
    return

def displayShots(loops):
    # print("Hello, World!")
    loops = 5_00 #0
    IS_RADIAL = True

    # here i have the arrays and other important things
    metricArr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    imperialArr = [0, 0, 0, 0, 0]
    numberOfShots = 0


    # generates points and places them in the arrays
    metricArr, imperialArr, xs, ys, numberOfShots = generateCoordinates(IS_RADIAL, loops, numberOfShots, metricArr, imperialArr)


    # calculates and prints out results
    calculateAndPrintResults(numberOfShots, metricArr, imperialArr, loops)

    fig, ax = plt.subplots()

    # sets the limits of the axes
    ax.set_xlim((-1, 1))
    ax.set_ylim((-1, 1))
    
    makeFigure(ax)

    fig.savefig('plotcircles.png')
    

    plt.plot(xs, ys, ".")
    plt.plot(0, 0, color="#000000")
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.autoscale(enable=True, axis='both', tight=None)


    ax.set_aspect('equal', adjustable='box')

    plt.show()
    return


if __name__ == "__main__":
    displayShots(500)
