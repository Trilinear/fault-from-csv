import os
import argparse
import shutil

parser = argparse.ArgumentParser(description="create .stl fault from .ts, the python script will create the files in the same folder")
parser.add_argument("mode", help="0 = single file, 1 = folder", type=int)
parser.add_argument("--filename", metavar = "file", help=".ts file", default="")
parser.add_argument("--location", nargs=1, metavar="location", help="directory location", default="")
parser.add_argument("--write_location", nargs=1, metavar="write_location", help="where you want to create at", default="")
args = parser.parse_args()

if (args.location != ''):
    args.location = ''.join(args.location) + '/'
if (args.write_location != ''):
    args.write_location = ''.join(args.write_location) + '/'

def createFile():
    if extension == 'ts':
        try:
            os.system('python ./Meshing/creating_geometric_models/convertTs.py ' + args.filename + ' ' + baseName + '.stl')
            if (args.write_location != ''):
                if os.path.exists(args.write_location + baseName + '.stl'):
                    os.remove(args.write_location + baseName + '.stl')
                shutil.move(baseName + '.stl', args.write_location)
        except:
            print("Keyword python does not work or file location not accessible")

# For individual file mode
if int(args.mode) == 0:
    base = os.path.basename(args.filename)
    baseName = base.split(".")[0]
    extension = base.split(".")[1]
    createFile()
# For entire directory mode
elif int(args.mode) == 1:
    for file in os.listdir(args.location):
        args.filename = args.location + file
        base = os.path.basename(args.filename)
        baseName = base.split(".")[0]
        extension = base.split(".")[1]
        createFile()
