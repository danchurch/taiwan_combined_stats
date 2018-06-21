mcseq=("OTU167:Dc-X","OTU315:4w","OTU306:Dc-PosG","OTU386:Dc-PosG",
"OTU187:Dc-PosG","OTU891:1w","OTU762:Dc-X","OTU1214:9w",
"OTU1747:11w","OTU164:Dc-PosG","OTU1332:11w","OTU2003:Neg",
"OTU560:Dc-PosG","OTU1444:49w","OTU256:Dc-X","OTU1432:2w",
"OTU1549:104w","OTU6852:Neg","OTU417:1w","OTU84:38w",
"OTU1599:9w","OTU2831:5w","OTU46:60w","OTU2115:131w",
"OTU119:Dc-PosG","OTU220:Dc-PosG","OTU235:Dc-PosG","OTU264:Dc-PosG",
"OTU1183:36w","OTU64:1w","OTU409:4w","OTU437:1w",
"OTU18:9w","OTU414:13w","OTU655:1w","OTU2029:2w",
"OTU250:4w","OTU7329:38w","OTU925:133w","OTU1496:23w",
"OTU588:32w","OTU1888:25w","OTU972:130w")

with open('otus_95_combo_nolb.fasta', 'r') as zoop:
        refseq = zoop.readlines()

with open('mcseq.txt', 'w') as goop:
        for j,otu in enumerate(mcseq):
                for i,line in enumerate(refseq):
                        if otu in line:
                                goop.write(line)
                                goop.write(refseq[i+1])


