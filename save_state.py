"""
Written by Miles Wilhelms-Tricarico
Creates savefile.json and initializes it, saves to it, and loads from it."""
import json
import os
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
                "name": "",
                "sliderLabelMin": 0, #int
                "sliderLabelMax": 0, #int
                "readCheckBox": "false", #bool
                "writeCheckBox": "false" #bool
            })
        json.dump(initdata, savefile, ensure_ascii=False, indent=4)
        savefile.close()


def save_state(radio_index, name, slider_label_min, slider_label_max, read_check_box, write_check_box):
    """Saves the state of the specified radio button
    Returns: [nothing]
    """
    init_savefile_if_missing()

    savefile = open('savefile.json', 'r') # open savefile for reading
    data = json.load(savefile)
    savefile.close()

    savefile = open('savefile.json', 'w') # open savefile for writing
    data["savedTests"][radio_index - 1]["name"] = str(name)
    data["savedTests"][radio_index - 1]["sliderLabelMin"] = int(slider_label_min)
    data["savedTests"][radio_index - 1]["sliderLabelMax"] = int(slider_label_max)
    data["savedTests"][radio_index - 1]["readCheckBox"] = str(read_check_box)
    data["savedTests"][radio_index - 1]["writeCheckBox"] = str(write_check_box)
    json.dump(data, savefile, ensure_ascii=False, indent=4)
    savefile.close()


def load_radio_button(radio_index):
    """Loads the save data for a particular radio button
    Returns: name, slider_label_min, slider_label_max, read_check_box, write_check_box"""
    init_savefile_if_missing()

    savefile = open('savefile.json', 'r') # open savefile
    data = json.load(savefile)
    savefile.close()
    name = data["savedTests"][radio_index]["name"]
    slider_label_min = int(data["savedTests"][radio_index]["sliderLabelMin"])
    slider_label_max = int(data["savedTests"][radio_index]["sliderLabelMax"])
    read_check_box = data["savedTests"][radio_index]["readCheckBox"]
    write_check_box = data["savedTests"][radio_index]["writeCheckBox"]
    return name, slider_label_min, slider_label_max, read_check_box, write_check_box


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
