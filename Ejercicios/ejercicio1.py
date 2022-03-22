import getopt
import sys

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "n:m:o:")
    except getopt.GetoptError as err:
        print(err)  
        getopt.usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ["-n"]:
            num1 = float(arg)
        elif opt in ["-m"]:
            num2 = float(arg)
        elif opt in ["-o"]:
            if arg == "+":
                num3 = num1 + num2
                print("\nEl resultado es: ", num3)
                print("\n")
            elif arg == "-":
                num3 = num1 - num2
                print("\nEl resultado es: ", num3)
                print("\n")
            elif arg == "/":
                num3 = num1 / num2
                print("\nEl resultado es: ", num3)
                print("\n")
            elif arg == "m":
                num3 = num1 * num2
                print("\nEl resultado es: ", num3)
                print("\n")
        else:
            assert False, "unhandled option"

if __name__ == "__main__":
    main()