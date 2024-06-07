import re
import sys


def main():
    print(convert(input("Hours: ")))


#9 AM to 5 P | 9:00 AM to 5:00 PM
#12 AM to 12 PM >> 00:00 to 12:00
def convert(s):
    if matches_short := re.search(r"^(\d+) (AM|PM) to (\d+) (PM|AM)", s):
        hours_from, p_from, hours_to, p_to = matches_short.groups()

        return format24(hours_from, hours_to, p_from, p_to)

    elif matches_full := re.search(r"^(\d+):(\d+) (AM|PM) to (\d+):(\d+) (PM|AM)", s):
        hours_from, minutes_from, p_from, hours_to, minutes_to, p_to = matches_full.groups()

        return format24(hours_from, hours_to, p_from, p_to, minutes_from, minutes_to)
    else:
        raise ValueError
        #sys.exit("Unmatched")

def format24(hoursF, hoursT, partF, partT, minF="00", minT="00"):
    #hours format
    if int(hoursF) and int(hoursT) not in list(range(13)):
        raise ValueError
    elif int(minF) and int(minT) not in list(range(60)):
        raise ValueError

    #create a dictionary
    set_dict = {
            "daytime" : partF,
            "hours" : hoursF,
            "minutes" : minF}, {
            "daytime": partT,
            "hours": hoursT,
            "minutes": minT
            }
    #print(set_dict)

    for set in set_dict:
    #convert 12 to 24
        if set["daytime"] == "PM" and set["hours"] != "12":
                set["hours"] = int(set["hours"]) + 12

    #exception
        if set["daytime"] == "AM" and set["hours"] == "12":
            set["hours"] = "0"

    #print(set_dict)

    hours_from = str(set_dict[0]["hours"])
    hours_to = str(set_dict[1]["hours"])

    return f"{hours_from.zfill(2)}:{minF} to {hours_to.zfill(2)}:{minT}"


if __name__ == "__main__":
    main()

