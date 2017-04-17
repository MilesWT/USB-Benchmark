import os
import time

def writeBlock(letterDrive,blockSize):
    data = bytearray(1024*blockSize)
    for byte in data:
        byte = 0x88
    with open('%s:\output_file'%letterDrive, 'bw+') as fout:
        fout.seek(0)
        start = time.clock()
        fout.write(data)
        end = time.clock()
        fout.truncate()
    timeTaken = end-start
    return(timeTaken)

def readBlock(fileLocation,blockSize):
    with open(fileLocation, 'r') as fin:
        start = time.clock()
        fin.read(1024*blockSize)
        end = time.clock()
    timeTaken = end-start
    return(timeTaken)

if __name__ == "__main__":
    print(writeBlock("D",1024))
    print(readBlock("D:\output_file",1000))
