
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

    seqlist = ['hg18', 'panTro2', 'mm8', 'rn4', 'canFam2']

    for orgstr in seqlist:
        genomes[orgstr] = seqdb.BlastDB(orgstr)

    genomeUnion = seqdb.PrefixUnionDict(genomes)

    msaname = 'hg18_pairwise5way'
   
    mafdir = '/data/root2/' + msaname + '/'

    axtlist = glob.glob(os.path.join(axtdir, '*/*.axt')

    axtlist.sort()

    msa = cnestedlist.NLMSA(msaname, 'w', genomeUnion, axtFiles = axtlist) # axtFiles for axtNet (cf. mafFiles for MAF), FOR AXTNET FORMAT, YOU *MUST* GIVE *axtFiles =*msa.save_seq_dict() # IF YOU ARE NOT USING pygr.Data, YOU *MUST* SAVE SEQDICT.