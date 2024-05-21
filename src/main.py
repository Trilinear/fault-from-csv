import os
import argparse
import csv

parser = argparse.ArgumentParser(description="create .dat fault trace from .csv")
parser.add_argument("filename", help="csv file")
args = parser.parse_args()

filename = open(args.filename, 'r')

base = os.path.basename(args.filename)
baseName = base.split(".")[0]

file = csv.DictReader(filename)

northing = []
easting = []

# Goes through columns in our file
for col in file:
    northing.append(col['UTMNorth'])
    easting.append(col['UTMEast'])

if len(northing) == len(easting):
    # This is for old instances of .dat file
    if os.path.exists(baseName + '.dat'):
        os.remove(baseName + '.dat')
    # Writes Northing and Easting in scientific notation
    with open(baseName + '.dat', 'a') as f:
        northing = [str(i).replace(",", "") for i in northing]
        easting = [str(i).replace(",", "") for i in easting]
        for index in range(len(northing)):
            northingInExponent = format(float(northing[index]), '.10e')
            eastingInExponent = format(float(easting[index]), '.10e')
            f.write(northingInExponent + " " + 
                eastingInExponent + " 0.0000000000e+00\n")
else:
    raise SyntaxError('Northing list is not equal to Easting list')