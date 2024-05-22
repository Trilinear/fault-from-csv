import os
import argparse

parser = argparse.ArgumentParser(description="create .stl fault from .ts, the python script will create the files in the same folder")
parser.add_argument("mode", help="0 = single file, 1 = folder", type=int)
parser.add_argument("--filename", metavar = "location", help="csv file", default="")
parser.add_argument("--location", nargs=1, metavar="location", help="directory location", default="")
args = parser.parse_args()

args.location = ''.join(args.location)


def createFile(file):
    if extension == 'ts':
        os.system('python ./Meshing/creating_geometric_models/convertTs.py ' + args.filename + ' ' + args.location + baseName + '.stl')

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