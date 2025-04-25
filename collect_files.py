import os
import sys
import shutil

def f(i, o, m=None):
    def r(c, rel):
        depth = len(rel.split(os.sep)) if rel else 0

        tgt = os.path.join(o, rel) if rel else o
        os.makedirs(tgt, exist_ok=True)

        rl = rel.split(os.sep) if rel else []

        for x in sorted(os.scandir(c), key=lambda e: e.name):
            if x.is_file():
                t = os.path.join(tgt, x.name)
                shutil.copy(x.path, t)

                if m is not None and depth >= m:
                    if m > 1:
                        new_rel = os.path.join(*rl[-(m - 1):])
                    else:
                        new_rel = ""

                    lift_dir = os.path.join(o, new_rel) if new_rel else o
                    os.makedirs(lift_dir, exist_ok=True)

                    lt = os.path.join(lift_dir, x.name)
                    shutil.copy(x.path, lt)

            elif x.is_dir():
                if m is not None and depth >= m:
                    continue
                nr = os.path.join(rel, x.name) if rel else x.name
                r(x.path, nr)

    r(i, "")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python collect_files.py <input_dir> <output_dir> [max_depth]")
        sys.exit(1)

    ii = sys.argv[1]
    oo = sys.argv[2]
    mm = int(sys.argv[3]) if len(sys.argv) > 3 else None
    f(ii, oo, mm)
