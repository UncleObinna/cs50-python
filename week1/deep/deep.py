# Get input from user
question = input(
    "What is the answer to the Great Question of Life, the Universe and Everything? ")

# match question:
#     case 42 | "42" | "forty two" | "forty-two":
#         print("Yes")
#     case _:
#         print("No")

if question == 42 or question == "42" or question.lower() == "forty two" or question.lower() == "forty-two":
    print("Yes")
else:
    print("No")
