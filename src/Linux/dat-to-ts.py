import os
import argparse

input_dat_file = 'data.dat'
output_ts_file = 'data.ts'

parser = argparse.ArgumentParser(description="create .ts fault from .dat file")
parser.add_argument("filename", help=".dat file")
args = parser.parse_args()

# Construct the command to run the conversion script
command = f"python3 ./Meshing/creating_geometric_models/create_fault_from_trace.py {args.filename} 0 90 --dd 0.5e3 --maxdepth 2.5e4 --extend 4e3"

# Run the command
os.system(command)
