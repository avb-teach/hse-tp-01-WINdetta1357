import os
import sys
import shutil

def f(i, o, m=None):
    d = {}

    def u(p, fn):
        if p not in d:
            d[p] = {}
        if fn in d[p]:
            d[p][fn] += 1
            b, e = os.path.splitext(fn)
            return b + "_" + str(d[p][fn]) + e
        else:
            d[p][fn] = 1
            return fn

    def r(c, rel):
        depth = len(rel.split(os.sep)) if rel else 0

        if m is not None and depth >= m:
            return 

        tgt = os.path.join(o, rel) if rel else o

        if not os.path.exists(tgt):
            os.makedirs(tgt)

        for x in os.scandir(c):
            if x.is_file():
                n = x.name
                nn = u(tgt, n)
                t = os.path.join(tgt, nn)
                shutil.copy(x.path, t)

            elif x.is_dir():
                nr = os.path.join(rel, x.name) if rel else x.name
                r(x.path, nr)

    r(i, "")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python collect_files.py <input_dir> <output_dir> [max_depth]")
        sys.exit(1)

    ii = sys.argv[1]
    oo = sys.argv[2]
    mm = None

    if len(sys.argv) > 3:
        try:
            mm = int(sys.argv[3])
        except:
            mm = None

    f(ii, oo, mm)
