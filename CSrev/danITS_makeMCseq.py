mcseq=("OTU256:Dc-X","OTU119:Dc-PosG","OTU106:Dc-PosG","OTU386:Dc-PosG",
"OTU306:Dc-PosG","OTU264:Dc-PosG","OTU407:Dc-PosG","OTU191:Dc-PosG",
"OTU270:Dc-PosG","OTU271:Dc-PosG","OTU220:Dc-PosG","OTU258:Dc-PosG",
"OTU526:Dc-PosG","OTU235:Dc-PosG","OTU560:Dc-PosG","OTU164:Dc-PosG",
"OTU608:Dc-PosG","OTU733:Dc-PosG","OTU358:Dc-PosG","OTU826:Dc-PosG",
"OTU1153:Dc-PosI","OTU4210:Dc-PosG","OTU3674:Dc-PosG","OTU12510:PosG",
"OTU3183:Dc-PosG","OTU3723:Dc-PosG","OTU4453:Dc-PosG","OTU10694:Dc-PosI"
"OTU77:1w","OTU298:2w","OTU87:17w","OTU12521:Dc-PosG"
"OTU8401:Dc-PosG","OTU12516:PosI","OTU1183:36w","OTU98:2w",
"OTU41:1w","OTU249:1w","OTU410:37w","OTU84:38w",
"OTU1520:30w","OTU8984:Dc-PosG","OTU8986:Dc-PosG","OTU7914:Dc-PosG",
"OTU9035:Dc-PosG","OTU10988:PosG","OTU9833:Dc-PosI","OTU186:1w",
"OTU471:5w","OTU192:1w","OTU28:2w","OTU1216:1w",
"OTU958:19w","OTU338:1w","OTU1292:32w","OTU18:9w",
"OTU6703:17w","OTU2954:1w","OTU161:2w","OTU387:2w",
"OTU2446:2w","OTU1279:15w","OTU2202:3w","OTU5187:68w",
"OTU250:4w","OTU1599:9w","OTU1973:131w","OTU3711:17w",
"OTU1612:18w","OTU6688:19w","OTU281:109w","OTU210:27w",
"OTU2860:70w","OTU839:57w","OTU2567:130w","OTU12503:PosG")

with open('otus_95_combo_nolb.fasta', 'r') as zoop:
        refseq = zoop.readlines()

with open('seqs_danITS95.fasta', 'w') as goop:
        for j,otu in enumerate(mcseq):
                for i,line in enumerate(refseq):
                        if otu in line:
                                goop.write(line)
                                goop.write(refseq[i+1])
