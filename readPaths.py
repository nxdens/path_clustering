import numpy as np
pathFile = open("pathFile1.txt","r")
paths = len(open("pathFile1.txt","r").readlines())
longestPathLength = len(max(open("pathFile1.txt","r"),key=len).split(" "))
print(paths)
print(longestPathLength)
usingIntensity = 1
dilationRadius = 1 #has to be greater that 1
pathParams = 3+(usingIntensity*(3*dilationRadius-2)**2)
print(pathParams)
paths = np.zeros(paths,longestPathLength,pathParams) # start with just the xyz and intensity of the paths nothing around it yet