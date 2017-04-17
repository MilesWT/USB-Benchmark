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

if __name__ == "__main__":
    print(writeBlock("D",1000))
