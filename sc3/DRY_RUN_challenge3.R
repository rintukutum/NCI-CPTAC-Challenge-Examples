# -- Dry Run SubChallenge 3

library(randomForest)

## loading data
name_of_response = 'HGSC_pho'  
name_of_features = 'HGSC_prot'  

## loading data
RES = read.table(paste(path,'/training_data/',name_of_response,sep=""), sep=",",header=TRUE)
features = read.table(paste(path,'/training_data/',name_of_features,sep=""), sep=",",header=TRUE) 

## choose a subset of 5 phosphosite
RES = RES[,seq(1,5)] 

prediction_result = list()  ## store result of each run, for all proteins
out<-list()

for (j in 1:dim(RES)[2]) out[[j]]<-randomForest(x=t(features),y=RES[,j],nTree=1000)


# --- prediction step example
j=1
features.test<-features[seq(1,10),]
predict(out[[j]], t(features.test), type="response")$test$predicted

############################## save result ##############################
save(out,path + 'output/Challente3_prediction.rda')








