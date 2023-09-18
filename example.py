# Simple example demonstrating how to read values from the Basic, and the 
# usage of the Basic functions

from sys import exit
import time
import argparse
from basic import Basic
# check if rich is installed
try:
    from rich import print
except ImportError as e:
    pass # using regular print

def main():
    #parse command line arguments
    parser = argparse.ArgumentParser(description='Simple example demonstrating how to read values from the Basic,and the usage of the Basic functions')
    parser.add_argument("-portName",help="serial port name, default 'COM3'",default="COM3")
    parser.add_argument("-numPoints",help="number of points, default 1000 (~5 seconds)",default=1000,type=int)
    args = parser.parse_args()

    # set start time
    startTime = time.time_ns()

    # try to connect to port 
    try:
        basic = Basic(args.portName)
    except OSError as e:
        # if can't connect, print error and exit
        print(e)
        exit(1)


    # read the points and print
    for i in range(1,args.numPoints):
        data = basic.get_data()
        data_time = (time.time_ns()-startTime)/1000000000 # time from start in seconds   
        print ("[{time:.4f}, {value}]".format(time = data_time, value = data))


    # close serial port
    basic.close()


if __name__=="__main__":
    main()