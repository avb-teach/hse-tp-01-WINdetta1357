import os
import sys

def collect_files(INPUT_DIR, outDir, MAX_DEPTH):
    fileCountMap = dict()
    keysList = []

    def get_name_ext(filename):
        parts = filename.split('.')
        if len(parts) == 1:
            return filename, ''
        else:
            ext = '.' + parts[-1]
            name = '.'.join(parts[:-1])
            return name, ext

    def processDir(dir1, currentDepth):
        if currentDepth > MAX_DEPTH:
            return
        entries = os.scandir(dir1)
        for e in entries:
            if e.is_file():
                fullFileName = e.name
                originalName = fullFileName

                if fullFileName in keysList:
                    fileCountMap[fullFileName] = fileCountMap[fullFileName] + 1
                    namePart, extPart = get_name_ext(fullFileName)
                    fullFileName = namePart + "_" + str(fileCountMap[originalName]) + extPart
                else:
                    fileCountMap[fullFileName] = 1
                    keysList.append(fullFileName)

                srcPath = e.path
                destPath = outDir + '/' + fullFileName

                print("Копирую файл: " + fullFileName)

                with open(srcPath, 'rb') as f1:
                    data = f1.read()
                with open(destPath, 'wb') as f2:
                    f2.write(data)

            elif e.is_dir():
                callAgain(e.path, currentDepth + 1)

    def callAgain(x1, d):
        processDir(x1, d)

    callAgain(INPUT_DIR, 0)

if __name__ == "__main__":
    inpPath = sys.argv[1]
    outPath = sys.argv[2]
    depthInt = int(sys.argv[3])

    if not os.path.exists(outPath):
        os.mkdir(outPath)

    collect_files(inpPath, outPath, depthInt)
