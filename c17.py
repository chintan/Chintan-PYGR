
    from pygr import sequence, cnestedlist, seqdb

    sequence_db = seqdb.BlastDB('example.fa')

    class Annotation:
   
        def __init__(self, name, id, start, stop):
        self.name = name
        self.id = id
        self.start = start
        self.stop = stop

    annot_dict1 = dict(g1 = Annotation('gene', 'chrI', 50, 500), g2 = Annotation('gene', 'chrI', 50, 100))

    annot_dict2 = dict(e1 = Annotation('exon', 'chrI', 50, 70), e2 = Annotation('exon', 'chrI', 100, 150))

    annotation_db1 = seqdb.AnnotationDB(annot_dict1, sequence_db)

    annotation_db2 = seqdb.AnnotationDB(annot_dict2, sequence_db)

    newUnion = seqdb.PrefixUnionDict({'example' : sequence_db, 'gene' : annotation_db1, 'exon' : annotation_db2})

    annotations_map = cnestedlist.NLMSA('test', 'w', newUnion, pairwiseMode=True)

    for v in annotation_db1.values():
        annotations_map.addAnnotation(v)

    for v in annotation_db2.values():
        annotations_map.addAnnotation(v)

    annotations_map.build(saveSeqDict=True)