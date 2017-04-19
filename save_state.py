"""
Written by Miles Wilhelms-Tricarico
Creates savefile.json and initializes it, saves to it, and loads from it."""
import json
import os
import datetime
# from pprint import pprint #for pretty printing json

def is_non_zero_file(fpath):
    """Checks if file exists and if its size is greater than 0
    Returns: true/false"""
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0

def init_savefile_if_missing():
    """Creates savefile if it is missing
    Returns: [nothing]"""
    if not is_non_zero_file("savefile.json"): #init savefile if does not exist
        savefile = open("savefile.json", "w")
        initdata = {}
        initdata["savedTests"] = []
        for i in range(4):
            initdata["savedTests"].append({
                "name": "Test " + str(i+1),
                "sliderMin": 0, #int
                "sliderMax": 16, #int
                "readCheckBox": "True", #bool
                "writeCheckBox": "True" #bool
            })
        json.dump(initdata, savefile, ensure_ascii=False, indent=4)
        savefile.close()


def save_state(radio_index, name, slider_min, slider_max, read_checkbox, write_checkbox):
    """Saves the state of the specified radio button
    Returns: [nothing]
    """
    #init_savefile_if_missing()

    savefile = open('savefile.json', 'r') # open savefile for reading
    data = json.load(savefile)
    savefile.close()

    savefile = open('savefile.json', 'w') # open savefile for writing
    data["savedTests"][radio_index]["name"] = str(name)
    data["savedTests"][radio_index]["sliderMin"] = int(slider_min)
    data["savedTests"][radio_index]["sliderMax"] = int(slider_max)
    data["savedTests"][radio_index]["readCheckBox"] = str(read_checkbox)
    data["savedTests"][radio_index]["writeCheckBox"] = str(write_checkbox)
    json.dump(data, savefile, ensure_ascii=False, indent=4)
    savefile.close()

def save_test(devName, size, testName, serialNum, mount, desc, freeSpace, form, timeStamp, blockSize, readTimes, writeTimes):
    #init_savefile_if_missing()

    if not is_non_zero_file('saved_tests.json'):
        savefile = open('saved_tests.json', 'w')
        data={}
        data['Results'] = []
        json.dump(data, savefile, ensure_ascii=False, indent=4)
        savefile.close()

    savefile = open('saved_tests.json', 'r')  # open savefile for reading
    data = json.load(savefile)
    savefile.close()

    savefile = open('saved_tests.json', 'w')  # open savefile for writing
    data["Results"].append({
        "timeStamp": timeStamp,
        "testName": testName,
        "deviceName": devName,
        "size": size,
        "serialNum": serialNum,
        "mount": mount,
        "description": desc,
        "freeSpace": freeSpace,
        "format": form,
        "blockSize": blockSize,
        "readTimes": readTimes,
        "writeTimes": writeTimes
    })
    json.dump(data, savefile, ensure_ascii=False, indent=4)
    savefile.close()

def load_radio_button(radio_index):
    """Loads the save data for a particular radio button
    Returns: name, slider_min, slider_max, read_checkbox, write_checkbox"""
    init_savefile_if_missing()

    savefile = open('savefile.json', 'r') # open savefile
    data = json.load(savefile)
    savefile.close()
    name = data["savedTests"][radio_index]["name"]
    slider_min = int(data["savedTests"][radio_index]["sliderMin"])
    slider_max = int(data["savedTests"][radio_index]["sliderMax"])
    read_checkbox = data["savedTests"][radio_index]["readCheckBox"]
    write_checkbox = data["savedTests"][radio_index]["writeCheckBox"]
    return name, slider_min, slider_max, read_checkbox, write_checkbox


def load_all_names():
    """Loads all names of saves
    Returns: name1, name2, name3, name4"""
    init_savefile_if_missing()

    savefile = open('savefile.json', 'r') # open savefile
    data = json.load(savefile)
    savefile.close()
    name1 = data["savedTests"][0]["name"]
    name2 = data["savedTests"][1]["name"]
    name3 = data["savedTests"][2]["name"]
    name4 = data["savedTests"][3]["name"]
    return name1, name2, name3, name4

# if __name__ == "__main__": save_state(2, "yolo", "2", "14", "true", "true")
# if __name__ == "__main__": print(load_radio_button(2))
# if __name__ == "__main__": print(load_all_names())
