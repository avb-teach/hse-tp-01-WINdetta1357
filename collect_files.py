import os
import shutil
import sys

def collect_files(input_dir, output_dir, max_depth=None):
    file_count = {}

    def process_directory(directory, rel_path="", current_depth=0):
        if max_depth and current_depth >= max_depth:
            return
        current_output_dir = os.path.join(output_dir, rel_path)
        if not os.path.exists(current_output_dir):
            os.makedirs(current_output_dir)

        for entry in os.scandir(directory):
            if entry.is_file():
                base_name = entry.name
                if base_name in file_count:
                    file_count[base_name] += 1
                    name, ext = os.path.splitext(base_name)
                    new_name = name + "_" + str(file_count[base_name]) + ext
                else:
                    file_count[base_name] = 1
                    new_name = base_name
                shutil.copy(entry.path, os.path.join(current_output_dir, new_name))
                if max_depth:
                    parts = os.path.join(rel_path, new_name).split(os.sep)
                    if len(parts) > max_depth:
                        lifted_rel = os.path.join(*parts[-max_depth:])
                        lifted_target = os.path.join(output_dir, lifted_rel)
                        os.makedirs(os.path.dirname(lifted_target), exist_ok=True)
                        shutil.copy(entry.path, lifted_target)
            elif entry.is_dir():
                new_rel = os.path.join(rel_path, entry.name) if rel_path else entry.name
                process_directory(entry.path, new_rel, current_depth + 1)

    process_directory(input_dir)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Использование: python collect_files.py /path/to/input_dir /path/to/output_dir [max_depth]")
        sys.exit(1)
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    max_depth = int(sys.argv[3]) if len(sys.argv) > 3 else None

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    collect_files(input_dir, output_dir, max_depth)

