## biomsetup.R
##############################

library('VennDiagram')
library('phyloseq')
library('DESeq2')
library('vegan')
library('cooccur')
library('igraph')
library('ecodist')
library('ade4')
library('png')
library('randomcoloR')

biom95 <- import_biom('combo_otu_wMeta.biom', parseFunction=parse_taxonomy_greengenes)

neg95 <- subset_samples(biom95, sample_names(biom95)=='Neg')

##############################
