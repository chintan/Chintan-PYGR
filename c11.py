
    #!user/bin/env python

    import pygr.Data

    from pygr.seqdb import BlastDB, AnnotationDB

    seqdb = BlastDB('/somepath/hg18.fa')

    exon_slices = pygr.Data.Collection(path='exon_slices.db',mode='c',writeback=False)  # Store on disk

    exon_db = AnnotationDB(exon_slices, seqdb,sliceAttrDict=dict(id=0, exon_id=1, orientation=2, gene_id=3, start=4, stop=5))

    from pygr.cnestedlist import NLMSA 

    nlmsa = NLMSA('exonAnnot','w',use_virtual_lpo=True,bidirectional=False)           

    ifile = file('exonslice.txt')

    for line in ifile:
        row = [x for x in line.split()] # CONVERT TO LIST SO MUTABLE
        row[1] = int(row[1]) # CONVERT FROM STRING TO INTEGER
        exon_slices[row[1]] = row
        exon = exon_db[row[1]] # GET THE ANNOTATION OBJECT FOR THIS EXON
        nlmsa.addAnnotation(exon) # SAVE IT TO GENOME MAPPING
        exon_db.clear()

    nlmsa.build() # FINALIZE GENOME ALIGNMENT INDEXES

    ifile.close()

    pygr.Data.Bio.Seq.Genome.hg18 = seqdb  # SAVE TO pygr.Data

    pygr.Data.Bio.Annotation.hg18.exons = exon_db

    pygr.Data.Bio.Annotation.hg18.exonmap = nlmsa

    pygr.Data.schema.Bio.Annotation.hg18.exonmap = \
    
    pygr.Data.ManyToManyRelation(seqdb,bindAttrs=('exons',))

    pygr.Data.save()

    # [Note that to work with these results using the pygr.Data schema (i.e. to search a piece of genomic sequence using its "exons" attribute), you should make sure to load the data from pygr.Data.  To do this, start a new Python session and run a test like the following:]

    import pygr.Data

    hg18 = pygr.Data.Bio.Seq.Genome.hg18()

    chr16 = seqdb['chr1']
    
    qint = chr16[10000:20000] # an arbitrary genomic interval containing genes...

    for exon in qint.exons:
        print(exon)







