#!bin/python
import os, getopt, argparse, sys

parser=argparse.ArgumentParser(
    description='''Simple script to enumerate the number of markers attributed to each MAG.''')
parser.add_argument('accessions', type=str, help="provide absolute path to accessions list file")
parser.add_argument('directory', type=str, help="provide absolute path to directory with marker files to be enumerated")
args=parser.parse_args()

acc=args.accessions
dir=args.directory

with open(acc) as file:
    lines = []
    for line in file:
        lines.append(line.rstrip())

for i in lines:
    count=0
    for filename in os.listdir(dir):
        filepath = os.path.join(dir, filename)
        with open(filepath, 'r') as fp:
            for line in fp:
                # String to search for:
                count += line.count(i)
    print (i + ":" + "\t" + str(count))

