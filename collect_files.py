import os
import shutil
import sys

def collect_files(input_dir, output_dir):
    file_count = {}

    def process_directory(directory):
        for entry in os.scandir(directory):
            if entry.is_file():
                base_name = entry.name
                if base_name in file_count:
                    file_count[base_name] += 1
                    name, ext = os.path.splitext(base_name)
                    base_name = f"{name}_{file_count[base_name]}{ext}"
                else:
                    file_count[base_name] = 1
                shutil.copy(entry.path, os.path.join(output_dir, base_name))
            elif entry.is_dir():
                process_directory(entry.path)

    process_directory(input_dir)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Использование: python collect_files.py /path/to/input_dir /path/to/output_dir")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    collect_files(input_dir, output_dir)
