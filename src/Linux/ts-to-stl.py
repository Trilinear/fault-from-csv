import os
import argparse
import shutil

parser = argparse.ArgumentParser(description="create .stl fault from .ts, the python script will create the files in the same folder")
parser.add_argument("mode", help="0 = single file, 1 = folder", type=int)
parser.add_argument("--filename", metavar = "location", help=".ts file", default="")
parser.add_argument("--location", nargs=1, metavar="location", help="directory location", default="")
args = parser.parse_args()
args.location = ''.join(args.location)
parser.add_argument("--write_location", nargs=1, metavar="write_location", help="where you want to create at", default=args.location)
args = parser.parse_args()

args.location = ''.join(args.location)
args.write_location = ''.join(args.write_location)

def createFile(file):
    if extension == 'ts':
        try:
            os.system('python3 ./Meshing/creating_geometric_models/convertTs.py ' + baseName + '.ts ' + baseName + '.stl')
            if (args.write_location != ''):
                if os.path.exists(args.write_location + baseName + '.stl'):
                    os.remove(args.write_location + baseName + '.stl')
                shutil.move(baseName + '.stl', args.write_location)
        except:
            print("Keyword python3 does not work or file location not accessible")
            print(type(file))
            print(type(baseName))
            print(baseName)

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
