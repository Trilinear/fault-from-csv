import os
import argparse
import csv

parser = argparse.ArgumentParser(description="create .dat fault trace from .csv, the python script will create the files in the same folder")
parser.add_argument("mode", help="0 = single file, 1 = folder")
parser.add_argument("--filename", help="csv file", default="")
parser.add_argument("--location", nargs=1, metavar="location", help="directory location", default="")
args = parser.parse_args()

args.location = ''.join(args.location)
print(type(args.location))
print(args.location)

# Goes through columns in our file
def createFile(file):
    readFile = csv.DictReader(file)
    northing = []
    easting = []
    for col in readFile:
        northing.append(col['UTMNorth'])
        easting.append(col['UTMEast'])
    writeFile(file, northing, easting)
    return file

def writeFile(file, northing, easting):
    if len(northing) == len(easting):
        # This is for old instances of .dat file
        if os.path.exists(baseName + '.dat'):
            os.remove(baseName + '.dat')
        # Writes Northing and Easting in scientific notation
        with open(args.location + baseName + '.dat', 'a') as f:
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

if int(args.mode) == 0:
        filename = open(args.filename, 'r')
        base = os.path.basename(args.filename)
        baseName = base.split(".")[0]
        createFile(filename)
else:
    for file in os.listdir(args.location):
        print(file)
        filename = open(args.location + file, 'r')
        base = os.path.basename(file)
        baseName = base.split(".")[0]
        createFile(filename)


