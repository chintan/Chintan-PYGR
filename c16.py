
    #!/usr/bin/env python

    import sys
    import os 
    import string
    import glob

    from pygr import seqdb, cnestedlist

    os.environ['PYGRDATAPATH'] = 'http://biodb2.bioinformatics.ucla.edu:5000'

    import pygr.Data

    # hg18 = seqdb.BlastDB('/result/pygr_data/hg18')

    hg18 = pygr.Data.Bio.Seq.Genome.HUMAN.hg18()

    genomedict = {'hg18':hg18}

    uniondict = seqdb.PrefixUnionDict(genomedict)

    axtlist = []

    dirlist = ['hg18_self']

    for dirname in dirlist:
        axtlist += glob.glob(os.path.join(dirname, '*.axt'))

    msa = cnestedlist.NLMSA('hg18_self', 'w', uniondict, axtFiles = axtlist)
 
    msa.save_seq_dict()

   # Instead of creating BlastDB in local machine, we can share BlastDB over XMLRPC and create NLMSA using that         BlastDB.