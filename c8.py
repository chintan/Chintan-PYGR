   
    #!/usr/bin/env python

    import sys 
    import os 
    import string 
    import glob

    from pygr import seqdb

    from pygr import cnestedlist

    args = sys.argv

    if len(args) != 2:
       print 'Usage:', args[0], 'dummy'
       sys.exit()

    genomes = {}

    seqlist = ['hg18', 'panTro1', 'rheMac2', 'rn4', 'mm8', 'oryCun1', 'bosTau2', 'canFam2', 'dasNov1', 'loxAfr1',     'echTel1', 'monDom4', 'galGal2', 'xenTro1', 'tetNig1', 'fr1', 'danRer3'] # SHOULD BE ALL CHROMOSOME ASSEMBLIES 
    #! For Multigenome Alignments

    for orgstr in seqlist:
        genomes[orgstr] = seqdb.BlastDB(orgstr)

    genomeUnion = seqdb.PrefixUnionDict(genomes)

    msaname = 'hg18_multiz17way'
    
    mafdir = '/data/root2/' + msaname + '/'

    maflist = glob.glob(mafdir + '*.maf')
    
    maflist.sort()

    cnestedlist.NLMSA(msaname, 'w' , genomeUnion, maflist)

    # [ Note:Depending on your system, it would take several hours to finish. By default, it will use 1GB memory.          If you have less memory, you have to decrease file size. You can pass arguments as follows.

    #  cnestedlist.NLMSA(msaname, 'w', genomeUnion, maflist, maxlen = 536870912, maxint = 22369620) 

    # 500MB Version. It will use less than 750MB Memory at most.



