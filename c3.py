
#!/usr/bin/env python

    import sys
    import os
    import string
    import operator
    import gzip

    args = sys.argv

    if len(args) != 3:

       print 'Usage:', args[0], 'inputdir outgfftag'

    sys.exit()

    if args[1][-1] != '/': 
 
       args[1] += '/'

       seqfiles = [i for i in os.listdir(args[1]) if i[-2:] == 'gz']

    seqfiles.sort()

    # List oforganism

    orgList = ['homo', 'mus', 'rattus', 'canis', 'gallus', 'danio', 'takifugu']

    # Libnamedict

    librarydict = {}

    for orgstr in orgList:

        librarydict.setdefault(orgstr, {}).setdefault('LibName', {})

        librarydict.setdefault(orgstr, {}).setdefault('LibCount', {})

    # Filedict

    filedict = {}

    # Variables

    gbAcc = ''

    gbGi = ''

    cloneId = ''

    seqEnd = ''

    libId = ''

    libName = ''

    organism = ''

    one_gff = []

    for seqfile in seqfiles:

        print 'Opening', seqfile

        cur_handler = gzip.GzipFile(args[1] + seqfile, 'r')

    while 1:

        lines = cur_handler.readline()

        if lines == '': 
           
           break

            if lines[:2] != '||':

               one_gff.append(lines)
  
               continue

    # To get gbAcc

    gbAcc = [i[16:].strip() for i in one_gff if i[:11] == 'GenBank Acc'][0]

    gbAcc = string.split(gbAcc, ' ')[0]

    # To get gbGi

    gbGi = [i[16:].strip() for i in one_gff if i[:10] == 'GenBank gi'][0]

    gbGi = string.split(gbGi, ' ')[0]

    # To get clone id & sequence end

    cloneId = [i[16:].strip() for i in one_gff if i[:8] == 'Clone Id']

        if len(cloneId):

           cloneId = cloneId[0]

            if '('in cloneId and')' in cloneId:

                  ix = cloneId.index('(') + 1

                  iy = cloneId.index(')')

                    if '3' in cloneId[ix:iy]:

                        seqEnd = '3'

            elif '5' in cloneId[ix:iy]:

                  seqEnd = '5'

            if '('in cloneId:

                  cloneId = cloneId[:cloneId.index('(')].strip()

            else:

                  cloneId = cloneId.strip()
 
       else:

             cloneId = ''

        # Purging invalid cloneID

       if cloneId in ['CA', 'IMAGE:']:

          cloneId = ''

       if '?' in cloneId: cloneId = ''

       # To get libName

          ilib = [i for i in range(len(one_gff)) if one_gff[:8] == 'Lib Name']

       if len(ilib):

          ix = ilib[0]

          libName = one_gff[ix][16:].strip()

            if ':' not in one_gff[ix+1][:16]:

               libName += one_gff[ix+1][16:].strip()

                 if ':' not in one_gff[ix+2][:16]:

                    libName += one_gff[ix+2][16:].strip()

                 if ':' not in one_gff[ix+3][:16]:

                    libName += one_gff[ix+3][16:].strip()

       else:

            libName = ''

    # To get libId

    libId = [i[16:].strip() for i in one_gff if i[:12] == 'dbEST lib id']

    if len(libId):

       libId = libId[0]

    else:

       libId = ''

    # To get organism, and filename

    organism = [i[16:].strip() for i in one_gff if i[:8] == 'Organism']

    if len(organism):

         organism = organism[0]

    else:

         organism = ' '

    myorgstr = string.split(organism.strip(), ' ')[0].lower()

    if myorgstr in orgList:

       if len(libId) and len(libName):

          librarydict[myorgstr]['LibName'][libId] = libName

       if len(libId):

          librarydict[myorgstr]['LibCount'].setdefault(libId, 0)

          librarydict[myorgstr]['LibCount'][libId] += 1

          filename = myorgstr + '_' + args[2] + '.dbEST'

          mystring = gbAcc + '\t' + gbGi + '\t' + cloneId + '\t' + seqEnd + '\t' + libId + '\n'

          try:

              filedict[filename].writelines(mystring)

          except:

                 filedict[filename] = open(filename, 'w')

                 filedict[filename].writelines(mystring)

    # Purging

    gbAcc = ''

    gbGi = ''

    cloneId = ''

    seqEnd = ''

    libId = ''

    libName = ''

    organism = ''

    one_gff = []

    if len(one_gff):

       raise 'Last Line not end with ||'

    for fname in filedict.keys():

       filedict[fname].close()

    for myorgstr in librarydict.keys():

       myfile = open(myorgstr + '_' + args[2] + '.dbESTlibrary', 'w')

    for lid in librarydict[myorgstr]['LibCount'].keys():

       mystr = lid + '\t' + str(librarydict[myorgstr]['LibCount'][lid]) + '\t' + librarydict[myorgstr]                    ['LibName'][lid] + '\n'

       myfile.write(mystr)

       myfile.close()

    sys.exit()
