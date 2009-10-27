
    #!/usr/bin/env python

    import sys 
    import os 
    import string

    args = sys.argv

    if len(args) != 3:
       print 'Usage:', args[0], 'inputfastadirectory outputfasta'
       sys.exit()

    filelist = os.listdir(args[1])

    outfile = open(args[2], 'w')

    for filename in filelist:
        for lines in open(filename, 'r').xreadlines():
        outfile.write(lines)

    outfile.close()

    #! If you saved your output fasta file as "test", you can simply load that sequences using pygr.

    #! >>> from pygr import seqdb

    #! >>> sprot = seqdb.BlastDB('test')