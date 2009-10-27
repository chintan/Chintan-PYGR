
    #! If your sequence file name is "test", you can simply load that sequences using pygr.

    #! >>> from pygr import seqdb

    #! >>> sprot = seqdb.BlastDB('test')

    #! Pygr will automatically generate test.seqlen and test.pureseq files. test.seqlen file is for saving coordinates and identifiers information to access your sequences (python shelve file), and test.pureseq file is sequence only file without sequence header.