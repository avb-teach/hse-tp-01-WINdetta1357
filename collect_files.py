import os
import sys
import shutil

def a(b, c, d=None):
    e = {}
    def f(g, h=""):
        lst = list(os.scandir(g))
        for i in range(len(lst)):
            j = lst[i]
            if j.is_file():
                k = j.name
                if k in e:
                    e[k] = e[k] + 1
                    m, n = os.path.splitext(k)
                    k = m + "_" + str(e[k]) + n
                else:
                    e[k] = 1
                p = os.path.join(c, h, k)
                shutil.copy(j.path, p)
                if d is not None:
                    q = os.path.join(h, k)
                    r = q.split(os.sep)
                    if len(r) > d:
                        s = os.path.join(*r[-d:])
                        t = os.path.join(c, s)
                        u = os.path.dirname(t)
                        if not os.path.exists(u):
                            os.makedirs(u)
                        shutil.copy(j.path, t)
            elif j.is_dir():
                v = os.path.join(h, j.name) if h != "" else j.name
                f(j.path, v)
    f(b, "")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python collect_files.py <input_dir> <output_dir> [max_depth]")
        sys.exit(1)
    w = sys.argv[1]
    x = sys.argv[2]
    if not os.path.exists(x):
        os.makedirs(x)
    y = None
    if len(sys.argv) > 3:
        y = int(sys.argv[3])
    a(w, x, y)
