#!/usr/bin/env python

    import sys 
    import os 
    import string

    from pygr import cnestedlist

    args = sys.argv

    if len(args) != 2:
       print 'Usage:', args[0], 'dummy'
       sys.exit()

    cnestedlist.textfile_to_binaries('canFam2_multiz4way.txt')

    cnestedlist.textfile_to_binaries('danRer3_multiz5way.txt')
    
    cnestedlist.textfile_to_binaries('danRer4_multiz7way.txt')

    cnestedlist.textfile_to_binaries('dm2_multiz15way.txt')

    cnestedlist.textfile_to_binaries('dm2_multiz9way.txt')

    cnestedlist.textfile_to_binaries('galGal2_multiz7way.txt')

    cnestedlist.textfile_to_binaries('galGal3_multiz7way.txt')

    cnestedlist.textfile_to_binaries('hg17_multiz17way.txt')

    cnestedlist.textfile_to_binaries('hg18_multiz17way.txt')

    cnestedlist.textfile_to_binaries('mm7_multiz17way.txt')

    cnestedlist.textfile_to_binaries('mm8_multiz17way.txt')

    cnestedlist.textfile_to_binaries('rn4_multiz9way.txt')

    cnestedlist.textfile_to_binaries('xenTro1_multiz5way.txt')


 