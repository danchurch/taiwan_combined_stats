#!/usr/bin/env python3

coreSeq=("OTU19:","OTU202:","OTU10:","OTU17:",
 "OTU15:","OTU27:","OTU94:","OTU91:",
 "OTU239:","OTU16:","OTU199:","OTU678:")

with open('otus_95_combo_nolb.fasta', 'r') as zoop:
        refseq = zoop.readlines()

with open('seqs_leafCoreMycobiom.fasta', 'w') as goop:
        for j,otu in enumerate(coreSeq):
                for i,line in enumerate(refseq):
                        if otu in line:
                                goop.write(line)
                                goop.write(refseq[i+1])
