#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]  # Get all arguments except the script name
    count = len(argv)

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    for i, arg in enumerate(argv, 1):
        print("{}: {}".format(i, arg))
