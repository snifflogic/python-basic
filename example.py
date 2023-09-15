# Simple example demonstrating how to read values from the Basic, and the 
# usage of the Basic functions

from sys import exit
import time
import argparse
from basic import Basic
from rich import print
def main():
    parser = argparse.ArgumentParser(description='Simple example demonstrating how to read values from the Basic,and the usage of the Basic functions')
    parser.add_argument("portName",help="serial port name",default="COM3")
    parser.add_argument("-numPoints",help="number of points",default=10000,type=int)
    args = parser.parse_args()
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


    ## close serial port
    basic.close()


if __name__=="__main__":
    main()