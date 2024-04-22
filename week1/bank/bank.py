# get input from user
greeting = input("Enter greeting here: ").lower().strip()

# process greeting
if "hello" in greeting:
    print("$0")
elif greeting[0].lower() == "h":
    print("$20")
else:
    print("$100")
