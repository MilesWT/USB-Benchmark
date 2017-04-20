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

def writeFile(letterDrive,fileSize,blockSize): #inputs: str letterDrive to access. Size of write
    numWrites = (fileSize*1024)/blockSize
    data = bytearray(1024*blockSize) #create the array for the data. Must be strictly sized
    for byte in data:
        byte = 0xaa #allocate the data to the same values. hex aa is alternating bits
    with open('%s:\output_file'%letterDrive, 'bw+') as fout:
        fout.seek(0)
        start = time.clock()
        for i in range(int(numWrites)):
            fout.write(data) #write to file
        end = time.clock()
        fout.truncate()
    timeTaken = end-start
    return(timeTaken) #return time taken


def readFile(fileLocation,blockSize): #inputs: str full fileLocation to access. Size of read
    fileSize = os.stat(fileLocation).st_size
    numReads = fileSize/(blockSize*1024)
    with open(fileLocation, 'r') as fin: #open the file
        start = time.clock()
        for i in range(int(numReads)):
            fin.read(1024*blockSize) #read in up to the blockSize in kB
        end = time.clock()
    timeTaken = end-start
    return(timeTaken) #return time taken

def benchmarkDevice(mainWindow,app,letterDrive,smallBlockSize,bigBlockSize,fileSize,write=True,read=True):
    #Write section
    writeflag = True
    writeTimes = []
    readTimes = []
    blockSizes =[]
    for i in range(smallBlockSize,bigBlockSize+1):
        if write:
            if read:
                tempString = "Writing at "+ str(2**i)+" kB blockSize " +"(Test "+ str((i-smallBlockSize+1)*2-1) + " of " + str((bigBlockSize-smallBlockSize+1)*2) + ")"
            else:
                tempString = "Writing at "+ str(2**i)+" kB blockSize " +"(Test "+ str(i-smallBlockSize+1) + " of " + str((bigBlockSize-smallBlockSize+1)) + ")"
            mainWindow.addText(tempString)
            app.processEvents()
            writeTimes.append(fileSize/(writeFile(letterDrive,fileSize,2**i)))
            writeflag = False
        elif writeflag:
            writeFile(letterDrive, fileSize, 2 ** 8)
            writeflag = False
        if read:
            if write:
                tempString = "Reading at "+ str(2**i)+" kB blockSize " + "(Test "+ str((i-smallBlockSize+1)*2) + " of " + str((bigBlockSize-smallBlockSize+1)*2) + ")"
            else:
                tempString = "Reading at "+ str(2**i)+" kB blockSize " + "(Test "+ str((i-smallBlockSize+1)) + " of " + str((bigBlockSize-smallBlockSize+1)) + ")"
            mainWindow.addText(tempString)
            app.processEvents()
            readTimes.append(fileSize/(readFile('%s:\output_file'%letterDrive,2**i)))
        blockSizes.append(2**i)
    os.remove('%s:\output_file'%letterDrive)
    # if(read and write):
    #     return(blockSizes,writeTimes,readTimes)
    # elif(read):
    #     return(blockSizes,readTimes)
    # elif(write):
    #     return(blockSizes,writeTimes)
    # else:
    #     return(blockSizes)
    return (blockSizes, writeTimes, readTimes)

if __name__ == "__main__":
    print(benchmarkDevice("D",0,16,100))
