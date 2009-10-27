
#!/usr/bin/env python

    import sys
    import os
    import string

    from pygr import seqdb, cnestedlist

    import pygr.Data

    args = sys.argv
    
    if len(args) != 2:
       print 'Usage:', args[0], 'dummy'
       sys.exit()

    seqdir = '/data/PYGRDATA/'

    canFam2_multiz4way = cnestedlist.NLMSA(seqdir + 'canFam2_multiz4way')

    for id, genome in canFam2_multiz4way.seqDict.prefixDict.items():
        pygr.Data.getResource.addResource('Bio.Seq.Genome.'+id, genome)
        pygr.Data.Bio.Seq.MSA.canFam2_multiz4way = canFam2_multiz4way

    danRer3_multiz5way = cnestedlist.NLMSA(seqdir + 'danRer3_multiz5way')

    for id, genome in danRer3_multiz5way.seqDict.prefixDict.items():
        pygr.Data.getResource.addResource('Bio.Seq.Genome.'+id, genome)
        pygr.Data.Bio.Seq.MSA.danRer3_multiz5way = danRer3_multiz5way

    danRer4_multiz7way = cnestedlist.NLMSA(seqdir + 'danRer4_multiz7way')

    for id, genome in danRer4_multiz7way.seqDict.prefixDict.items():
        pygr.Data.getResource.addResource('Bio.Seq.Genome.'+id, genome)
        pygr.Data.Bio.Seq.MSA.danRer4_multiz7way = danRer4_multiz7way

    dm2_multiz9way = cnestedlist.NLMSA(seqdir + 'dm2_multiz9way')

    for id, genome in dm2_multiz9way.seqDict.prefixDict.items():
        pygr.Data.getResource.addResource('Bio.Seq.Genome.'+id, genome)
        pygr.Data.Bio.Seq.MSA.dm2_multiz9way = dm2_multiz9way

    dm2_multiz15way = cnestedlist.NLMSA(seqdir + 'dm2_multiz15way')

    for id, genome in dm2_multiz15way.seqDict.prefixDict.items():
        pygr.Data.getResource.addResource('Bio.Seq.Genome.'+id, genome)
        pygr.Data.Bio.Seq.MSA.dm2_multiz15way = dm2_multiz15way

    galGal2_multiz7way = cnestedlist.NLMSA(seqdir + 'galGal2_multiz7way')

    for id, genome in galGal2_multiz7way.seqDict.prefixDict.items():
        pygr.Data.getResource.addResource('Bio.Seq.Genome.'+id, genome)
        pygr.Data.Bio.Seq.MSA.galGal2_multiz7way = galGal2_multiz7way

    galGal3_multiz7way = cnestedlist.NLMSA(seqdir + 'galGal3_multiz7way')
    
    for id, genome in galGal3_multiz7way.seqDict.prefixDict.items():
        pygr.Data.getResource.addResource('Bio.Seq.Genome.'+id, genome)
        pygr.Data.Bio.Seq.MSA.galGal3_multiz7way = galGal3_multiz7way

    hg17_multiz17way = cnestedlist.NLMSA(seqdir + 'hg17_multiz17way')

    for id, genome in hg17_multiz17way.seqDict.prefixDict.items():
        pygr.Data.getResource.addResource('Bio.Seq.Genome.'+id, genome)
        pygr.Data.Bio.Seq.MSA.hg17_multiz17way = hg17_multiz17way

    hg18_multiz17way = cnestedlist.NLMSA(seqdir + 'hg18_multiz17way')

    for id, genome in hg18_multiz17way.seqDict.prefixDict.items():
        pygr.Data.getResource.addResource('Bio.Seq.Genome.'+id, genome)
        pygr.Data.Bio.Seq.MSA.hg18_multiz17way = hg18_multiz17way

    mm7_multiz17way = cnestedlist.NLMSA(seqdir + 'mm7_multiz17way')

    for id, genome in mm7_multiz17way.seqDict.prefixDict.items():
        pygr.Data.getResource.addResource('Bio.Seq.Genome.'+id, genome)
        pygr.Data.Bio.Seq.MSA.mm7_multiz17way = mm7_multiz17way

    mm8_multiz17way = cnestedlist.NLMSA(seqdir + 'mm8_multiz17way')
    
    for id, genome in mm8_multiz17way.seqDict.prefixDict.items():
    	pygr.Data.getResource.addResource('Bio.Seq.Genome.'+id, genome)
	pygr.Data.Bio.Seq.MSA.mm8_multiz17way = mm8_multiz17way

    rn4_multiz9way = cnestedlist.NLMSA(seqdir + 'rn4_multiz9way')

    for id, genome in rn4_multiz9way.seqDict.prefixDict.items():
    	pygr.Data.getResource.addResource('Bio.Seq.Genome.'+id, genome)
	pygr.Data.Bio.Seq.MSA.rn4_multiz9way = rn4_multiz9way

    xenTro1_multiz5way = cnestedlist.NLMSA(seqdir + 'xenTro1_multiz5way')

    for id, genome in xenTro1_multiz5way.seqDict.prefixDict.items():
        pygr.Data.getResource.addResource('Bio.Seq.Genome.'+id, genome)
        pygr.Data.Bio.Seq.MSA.xenTro1_multiz5way = xenTro1_multiz5way

    gasAcu1_multiz8way = cnestedlist.NLMSA(seqdir + 'gasAcu1_multiz8way')

    for id, genome in gasAcu1_multiz8way.seqDict.prefixDict.items():
        pygr.Data.getResource.addResource('Bio.Seq.Genome.'+id, genome)
        pygr.Data.Bio.Seq.MSA.gasAcu1_multiz8way = gasAcu1_multiz8way


    pygr.Data.Bio.Seq.Genome.droAna2 = seqdb.BlastDB(seqdir + 'droAna2')

    pygr.Data.Bio.Seq.Genome.droEre1 = seqdb.BlastDB(seqdir + 'droEre1')

    pygr.Data.Bio.Seq.Genome.droGri1 = seqdb.BlastDB(seqdir + 'droGri1')

    pygr.Data.Bio.Seq.Genome.droMoj2 = seqdb.BlastDB(seqdir + 'droMoj2')

    pygr.Data.Bio.Seq.Genome.droVir2 = seqdb.BlastDB(seqdir + 'droVir2')

    pygr.Data.save() 
    

# [Note: ALL pygr.Data entries are not saved yet until you explicitly give pygr.Data.save()]



