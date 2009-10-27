
    #!First, you have to check whether you have installed BLAST or not. "formatdb" command should be in your PATH.


    #!If your sequence file name is "test" and you had already created BlastDB object, you can create BLAST database by simple function.
 
    #!>>> from pygr import seqdb

    #!>>> testdb = seqdb.BlastDB('test')
   
    #!>>> testdb.formatdb()
   
    #!Building index: formatdb -i est.fa -o T -p F