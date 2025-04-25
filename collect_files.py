import os
import sys
import shutil


def collect_files(input_dir, output_dir, max_depth=None):
    def recurse(current_path, relative_path):

        current_depth = len(relative_path.split(os.sep)) if relative_path else 0

        target_dir = os.path.join(output_dir, relative_path) if relative_path else output_dir
        os.makedirs(target_dir, exist_ok=True)

        entries = sorted(os.scandir(current_path), key=lambda e: e.name)

        for entry in entries:
            if entry.is_file():
                target_path = os.path.join(target_dir, entry.name)
                shutil.copy(entry.path, target_path)

                if max_depth is not None:
                    if current_depth >= max_depth:
                        if max_depth > 1:
                            rel_parts = relative_path.split(os.sep)[-(max_depth - 1):]
                            lift_rel_path = os.path.join(*rel_parts)
                        else:
                            lift_rel_path = ""

                        lift_dir = os.path.join(output_dir, lift_rel_path)
                        os.makedirs(lift_dir, exist_ok=True)

                        lifted_file_path = os.path.join(lift_dir, entry.name)
                        shutil.copy(entry.path, lifted_file_path)

            elif entry.is_dir():
                if max_depth is not None:
                    if current_depth >= max_depth:
                        continue

                next_rel_path = os.path.join(relative_path, entry.name) if relative_path else entry.name
                recurse(entry.path, next_rel_path)

    recurse(input_dir, "")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python collect_files.py <input_dir> <output_dir> [max_depth]")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    max_depth = int(sys.argv[3]) if len(sys.argv) > 3 else None

    collect_files(input_dir, output_dir, max_depth)
