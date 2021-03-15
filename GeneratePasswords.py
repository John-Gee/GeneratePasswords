#!/bin/python


import sys


def GetPWDS(tokens, l, st):
    for i in l:
        for alt in set(tokens[i]):
            if alt.startswith("^"):
                if (len(st) > 0):
                    break
                alt = alt[1:]
            elif alt.startswith("$"):
                if len(l) <= 1:
                    alt = alt[1:]
                else:
                    break
            elif alt.startswith("\\"):
                alt = alt[1:]
            if len(l) <= 1:
                print(st+alt)
            else:
                l2 = l.copy()
                l2.remove(i)
                GetPWDS(tokens, l2, st+alt)


if len(sys.argv) <= 1:
    print("Please input the tokens text file to this program!")
    print(f"python {sys.argv[0]} PATH_TO_TXT")
    exit(-1)

filename = sys.argv[1]

tokens   = []

with open(filename) as f:
    for line in f.read().splitlines():
        if(not line.startswith("#")):
            tokens.append(line.split())
    
l = []
for i in range(0, len(tokens)):
    l.append(i)

GetPWDS(tokens, l, "")
