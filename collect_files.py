import sys
import os

def pushh(input_dir, output_dir):
    files = os.listdir(input_dir)
    for file in files:
        print(file)

if __name__ == "__main__":
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    pushh(input_dir, output_dir)
