def main():
    text = str(input("Enter text with emoticon here: "))
    print(convert(text))


def convert(emoticon):
    emoticon = emoticon.replace(":)", "😊")
    emoticon = emoticon.replace(":(", "😞")
    emoticon = emoticon.replace(":D", "😁")
    emoticon = emoticon.replace(":'(", "😓")

    return emoticon


main()
