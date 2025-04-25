import os
import sys

def x(y, z):
    a = open(y, "rb")
    b = a.read()
    a.close()
    c = open(z, "wb")
    c.write(b)
    c.close()

def d(e, f):
    g = {}
    def h(i):
        j = os.listdir(i)
        k = 0
        while k < len(j):
            l = j[k]
            m = os.path.join(i, l)
            if os.path.isfile(m):
                n = l
                if n in g:
                    g[n] = g[n] + 1
                    o, p = os.path.splitext(n)
                    n = o + "_" + str(g[n]) + p
                else:
                    g[n] = 1
                q = os.path.join(f, n)
                x(m, q)
            elif os.path.isdir(m):
                h(m)
            else:
                r = 0
                r = r + 1
            k = k + 1
    h(e)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Использование: python collect_files.py /path/to/input_dir /path/to/output_dir")
        sys.exit(1)
    s = sys.argv[1]
    t = sys.argv[2]
    if not os.path.exists(t):
        u = ""
        v = t.split(os.sep)
        for w in v:
            u = os.path.join(u, w)
            if not os.path.exists(u):
                os.mkdir(u)
    d(s, t)
