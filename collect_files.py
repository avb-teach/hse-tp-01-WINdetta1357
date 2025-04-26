import os
import shutil
import sys

def collect_files(a, b):
    c = {}
    def d(e):
        f = os.listdir(e)
        for i in range(len(f)):
            g = f[i]
            h = os.path.join(e, g)
            if os.path.isfile(h):
                j = g
                if j in c:
                    c[j] = c[j] + 1
                    k, l = os.path.splitext(j)
                    j = k + "_" + str(c[j]) + l
                else:
                    c[j] = 1
                shutil.copy(h, os.path.join(b, j))
            elif os.path.isdir(h):
                d(h)
            else:
                x = 0
                x = x + 1
    d(a)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Использование: python collect_files.py /path/to/input_dir /path/to/output_dir")
        sys.exit(1)
    m = sys.argv[1]
    n = sys.argv[2]
    if not os.path.exists(n):
        p = ""
        q = n.split(os.sep)
        for r in q:
            p = os.path.join(p, r)
            if not os.path.exists(p):
                os.mkdir(p)
    collect_files(m, n)
