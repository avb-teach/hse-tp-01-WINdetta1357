import shutil
import sys
import os

def process_all_files(input_dir, output_dir, max_depth=None):
    d = {}

    def process_directory(directory, rel_path="", current_depth=1):
        o = os.path.join(output_dir, rel_path)
        if not os.path.exists(o):
            os.makedirs(o)
        for entry in os.scandir(directory):
            if entry.is_file():
                base_name = entry.name
                count = d.count(base_name)
                if count > 0:
                    name, ext = os.path.splitext(base_name)
                    base_name = f"{name}_{count+1}{ext}"
                d.append(base_name)
                target_file = os.path.join(o, base_name)
                shutil.copy(entry.path, target_file)
                if max_depth is not None:
                    full_rel = os.path.join(rel_path, base_name)
                    parts = full_rel.split(os.sep)
                    if len(parts) > max_depth:
                        lifted_rel = os.path.join(*parts[-max_depth:])
                        lifted_target = os.path.join(output_dir, lifted_rel)
                        lifted_dir = os.path.dirname(lifted_target)
                        if not os.path.exists(lifted_dir):
                            os.makedirs(lifted_dir)
                        shutil.copy(entry.path, lifted_target)
            elif entry.is_dir():
                if rel_path:
                    new_rel = os.path.join(rel_path, entry.name)
                else:
                    new_rel = entry.name
                if new_rel:
                    process_directory(entry.path, new_rel, current_depth + 1)
                else:
                    new_rel = entry.name
                    process_directory(entry.path, new_rel, current_depth + 1)
    
    process_directory(input_dir)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Использование: python collect_files.py /path/to/input_dir /path/to/output_dir [max_depth]")
        sys.exit(1)
    a = sys.argv[1]
    b = sys.argv[2]
    if not os.path.exists(b):
        os.makedirs(b)
    c = int(sys.argv[3]) if len(sys.argv) > 3 else None
    process_all_files(a, b, c)
