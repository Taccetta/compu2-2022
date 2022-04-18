import argparse
import shutil


def main():
    try:
        parser = argparse.ArgumentParser(description='Copytor')
        parser.add_argument('-i', '--file1', help='File name')
        parser.add_argument('-o', '--file2', help='File name')
        args = parser.parse_args()

        if args.file1 == None:
            print("Must specify a File name")
            exit(2)

        if args.file2 == None:
            print("Must specify a File name")
            exit(2)

    except:
        print("Error: Invalid Arguments.")
        exit(2)

    try:
        shutil.copyfile(args.file1, args.file2)
        print("Done!")
    
    except:
        print("Error: invalid name")

if __name__ == "__main__":
    main()