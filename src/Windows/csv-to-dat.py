import os
import argparse
import csv

parser = argparse.ArgumentParser(description="create .dat fault trace from .csv, the python script will create the files in the same folder")
parser.add_argument("mode", help="0 = single file, 1 = folder")
parser.add_argument("--filename", help=".csv file", default="")
parser.add_argument("--location", nargs=1, metavar="location", help="directory location", default="")
parser.add_argument("--write_location", nargs=1, metavar="write_location", help="where you want to create at", default="")
args = parser.parse_args()

# '/' added to avoid scenarios where user inputs a directory with no / at the end, causes issues when it is missing
if (args.location != ''):
    args.location = ''.join(args.location) + '/'
if (args.write_location != ''):
    args.write_location = ''.join(args.write_location) + '/'



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

# For individual file mode
if int(args.mode) == 0:
    filename = open(args.filename, 'r')
    base = os.path.basename(args.filename)
    baseName = base.split(".")[0]
    extension = base.split(".")[1]
    createFile(filename)
# For entire directory mode
elif int(args.mode) == 1:
    for file in os.listdir(args.location):
        args.filename = args.location + file
        base = os.path.basename(args.filename)
        baseName = base.split(".")[0]
        extension = base.split(".")[1]
        filename = open(args.location + file, 'r')
        if extension == 'csv':
            createFile(filename)
