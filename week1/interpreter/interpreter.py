# get input from user
x, y, z = input("enter values here: ").split()

# convert input to floats
x = float(x)
z = float(z)

# process input and print out result
if y == "+":
    print(f"{x + z:.1f}")
elif y == "-":
    print(f"{x - z:.1f}")
elif y == "*":
    print(f"{x * z:.1f}")
elif y == "/":
    print(f"{x / z:.1f}")

#      #
#  OR  #
#      #

match y:
    case "+":
        print(f"{x + y:.1f}")
    case "-":
        print(f"{x - z:.1f}")
    case "*":
        print(f"{x * z:.1f}")
    case "/":
        print(f"{x / z:.1f}")
