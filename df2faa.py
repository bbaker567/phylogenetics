#!/usr/bin/env python

import sys

csv = sys.argv[1] if len(sys.argv) > 1 else input("Dataframe file with comma-separated values: ")
out = csv.replace(".csv", ".faa")

try:
    with open(csv, "r") as csv_file, open(out, "w") as faa_file:
        next(csv_file)  # Skip the header line
        for line in csv_file:
            elements = line.strip().split(",")
            header = elements[0]
            seq = "".join(elements[1:])
            faa_file.write(f">{header}\n{seq}\n")
except IOError as e:
    print(f"Error: {str(e)}")
