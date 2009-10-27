
    #!/usr/bin/env python

    from Bio import GenBank import sys,os,string

    args = sys.argv

    if len(args) != 3:       
       print 'Usage:', args[0], 'input_gbff output_fasta'
       sys.exit()

    outfile = open(args[2], 'w')

    gbfile = open(args[1], 'r')

    featureparser = GenBank.FeatureParser()

    gbiterator = GenBank.Iterator(gbfile, featureparser)

    while 1:
       cur_record = gbiterator.next()

       if cur_record is None: break
       outfile.write('>' + cur_record.id + '\n')
       cur_seq = cur_record.seq.tostring()

         for ix in range(0, len(cur_seq), 80): outfile.write(cur_seq[ix:ix+80] + '\n')

    outfile.close()