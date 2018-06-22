mcseq=("OTU256:Dc-X","OTU306:Dc-PosG","OTU119:Dc-PosG","OTU220:Dc-PosG",
"OTU270:Dc-PosG","OTU191:Dc-PosG","OTU164:Dc-PosG","OTU235:Dc-PosG",
"OTU358:Dc-PosG","OTU106:Dc-PosG","OTU3674:Dc-PosG","OTU386:Dc-PosG",
"OTU271:Dc-PosG","OTU407:Dc-PosG","OTU258:Dc-PosG","OTU264:Dc-PosG",
"OTU4210:Dc-PosG","OTU1153:Dc-PosI","OTU8984:Dc-PosG","OTU526:Dc-PosG",
"OTU12510:PosG","OTU3723:Dc-PosG","OTU4453:Dc-PosG","OTU608:Dc-PosG",
"OTU3183:Dc-PosG","OTU826:Dc-PosG","OTU733:Dc-PosG","OTU8986:Dc-PosG",
"OTU9035:Dc-PosG","OTU8401:Dc-PosG","OTU560:Dc-PosG","OTU10988:PosG",
"OTU9833:Dc-PosI","OTU248:20w","OTU152:1w","OTU77:1w",
"OTU28:2w","OTU249:1w","OTU18:9w","OTU5738:17w",
"OTU610:1w","OTU1075:100w","OTU391:2w","OTU1524:3w",
"OTU257:3w","OTU7955:106w","OTU5111:14w","OTU84:38w",
"OTU1124:36w","OTU1466:9w","OTU1214:9w","OTU1941:17w",
"OTU428:45w","OTU2567:130w","OTU1516:133w","OTU1866:133w",
"OTU12502:PosG","OTU12503:PosG")

with open('otus_95_combo_nolb.fasta', 'r') as zoop:
        refseq = zoop.readlines()

with open('mcblast_dangen95.csv', 'w') as goop:
        for j,otu in enumerate(mcseq):
                for i,line in enumerate(refseq):
                        if otu in line:
                                goop.write(line)
                                goop.write(refseq[i+1])
