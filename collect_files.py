import os
import shutil
import sys

def collect_files(input_dir, output_dir, max_depth=None):
    file_count = {}

    def process_directory(directory, rel_path=""):
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
                target_file = os.path.join(current_output_dir, new_name)
                shutil.copy(entry.path, target_file)
                if max_depth is not None:
                    full_rel = os.path.join(rel_path, new_name)
                    parts = full_rel.split(os.sep)
                    if len(parts) > max_depth:
                        lifted_rel = os.path.join(*parts[-max_depth:])
                        lifted_target = os.path.join(output_dir, lifted_rel)
                        lifted_dir = os.path.dirname(lifted_target)
                        if not os.path.exists(lifted_dir):
                            os.makedirs(lifted_dir)
                        shutil.copy(entry.path, lifted_target)
            elif entry.is_dir():
                new_rel = os.path.join(rel_path, entry.name) if rel_path else entry.name
                process_directory(entry.path, new_rel)
    process_directory(input_dir)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Использование: python collect_files.py /path/to/input_dir /path/to/output_dir [max_depth]")
        sys.exit(1)
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    max_depth = int(sys.argv[3]) if len(sys.argv) > 3 else None
    collect_files(input_dir, output_dir, max_depth)
