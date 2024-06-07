
def main():
    t = convert(input("What time is it? "))

    if 7.0 <= t <= 8.0:
        print("breakfast time")
    elif 12.0 <= t <= 13.0:
        print("lunch time")
    elif 18.0 <= t <= 19.0:
        print("dinner time")



def convert(time):
    hour, minute = time.split(":")
    return float(hour) + float(minute) / 60

if __name__== "__main__":
    main()
