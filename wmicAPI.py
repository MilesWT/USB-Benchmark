import os
import time
import subprocess
def getDevices():

    RawDevices = subprocess.check_output("wmic logicaldisk where drivetype=2 get deviceid, volumename, description, volumeserialnumber, Size, Filesystem, freespace /format:list", shell=True)

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

def writeBlock(letterDrive,blockSize): #inputs: str letterDrive to access. Size of write
    data = bytearray(1024*blockSize) #create the array for the data. Must be strictly sized
    for byte in data:
        byte = 0xaa #allocate the data to the same values. hex aa is alternating bits
    with open('%s:\output_file'%letterDrive, 'bw+') as fout:
        fout.seek(0)
        start = time.clock()
        fout.write(data) #write to file
        end = time.clock()
        fout.truncate()
    timeTaken = end-start
    return(timeTaken) #return time taken

def readBlock(fileLocation,blockSize): #inputs: str full fileLocation to access. Size of read
    with open(fileLocation, 'r') as fin: #open the file
        start = time.clock()
        fin.read(1024*blockSize) #read in up to the blockSize in kB
        end = time.clock()
    timeTaken = end-start
    return(timeTaken) #return time taken

#if __name__ == "__main__":
#    print(writeBlock("D",1000))
#   print(readBlock("D:\output_file",1000))
#if __name__ == "__main__": main()
