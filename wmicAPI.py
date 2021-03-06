import os
import time
import subprocess
import random
import math
import traceback

def getDevices():
    RawDevices = subprocess.check_output(
        "wmic logicaldisk where drivetype=2 get deviceid, volumename, description, volumeserialnumber, Size, Filesystem, freespace /format:list",
        shell=True)

    RawDevices += subprocess.check_output(
        "wmic logicaldisk where drivetype=3 get deviceid, volumename, description, volumeserialnumber, Size, Filesystem, freespace /format:list",
        shell=True)
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

    if 'C:' in myDict['DeviceID']:
        temp = myDict['DeviceID'].index('C:')
        for key in myDict:
            del myDict[key][int(temp)]

    return (myDict)


def writeFile(letterDrive, fileSize, blockSize):  # inputs: str letterDrive to access. Size of write
    numWrites = (fileSize * 1024) / blockSize
    data = bytearray(1024 * blockSize)  # create the array for the data. Must be strictly sized
    for byte in range(len(data)):
        data[byte] = random.randint(0x0, 0xff)  # allocate the data to the same values. hex aa is alternating bits
    with open('%s:\output_file' % letterDrive, 'bw+') as fout:
        fout.seek(0)
        start = time.clock()
        for i in range(int(numWrites)):
            fout.write(data)  # write to file
            os.fsync(fout)
        end = time.clock()
        fout.truncate()
        fout.flush()
        os.fsync(fout)
        fout.close()

    del data
    timeTaken = end - start
    return (timeTaken)  # return time taken


def readFile(fileLocation, blockSize,i):  # inputs: str full fileLocation to access. Size of read
    fileSize = os.stat(fileLocation).st_size
    numReads = fileSize / (blockSize * 1024)
    filename = 'output_file_test' + str(i)
    #mW.addText(numReads)
    print(numReads)
    try:
        start = time.clock()
        with open(fileLocation, "rb",1024 * blockSize) as fin:  # open the file
            with open(filename, "wb+", 1024 * blockSize) as fout:
                for i in range(math.ceil(numReads)):
                    #fout.write(fin.read(1024 * blockSize))  # read in up to the blockSize in kB
                    data = fin.read(1024 * blockSize)
                    fin.flush()
                    #os.fsync(fin)
                    #print(data)
                    fin.flush()
                    fout.write(data)
                    fout.flush()
                    os.fsync(fout.fileno())
        end = time.clock()
        fin.close()
        #print(data)
        timeTaken = end - start
    except Exception as e:
        print(str(e))
        traceback.print_exc()

    try:
        print("written")
        os.remove(filename)
    except:
        print("file not found")
    print(timeTaken)
    return (timeTaken)  # return time taken


def benchmarkDevice(mainWindow, app, letterDrive, smallBlockSize, bigBlockSize, fileSize, write=True, read=True):
    # Write section
    writeflag = True
    writeTimes = []
    readTimes = []
    blockSizes = []
    mW = mainWindow
    for i in range(smallBlockSize, bigBlockSize + 1):
        if write:
            if read:
                tempString = "Writing at " + str(2 ** i) + " kB blockSize " + "(Test " + str(
                    (i - smallBlockSize + 1) * 2 - 1) + " of " + str((bigBlockSize - smallBlockSize + 1) * 2) + ")"
            else:
                tempString = "Writing at " + str(2 ** i) + " kB blockSize " + "(Test " + str(
                    i - smallBlockSize + 1) + " of " + str((bigBlockSize - smallBlockSize + 1)) + ")"
            mainWindow.addText(tempString)
            app.processEvents()
            writeTimes.append(fileSize / (writeFile(letterDrive, fileSize, 2 ** i)))
            writeflag = False
            # os.remove('%s:\output_file' % letterDrive)
        elif writeflag:
            mainWindow.addText("Writing a Temporary File for Reading Tests")
            app.processEvents()
            writeFile(letterDrive, fileSize, 2 ** 8)
            writeflag = False
        if read:
            if write:
                tempString = "Reading at " + str(2 ** i) + " kB blockSize " + "(Test " + str(
                    (i - smallBlockSize + 1) * 2) + " of " + str((bigBlockSize - smallBlockSize + 1) * 2) + ")"
            else:
                tempString = "Reading at " + str(2 ** i) + " kB blockSize " + "(Test " + str(
                    (i - smallBlockSize + 1)) + " of " + str((bigBlockSize - smallBlockSize + 1)) + ")"
            mainWindow.addText(tempString)
            app.processEvents()
            readTimes.append(fileSize / (readFile('%s:\output_file' % letterDrive, 2 ** i, i)))#'%s:Iron Man 2008.720p.BrRip.x264.YIFY.mp4'
        blockSizes.append(2 ** i)
    os.remove('%s:\output_file' % letterDrive)

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
    print(benchmarkDevice("D", 0, 16, 100))
