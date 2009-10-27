
    #!/usr/bin/env python

    import sys
    import os 
    import string

    args = sys.argv

    if len(args) != 2:
       print 'Usage:', args[0], 'dummy'
       sys.exit()

    # PYGRDATAPATH for PYGR resources

      os.environ['PYGRDATAPATH'] = '/Users/deepreds/projects/test'

    # PYGRDATADOWNLOAD FOR SAVING GENOME ASSEMBLIES

      os.environ['PYGRDATADOWNLOAD'] = '/Users/deepreds/projects/test'

    import pygr.Data
    
    from pygr import seqdb
    
    from pygr.downloader import *

    from download_save_assemblies_sourceurl import sprotDict, docstringdict

    for lines in open('ftp_urls.txt', 'r').xreadlines():
    
    #ftp://hgdownload.cse.ucsc.edu/goldenPath/anoCar1/bigZips/anoCar1.fa.gz
    
    ftpurl = lines.strip()
     
    genomeassembly = lines.split('/')[-3]
    
    if not sprotDict.has_key(genomeassembly) or not docstringdict.has_key(genomeassembly): continue
    
    s = SourceURL(ftpurl, filename = genomeassembly + '.zip', singleFile = True)
    
    s.__doc__ = 'UCSC SourceURL for ' + genomeassembly
    
    pygr.Data.getResource.addResource('Bio.Seq.Genome.SourceURL.' + sprotDict[genomeassembly] + '.' + genomeassembly, s)

    pygr.Data.save()

    # Unpickling and save files, open SEQDB
 
    mylist = pygr.Data.dir('Bio.Seq.Genome.SourceURL')

    for pygrresource in mylist:

    # Unpickling and initiating downloading assemblies from ftp url
    
    localpath = pygr.Data.getResource(pygrresource)
    
    genomeassembly = pygrresource.split('.')[-1]
    
    s = seqdb.BlastDB(localpath)
    
    s.__doc__ = docstringdict[genomeassembly]
    
    pygr.Data.getResource.addResource('Bio.Seq.Genome.' + sprotDict[genomeassembly] + '.' + genomeassembly, s)

    pygr.Data.save()


    # [download_save_assemblies_sourceurl.py]

    #!/usr/bin/env python

    import sys 
    import os
    import string
    import glob

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
    'mm9': 'MOUSE', 'dm3': 'DROME', 'ce4': 'CAEEL', 'cb3': 'CAEBR', 'caeRem2': 'CAERE', 'danRer5': 'DANRE',
    'ponAbe2': 'PONPA', 'calJac1': 'CALJA', 'bosTau4': 'BOVIN'
    }

    docstringdict = {
    'anoCar1':'Lizard Genome (January 2007)',
    'anoGam1':'A. gambiae Genome (February 2003)',
    'apiMel2':'A. mellifera Genome (January 2005)',
    'apiMel3':'A. mellifera Genome (May 2005)',
    'bosTau2':'Cow Genome (March 2005)',
    'bosTau3':'Cow Genome (August 2006)',
    'bosTau4':'Cow Genome (October 2007)',
    'caeRem2':'C. remanei Genome (March 2006)',
    'calJac1':'Common marmoset Genome (June 2007)',
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
    'danRer5':'Zebrafish Genome (July 2007)',
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
    'ponAbe2':'Sumatran orangutan Genome (July 2007)',
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



