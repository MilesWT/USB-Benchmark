import os
import time
import subprocess
def getDevices():
    RawDevices = subprocess.check_output("wmic logicaldisk where drivetype=2 get deviceid, volumename, description, volumeserialnumber, Size, Filesystem /format:list", shell=True)
    Devices = RawDevices.decode().split("\n")
    X = [elem.strip().split("=") for elem in Devices]
    Final = [x for x in X if x != ['']]
    myDict = {}
    for sub_list in Final:
        key, value = sub_list[0], sub_list[1]
        if key in myDict:
            myDict[key].append(value)
        else:
            myDict[key] = [value]
    return(myDict)

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
# display some lines
#if __name__ == "__main__":
#    print(writeBlock("D",1000))
#if __name__ == "__main__": main()
