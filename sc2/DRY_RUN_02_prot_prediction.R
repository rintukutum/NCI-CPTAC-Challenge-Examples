
# path <- "/Users/miyang/Documents/RWTH_Aachen/DREAM_CPTAC/DOCKER_STORAGE/docker_R_sc2/"
path <- "/"

# load saved models
load(paste0(path,"model_storage/SAVE_WEIGHT_HGSC_ALL_PROT_RNA_microarray_fold10_ite10.Rdata"))

# load testing data
HGSC_rna_EVAL  <- read.csv(paste0(path,"evaluation_data/prospective_ova_rna_seq_sort_common_gene_15632.txt"), row.names= 1, sep="\t", check.names = F )
HGSC_prot_EVAL <- read.csv(paste0(path,"evaluation_data/prospective_ova_proteome_filtered.txt"), row.names= 1, sep="\t", check.names = F )

# take common patients
common_patient <- intersect(colnames(HGSC_prot_EVAL),colnames(HGSC_rna_EVAL))
HGSC_prot_EVAL <- HGSC_prot_EVAL[ ,common_patient] ; HGSC_rna_EVAL <- HGSC_rna_EVAL[ ,common_patient]

# take common proteins and common predictors
common_protein <- intersect(rownames(weight), rownames(HGSC_prot_EVAL))
weight <- weight[common_protein, ]
HGSC_prot_EVAL <- HGSC_prot_EVAL[ common_protein , ]

common_feature <- intersect(colnames(weight), rownames(HGSC_rna_EVAL))
weight <- weight[ , common_feature]
HGSC_rna_EVAL <- HGSC_rna_EVAL[ common_feature , ]

# matrix multiplication to make the prediction
weight <- as.matrix(weight) ; HGSC_rna_EVAL <- as.matrix(HGSC_rna_EVAL)
prediction_ovarian <- weight %*% HGSC_rna_EVAL

prediction_ovarian[which(rowSums(prediction_ovarian)==0), 1] <- 0.1
prediction_ovarian <- cbind(rownames(prediction_ovarian),prediction_ovarian)
colnames(prediction_ovarian)[1] <- "proteinID"

# save the prediction matrix
write.table(prediction_ovarian, file = paste0(path,"output/predictions.tsv"), sep="\t" )

# save the confidence matrix 
write.table(prediction_ovarian, file = paste0(path,"output/confidence.tsv"), sep="\t" )
