import subprocess
def getDevices():
    RawDevices = subprocess.check_output("wmic logicaldisk where drivetype=2 get deviceid, volumename, description, volumeserialnumber /format:list", shell=True)
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
# display some lines

#if __name__ == "__main__": main()
