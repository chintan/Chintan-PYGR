    
    #!/usr/bin/env python

    import sys
    import os
    import string
    import glob

    from pygr import seqdb, cnestedlist

    args = sys.argv

    if len(args) != 2:
       print 'Usage:', args[0], 'dummy'
       sys.exit()

    seqdir = '/data/GENOMES'

    os.environ['PYGRDATAPATH'] = seqdir

    import pygr.Data

    sprotDict = {
    'AaegL1': 'AEDAE', 'aedes1': 'AEDAE', 'amel2': 'APIME', 'anoCar1': 'ANOCA', 'anoGam1': 'ANOGA', 'apiMel2': 'APIME',
    'apiMel3': 'APIME', 'bomMor0': 'BOMMO', 'bosTau2': 'BOVIN', 'bosTau3': 'BOVIN', 'canFam2': 'CANFA',
    'cavPor2': 'CAVPO', 'ce2': 'CAEEL', 'ci2': 'CIOIN', 'CSAV2': 'CIOSA', 'danRer1': 'DANRE', 'danRer2': 'DANRE',
    'danRer3': 'DANRE', 'danRer4': 'DANRE', 'dasNov1': 'DASNO', 'dm2': 'DROME', 'dp3': 'DROPS', 'dp4': 'DROPS',
    'droAna1': 'DROAN', 'droAna2': 'DROAN', 'droAna3': 'DROAN', 'droEre1': 'DROER', 'droEre2': 'DROER',
    'droGri1': 'DROGR', 'droGri2': 'DROGR', 'droMoj1': 'DROMO', 'droMoj2': 'DROMO', 'droMoj3': 'DROMO',
    'droPer1': 'DROPE', 'droSec1': 'DROSE', 'droSim1': 'DROSI', 'droVir1': 'DROVI', 'droVir2': 'DROVI',
    'droVir3': 'DROVI', 'droWil1': 'DROWI', 'droYak1': 'DROYA', 'droYak2': 'DROYA', 'echTel1': 'ECHTE',
    'equCab1': 'HORSE', 'eriEur1': 'ERIEU', 'felCat3': 'FELCA', 'fr1': 'FUGRU', 'fr2': 'FUGRU', 'galGal2': 'CHICK',
    'galGal3': 'CHICK', 'gasAcu1': 'GASAC', 'hg17': 'HUMAN', 'hg18': 'HUMAN', 'loxAfr1': 'LOXAF', 'mm5': 'MOUSE',
    'mm6': 'MOUSE', 'mm7': 'MOUSE', 'mm8': 'MOUSE', 'monDom1': 'MONDO', 'monDom2': 'MONDO', 'monDom4': 'MONDO',
    'ornAna1': 'ORNAN', 'oryCun1': 'RABIT', 'oryLat1': 'ORYLA', 'otoGar1': 'OTOGA', 'panTro1': 'PANTR',
    'panTro2': 'PANTR', 'rheMac1': 'MACMU', 'rheMac2': 'MACMU', 'rn3': 'RAT', 'rn4': 'RAT', 'sacCer1': 'YEAST',
    'sorAra1': 'SORAR', 'Sscrofa2': 'PIG', 'strPur1': 'STRPU', 'tetNig1': 'TETNG',
    'triCas2': 'TRICA', 'tupBel1': 'TUPGB', 'xenTro1': 'XENTR', 'xenTro2': 'XENTR', 'priPac1': 'PRIPA',
    'mm9': 'MOUSE', 'dm3': 'DROME', 'ce4': 'CAEEL', 'cb3': 'CAEBR', 'caeRem2': 'CAERE'
    }

    docstringdict = {
    'anoCar1':' Lizard Genome (January 2007)',
    'anoGam1':'A. gambiae Genome (February 2003)',
    'apiMel2':'A. mellifera Genome (January 2005)',
    'apiMel3':'A. mellifera Genome (May 2005)',
    'bosTau2':'Cow Genome (March 2005)',
    'bosTau3':'Cow Genome (August 2006)',
    'caeRem2':'C. remanei Genome (March 2006)',
    'canFam2':'Dog Genome (May 2005)',
    'cavPor2':'Guinea Pig (October 2005)',
    'cb3':'C. briggsae Genome (January 2007)',
    'ce2':'C. elegans Genome (March 2004)',
    'ce4':'C. elegans Genome (January 2007)',
    'ci2': 'C. intestinalis Genome (March 2005)',
    'danRer1':'Zebrafish Genome (November 2003)',
    'danRer2':'Zebrafish Genome (Junuary 2004)',
    'danRer3':'Zebrafish Genome (May 2005)',
    'danRer4':'Zebrafish Genome (March 2006)',
    'dasNov1':'Armadillo Genome (May 2005)',
    'dm2':'D. melanogaster Genome (April 2004)',
    'dm3':'D. melanogaster Genome (April 2006)',
    'dp3':'D. pseudoobscura Genome (November 2004)',
    'dp4':'D. pseudoobscura Genome (February 2006)',
    'droAna1':'D. ananassae Genome (July 2004)',
    'droAna2':'D. ananassae Genome (August 2005)',
    'droAna3':'D. ananassae Genome (February 2006)',
    'droEre1':'D. erecta Genome (August 2005)',
    'droEre2':'D. erecta Genome (February 2006)',
    'droGri1':'D. grimshawi Genome (August 2005)',
    'droGri2':'D. grimshawi Genome (February 2006)',
    'droMoj1':'D. mojavensis Genome (August 2004)',
    'droMoj2':'D. mojavensis Genome (August 2005)',
    'droMoj3':'D. mojavensis Genome (February 2006)',
    'droPer1':'D. persimilis Genome (October 2005)',
    'droSec1':'D. sechellia Genome (October 2005)',
    'droSim1':'D. simulans Genome (April 2005)',
    'droVir1':'D. virilis Genome (July 2004)',
    'droVir2':'D. virilis Genome (August 2005)',
    'droVir3':'D. virilis Genome (February 2006)',
    'droWil1':'D. willistoni Genome (February 2006)',
    'droYak1':'D. yakuba Genome (April 2004)',
    'droYak2':'D. yakuba Genome (November 2005)',
    'echTel1':'Tenrec Genome (July 2005)',
    'eriEur1':'European Hedgehog (Junuary 2006)',
    'equCab1':'Horse Genome (January 2007)',
    'felCat3':'Cat Genome (March 2006)',
    'fr1':'Fugu Genome (August 2002)',
    'fr2':'Fugu Genome (October 2004)',
    'galGal2':'Chicken Genome (February 2004)',
    'galGal3':'Chicken Genome (May 2006)',
    'gasAcu1':'Stickleback Genome (February 2006)',
    'hg17':'Human Genome (May 2004)',
    'hg18':'Human Genome (May 2006)',
    'loxAfr1':'Elephant Genome (May 2005)',
    'mm5':'Mouse Genome (May 2004)',
    'mm6':'Mouse Genome (March 2005)',
    'mm7':'Mouse Genome (August 2005)',
    'mm8':'Mouse Genome (March 2006)',
    'mm9':'Mouse Genome (July 2007)',
    'monDom1':'Opossum Genome (October 2004)',
    'monDom2':'Opossum Genome (June 2005)',
    'monDom4':'Opossum Genome (January 2006)',
    'ornAna1':'Platypus Genome (March 2007)',
    'oryCun1':'Rabbit Genome (May 2005)',
    'oryLat1':'Medaka Genome (April 2006)',
    'otoGar1':'Bushbaby Genome (December 2006)',
    'panTro1':'Chimpanzee Genome (November 2003)',
    'panTro2':'Chimpanzee Genome (March 2006)',
    'priPac1':'P. pacificus Genome (February 2007)',
    'rheMac1':'Rhesus Genome (January 2005)',
    'rheMac2':'Rhesus Genome (January 2006)',
    'rn3':'Rat Genome (June 2003)',
    'rn4':'Rat Genome (November 2004)',
    'sacCer1':'Yeast (S. cerevisiae) Genome (October 2003)',
    'sorAra1':'Shrew (Junuary 2006)',
    'strPur1':'S. purpuratus Genome (April 2005)',
    'tetNig1':'Tetraodon Genome (February 2004)',
    'tupBel1':'Tree Shrew (December 2006)',
    'triCas2':'T. castaneum Genome (September 2005)',
    'xenTro1':'X. tropicalis Genome (October 2004)',
    'xenTro2':'X. tropicalis Genome (August 2005)'
    }

    seqlist = glob.glob(os.path.join(seqdir, '*.seqlen'))

    for seqname in seqlist:
        genoname = os.path.basename(seqname)[:-7]
    
    if not docstringdict.has_key(genoname) or not sprotDict.has_key(genoname): continue
       genome = seqdb.BlastDB(os.path.join(seqdir, genoname))
       genome.__doc__ = docstringdict[genoname]
       pygr.Data.getResource.addResource('Bio.Seq.Genome.' + sprotDict[genoname] + '.' + genoname, genome)
   
    #Print genoname + '\t' + 'Bio.Seq.Genome.' + sprotDict[genoname] + '.' + genoname

    pygr.Data.save()

    [deepreds@mbi136-219 src_update]$ more 2_register_seqdb.txt
    
    priPac1 Bio.Seq.Genome.PRIPA.priPac1

    droPer1 Bio.Seq.Genome.DROPE.droPer1
    ce2     Bio.Seq.Genome.CAEEL.ce2
    mm9     Bio.Seq.Genome.MOUSE.mm9
    apiMel3 Bio.Seq.Genome.APIME.apiMel3
    cb3     Bio.Seq.Genome.CAEBR.cb3
    ce4     Bio.Seq.Genome.CAEEL.ce4
    droEre2 Bio.Seq.Genome.DROER.droEre2
    ci2     Bio.Seq.Genome.CIOIN.ci2
    dm3     Bio.Seq.Genome.DROME.dm3
    droSec1 Bio.Seq.Genome.DROSE.droSec1
    xenTro2 Bio.Seq.Genome.XENTR.xenTro2
    panTro1 Bio.Seq.Genome.PANTR.panTro1
    caeRem2 Bio.Seq.Genome.CAERE.caeRem2
    gasAcu1 Bio.Seq.Genome.GASAC.gasAcu1
    droGri2 Bio.Seq.Genome.DROGR.droGri2
    droMoj1 Bio.Seq.Genome.DROMO.droMoj1
    oryLat1 Bio.Seq.Genome.ORYLA.oryLat1
    droMoj2 Bio.Seq.Genome.DROMO.droMoj2
    mm8     Bio.Seq.Genome.MOUSE.mm8
    xenTro1 Bio.Seq.Genome.XENTR.xenTro1
    droYak1 Bio.Seq.Genome.DROYA.droYak1
    felCat3 Bio.Seq.Genome.FELCA.felCat3
    droYak2 Bio.Seq.Genome.DROYA.droYak2
    droAna1 Bio.Seq.Genome.DROAN.droAna1
    anoGam1 Bio.Seq.Genome.ANOGA.anoGam1
    hg17    Bio.Seq.Genome.HUMAN.hg17
    monDom4 Bio.Seq.Genome.MONDO.monDom4
    monDom1 Bio.Seq.Genome.MONDO.monDom1
    dp4     Bio.Seq.Genome.DROPS.dp4
    danRer4 Bio.Seq.Genome.DANRE.danRer4
    rn3     Bio.Seq.Genome.RAT.rn3
    droEre1 Bio.Seq.Genome.DROER.droEre1
    anoCar1 Bio.Seq.Genome.ANOCA.anoCar1
    monDom2 Bio.Seq.Genome.MONDO.monDom2
    droVir1 Bio.Seq.Genome.DROVI.droVir1
    droAna3 Bio.Seq.Genome.DROAN.droAna3
    droSim1 Bio.Seq.Genome.DROSI.droSim1
    equCab1 Bio.Seq.Genome.HORSE.equCab1
    galGal3 Bio.Seq.Genome.CHICK.galGal3
    droMoj3 Bio.Seq.Genome.DROMO.droMoj3
    rn4     Bio.Seq.Genome.RAT.rn4
    droWil1 Bio.Seq.Genome.DROWI.droWil1
    dp3     Bio.Seq.Genome.DROPS.dp3
    rheMac2 Bio.Seq.Genome.MACMU.rheMac2
    ornAna1 Bio.Seq.Genome.ORNAN.ornAna1
    mm5     Bio.Seq.Genome.MOUSE.mm5
    oryCun1 Bio.Seq.Genome.RABIT.oryCun1
    rheMac1 Bio.Seq.Genome.MACMU.rheMac1
    droAna2 Bio.Seq.Genome.DROAN.droAna2
    canFam2 Bio.Seq.Genome.CANFA.canFam2
    fr1     Bio.Seq.Genome.FUGRU.fr1
    loxAfr1 Bio.Seq.Genome.LOXAF.loxAfr1
    droGri1 Bio.Seq.Genome.DROGR.droGri1
    dasNov1 Bio.Seq.Genome.DASNO.dasNov1
    triCas2 Bio.Seq.Genome.TRICA.triCas2
    mm7     Bio.Seq.Genome.MOUSE.mm7
    danRer2 Bio.Seq.Genome.DANRE.danRer2
    mm6     Bio.Seq.Genome.MOUSE.mm6
    bosTau2 Bio.Seq.Genome.BOVIN.bosTau2
    apiMel2 Bio.Seq.Genome.APIME.apiMel2
    fr2     Bio.Seq.Genome.FUGRU.fr2
    danRer3 Bio.Seq.Genome.DANRE.danRer3
    tetNig1 Bio.Seq.Genome.TETNG.tetNig1
    echTel1 Bio.Seq.Genome.ECHTE.echTel1
    danRer1 Bio.Seq.Genome.DANRE.danRer1
    dm2     Bio.Seq.Genome.DROME.dm2
    panTro2 Bio.Seq.Genome.PANTR.panTro2
    galGal2 Bio.Seq.Genome.CHICK.galGal2
    droVir2 Bio.Seq.Genome.DROVI.droVir2
    hg18    Bio.Seq.Genome.HUMAN.hg18
    droVir3 Bio.Seq.Genome.DROVI.droVir3
    sacCer1 Bio.Seq.Genome.YEAST.sacCer1
    strPur1 Bio.Seq.Genome.STRPU.strPur1
    sorAra1 Bio.Seq.Genome.SORAR.sorAra1
    otoGar1 Bio.Seq.Genome.OTOGA.otoGar1
    tupBel1 Bio.Seq.Genome.TUPGB.tupBel1
    cavPor2 Bio.Seq.Genome.CAVPO.cavPor2
    bosTau3 Bio.Seq.Genome.BOVIN.bosTau3
    eriEur1 Bio.Seq.Genome.ERIEU.eriEur1

    # If you are saving NLMSA into /data/NLMSA directory,

    # [deepreds@mbi136-219 src_update]$ more 4_textfile_to_binaries.py

    #!/usr/bin/env python

    import sys
    import os 
    import string
    import glob
    
    from pygr import cnestedlist

    args = sys.argv

    if len(args) != 2:
        print 'Usage:', args[0], 'dummy'
        sys.exit()

    genoDict = {}

    for lines in open('2_register_seqdb.txt', 'r').xreadlines():
        genoname, pygrstr = lines.splitlines()[0].split('\t')
        genoDict[genoname] = pygrstr

    seqdir = '/data/GENOMES'

    msadir = '/data/NLMSA'

    os.environ['PYGRDATAPATH'] = seqdir
    
    import pygr.Data

    os.chdir(msadir)

    gzlist = glob.glob('*.txt.gz')
 
    gzlist.sort()
    
    for gzname in gzlist:
        q = 'gzip -d ' + gzname
        os.system(q)
    
    txtname = gzname[:-3]
    
    msaname = txtname[:-4]
    
    cnestedlist.textfile_to_binaries(txtname)
    
    msa = cnestedlist.NLMSA(os.path.join(msadir, msaname))
    
    seqlist = msa.seqDict.prefixDict.keys()
    
    seqlist.sort()
    
    myorg, mymultiz = string.split(msaname, '_')
    
    msa.__doc__ = myorg + ' referenced ' + mymultiz + ' alignments (' + ', '.join(seqlist) + ')'
    
    # For genoname, genome in msa.seqDict.prefixDict.items():
    # pygr.Data.getResource.addResource(genoDict[genoname], genome)
    # Latest Version of PYGR, textfile_to_binaries() automatically verifies that the genomes are available
    # pygr.Data, and saves them as pygr.Data ids in the output binaries without any need for user intervention    
   
    pygr.Data.getResource.addResource('Bio.MSA.UCSC.' + msaname, msa)
    
    pygr.Data.save()
    
    os.remove(txtname)


