path = '/'
# load imputation algorithm
source(paste0(path,"imputation_function.R"));

for(m in 1:1)
{
  # load testing data
  data.obs = read.csv(paste0(path,"evaluation_data/data_test_obs_",m,'.txt'),row.names= 1, sep="\t")
  # impute testing data
  data.impu = as.data.frame(my.imputation(data.obs))
  prediction <- cbind(proteinID = rownames(data.impu),data.impu)
  # output imputation result
  write.table(prediction, file=paste0(path,"output/predictions_",m,'.txt'),sep='\t',row.names = F,quote=F) 
  write.table(prediction, file=paste0(path,"output/confidence_",m,'.txt'),sep='\t',row.names = F,quote=F) 
}

