# Simple example demonstrating how to read values from the Basic, and the 
# usage of the Basic functions

from sys import exit
import time

from basic import Basic

## variables
# serial port name
port = "COM3" # see Basic documentation for port name on Mac
# start time
startTime = time.time_ns()
# number of points
numPoints = 1000; # 1000 points ~ 5 seconds of data

## script
# try to connect to port 
try:
    basic = Basic(port)
except Exception as e:
    # if can't connect, print error and exit
    print(str(e))
    exit()


# read 1000 points and print
for i in range(1,numPoints):
    data = basic.get_data()
    data_time = (time.time_ns()-startTime)/1000000000 # time from start in seconds   
    print ("[{time:.4f}, {value}]".format(time = data_time, value = data))


## close serial port
basic.close()

