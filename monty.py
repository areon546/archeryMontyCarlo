import random as rng
import matplotlib.pyplot as plt
import math


def generateCoordinates(RADIAL : bool, xs, ys) -> int:
    
    if (RADIAL):
        xPos, yPos, radius = generateCoordinatesRadially(xs, ys)
    else:
        xPos, yPos = generateCoordinatesUniformly(xs, ys)
        radius = (xPos**2 + yPos**2)**(1/2)
    
    xCoords.append(xPos)
    yCoords.append(yPos)
    
    # print(xPos, yPos, radius)
    
    return radius

def generateCoordinatesRadially(xs, ys):
    
    # generate a random angle
    theta = rng.uniform(0,2*math.pi)
    
    # generate a random distance across the radius
    radius = rng.uniform(0.0,1.0)
    
    # generate a point based on the angle and radius
    xPos = math.sin(theta)
    yPos = math.cos(theta)
    # print(theta, radius, xPos, yPos)
    
    return xPos, yPos, radius

def generateCoordinatesUniformly(xs, ys):
    xPos = rng.uniform(-1.0, 1.0)
    yPos = rng.uniform(-1.0, 1.0)
    
    return xPos, yPos



if __name__ == "__main__":
    print("Hello, World!")

    # here i have the arrays and other important things
    xCoords = []
    yCoords = []
    metricArr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    imperialArr = [0, 0, 0, 0, 0]
    metricArrR = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    imperialArrR = [0, 0, 0, 0, 0]
    loops = 2_000
    inC = 0
    counter = 0
    maxR = 1
    IS_RADIAL = True


    while counter<loops:
        counted = False

        # here i make the random numbers
        radius = generateCoordinates(IS_RADIAL, xCoords, yCoords)      
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
                inC+=1
        
        counter+=1



    for i in range(0, 10):
        metricArrR[i] = metricArr[i]*(10-i)
        #print("metric", i, 10-i)

    for i in range(0, 5):
        imperialArrR[i] = imperialArr[i]*(9-(2*i))
        #print("imperial", i, 9-2*i)
        

    print("sum divided by number in circle")
    print("\nMetric")
    print(metricArr, metricArrR, ", sum: ", sum(metricArrR),
        ", avg: ", (sum(metricArrR)/inC))

    print("\nImperial")
    print(imperialArr, imperialArrR, ", sum: ", sum(imperialArrR), 
        ", avg: ", (sum(imperialArrR)/inC))

    print("\n")

    print("accounting for not including misses")
    print(metricArr, metricArrR, ", sum: ", sum(metricArrR),
        ", avg: ", (sum(metricArrR)/loops))
    print(imperialArr, imperialArrR, ", sum: ", sum(imperialArrR), 
        ", avg: ", (sum(imperialArrR)/loops))

    fig, ax = plt.subplots()

    # sets the limits of the axes
    ax.set_xlim((-1, 1))
    ax.set_ylim((-1, 1))

    #Makes the circles
    circles = []

    circles.append(plt.Circle((0, 0), (1), 
                            color='black', fill=False)) # 1
    circles.append(plt.Circle((0, 0), (0.9), 
                            color='black', fill=False)) # .9
    circles.append(plt.Circle((0, 0), (0.8), 
                            color='black', fill=True)) # .8
    circles.append(plt.Circle((0, 0), (0.7), 
                            color='white', fill=False)) # .7
    circles.append(plt.Circle((0, 0), (0.6), 
                            color='blue', fill=True)) # .6
    circles.append(plt.Circle((0, 0), (0.5), 
                            color='black', fill=False)) # .5
    circles.append(plt.Circle((0, 0), (0.4), 
                            color='red', fill=True)) # .4
    circles.append(plt.Circle((0, 0), (0.3), 
                            color='black', fill=False)) # .3
    circles.append(plt.Circle((0, 0), (0.2), 
                            color='gold', fill=True)) # .2
    circles.append(plt.Circle((0, 0), (0.1), 
                            color='black', fill=False)) # .1
        

    for i in range(0, 10):
        ax.add_patch(circles[i])

    fig.savefig('plotcircles.png')


    plt.plot(xCoords, yCoords, ".")
    plt.plot(0, 0, color="#000000")
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.autoscale(enable=True, axis='both', tight=None)


    ax.set_aspect('equal', adjustable='box')

    plt.show()