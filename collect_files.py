import os
import sys

def collect_files(INPUT_DIR, outDir):
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

    def processDir(dir1):
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
                destName = fullFileName
                destPath = outDir + '/' + destName

                print("Копирую файл: " + destName)

                with open(srcPath, 'rb') as f1:
                    data = f1.read()
                with open(destPath, 'wb') as f2:
                    f2.write(data)

            elif e.is_dir():
                nameOfDir = e.path
                callAgain(nameOfDir)

    def callAgain(x1):
        processDir(x1)

    callAgain(INPUT_DIR)

if __name__ == "__main__":
    totalArguments = len(sys.argv)

    if totalArguments < 3:
        print("Использование: python collect_files.py /path/to/input_dir /path/to/output_dir")
        sys.exit(1)

    inpPath = sys.argv[1]
    outPath = sys.argv[2]

    exists = os.path.exists(outPath)
    if exists == False:
        os.mkdir(outPath)

    collect_files(inpPath, outPath)

