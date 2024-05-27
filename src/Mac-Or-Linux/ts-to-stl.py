import os
import argparse

parser = argparse.ArgumentParser(description="create .stl fault from .ts, the python script will create the files in the same folder")
parser.add_argument("mode", help="0 = single file, 1 = folder", type=int)
parser.add_argument("convertfile", help="the directory to the convertTs.py file from SeisSol Meshing repository")
parser.add_argument("--filename", metavar = "location", help=".ts file", default="")
parser.add_argument("--location", nargs=1, metavar="location", help="directory location", default="")
args = parser.parse_args()

args.location = ''.join(args.location)
args.convertFile = ''.join(args.convertFile)

def createFile(file):
    if extension == 'ts':
        try:
            os.system('python '+ args.convertfile + args.filename + ' ' + args.location + baseName + '.stl')
        except:
            print("Error occured, file location not accessible or keyword 'python' does not work, trying python3")
            try:
                os.system('python3 '+ args.convertfile + args.filename + ' ' + args.location + baseName + '.stl')
            except:
                print("Neither keywords python3 or python work, file location not accessible")

if args.mode == 0:
    filename = open(args.filename, 'r')
    base = os.path.basename(args.filename)
    baseName = base.split(".")[0]
    extension = base.split(".")[1]
    createFile(filename)
else:
    for file in os.listdir(args.location):
        args.filename = args.location + file
        base = os.path.basename(file)
        baseName = base.split(".")[0]
        extension = base.split(".")[1]
        filename = open(args.location + file, 'r')
        createFile(filename)
