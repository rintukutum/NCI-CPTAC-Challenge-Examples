path <- "/"

# load saved models
load(paste0(path,"model_storage/SAVE_WEIGHT_HGSC_PROT_RNA_fold10_20ite.Rdata"))

# load testing data
HGSC_rna_EVAL  <- read.csv(paste0(path,"evaluation_data/pros_ova_rna_seq_sort_common_gene_15632") , row.names= 1)
HGSC_prot_EVAL <- read.csv(paste0(path,"evaluation_data/pros_ova_proteome_sort_common_gene_6577"), row.names= 1)

# take common proteins and common predictors
common_protein <- intersect(rownames(weight), colnames(HGSC_prot_EVAL))
weight <- weight[common_protein, ]
HGSC_prot_EVAL <- HGSC_prot_EVAL[ ,common_protein]

common_feature <- intersect(colnames(weight), colnames(HGSC_rna_EVAL))
weight <- weight[ , common_feature]
HGSC_rna_EVAL <- HGSC_rna_EVAL[ ,common_feature]

# matrix multiplication to make the prediction
weight <- as.matrix(weight) ; HGSC_rna_EVAL <- as.matrix(HGSC_rna_EVAL)
prediction_ovarian <- HGSC_rna_EVAL %*% t(weight)

# save the prediction matrix
write.csv(prediction_ovarian, paste0(path,"output/predictions.tsv")  ) 

