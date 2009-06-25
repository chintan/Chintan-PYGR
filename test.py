#!/usr/bin/env python

import sys, os, string

args = sys.argv
if len(args) != 3:
    print 'Usage:', args[0], 'swissprot_raw_fasta output_fasta'
    sys.exit()

outfile = open(args[2], 'w')
for lines in open(args[1], 'r').xreadlines():
    if lines[0] == '>':
        # IF YOU WANT TO SAVE "1431_ARATH" AS YOUR IDENTIFIER
        myid = string.split(lines[1:], ' ')[0]
        # IF YOU WANT TO SAVE "Q9C5W6" AS YOUR IDENTIFIER
        if '(' not in lines or ')' not in lines:
            print 'ACCESSION NOT FOUND', lines[:-1]
            sys.exit()
        parenstart = lines.index('(')
        parenend = lines.index(')')
        myid = lines[parenstart+1:parenend]
        # SAVE FASTA HEADER
        outfile.write('>' + myid + '\n')
    else:
        # SAVE SEQUENCES
        outfile.write(lines)
outfile.close()