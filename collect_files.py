import os, sys, shutil

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
        if m is None:
            tgt = o
        else:
            if rel:
                tgt = os.path.join(o, rel)
            else:
                tgt = o
        if not os.path.exists(tgt):
            os.makedirs(tgt)
        if rel:
            rl = rel.split(os.sep)
        else:
            rl = []
        for x in os.scandir(c):
            if x.is_file():
                n = x.name
                nn = u(tgt, n)
                t = os.path.join(tgt, nn)
                shutil.copy(x.path, t)
                if m is not None:
                    if len(rl) >= m:
                        if m > 1:
                            new_rel = os.path.join(*rl[-(m - 1):])
                        else:
                            new_rel = ""
                        if new_rel:
                            lift_dir = os.path.join(o, new_rel)
                        else:
                            lift_dir = o
                        if not os.path.exists(lift_dir):
                            os.makedirs(lift_dir)
                        nn2 = u(lift_dir, n)
                        lt = os.path.join(lift_dir, nn2)
                        shutil.copy(x.path, lt)
            else:
                if x.is_dir():
                    if rel:
                        nr = os.path.join(rel, x.name)
                    else:
                        nr = x.name
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
