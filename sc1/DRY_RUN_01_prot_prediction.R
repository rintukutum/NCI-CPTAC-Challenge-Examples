path = '/'
# load imputation algorithm
source(paste0(path,"imputation_function.R"));

for(m in 1:100)
{
  # load testing data
  data.obs = read.table(paste0(path,"evaluation_data/data_test_obs_",m,'.txt'),row.names= 1, sep="\t");
  # impute testing data
  data.impu = my.imputation(data.obs);
  # output imputation result
  write.table(data.impu, file=paste0(path,"output/data.impute.",m,'.txt'),header=T,sep='\t',row.names = 1);    
}
