#!/usr/bin/env python3

coreSeq=("OTU352:","OTU726:","OTU269:",
"OTU287:","OTU250:","OTU257:","OTU84:")

with open('otus_95_combo_nolb.fasta', 'r') as zoop:
        refseq = zoop.readlines()

with open('seqs_woodCoreMycobiom.fasta', 'w') as goop:
        for j,otu in enumerate(coreSeq):
                for i,line in enumerate(refseq):
                        if otu in line:
                                goop.write(line)
                                goop.write(refseq[i+1])
