import os
import argparse
import csv
import shutil

parser = argparse.ArgumentParser(description="converts .csv file into .stl file for use in gmsh")
parser.add_argument("mode", help="0 = single file, 1 = folder", type=int)
parser.add_argument("--filename", metavar = "location", help=".csv file", default="")
parser.add_argument("--location", nargs=1, metavar="location", help="directory location", default="")
args = parser.parse_args()
args.location = ''.join(args.location)
parser.add_argument("--write_location", nargs=1, metavar="write_location", help="where you want to create at", default=args.location)
args = parser.parse_args()

args.location = ''.join(args.location)
args.write_location = ''.join(args.write_location)


def createDAT(file):
    readFile = csv.DictReader(file)
    northing = []
    easting = []
    for col in readFile:
        northing.append(col['UTMNorth'])
        easting.append(col['UTMEast'])
    writeDAT(file, northing, easting)
    return file

def writeDAT(file, northing, easting):
    if len(northing) == len(easting):
        # This is for old instances of .dat file
        if os.path.exists(baseName + '.dat'):
            os.remove(baseName + '.dat')
        # Writes Northing and Easting in scientific notation
        with open(args.write_location + baseName + '.dat', 'a') as f:
            northing = [str(i).replace(",", "") for i in northing]
            easting = [str(i).replace(",", "") for i in easting]
            for index in range(len(northing)):
                northingInExponent = format(float(northing[index]), '.10e')
                eastingInExponent = format(float(easting[index]), '.10e')
                f.write(northingInExponent + " " + 
                    eastingInExponent + " 0.0000000000e+00\n")
    else:
        raise SyntaxError('Northing list is not equal to Easting list')
    return 0

def writeTS(file):
    # Construct the command to run the conversion script
    command = f"python3 ./Meshing/creating_geometric_models/create_fault_from_trace.py {args.write_location + '/' + file} 0 90 --dd 0.5e3 --maxdepth 2.5e4 --extend 4e3"

    # Run the command
    os.system(command)

def createSTL(file):
        try:
            os.system('python3 ./Meshing/creating_geometric_models/convertTs.py ' + file + ' ' + args.write_location + baseName + '.stl')
            if (args.write_location != ''):
                if os.path.exists(args.write_location + baseName + '.stl'):
                    os.remove(args.write_location + baseName + '.stl')
                shutil.move(baseName + '.stl', args.write_location)
        except:
            print("Error occured, file location not accessible")

def cleanup():
    os.remove(args.write_location + baseName + '.dat')
    # os.remove(baseName + '0.ts')


if int(args.mode) == 0:
        filename = open(args.filename, 'r')
        base = os.path.basename(args.filename)
        baseName = base.split(".")[0]
        extension = base.split(".")[1]
        createDAT(filename)
        writeTS(baseName + '.dat')
        createSTL(baseName + '0.ts')
        cleanup()
        print(baseName)
else:
    for file in os.listdir(args.location):
        print(file)
        filename = open(args.location + file, 'r')
        base = os.path.basename(file)
        baseName = base.split(".")[0]
        extension = base.split(".")[1]
        createDAT(filename)
        print(filename)