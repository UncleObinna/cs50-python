def main():
    # get input from user
    answer = input("What is the time now? ")
# convert input to usable time
    time = convert(answer)
# process time to get meal time
    if time >= 7 and time <= 8:
        print("Breakfast time")
    elif time >= 12 and time <= 13:
        print("Lunch time")
    elif time >= 18 and time <= 19:
        print("Dinner time")


# function to convert time
def convert(time):
# convert time to float value
    hours, mins = time.split(":")
    mins = float(mins) / 60
# return new time format
    time = float(hours) + round(mins, 2)
    return time


if __name__ == "__main__":
    main()
