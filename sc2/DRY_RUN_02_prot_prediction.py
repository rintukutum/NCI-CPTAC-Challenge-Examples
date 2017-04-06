#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 20:48:38 2017
@author: miyang
"""

import os
from scipy import stats
import xgboost as xgb
from xgboost.sklearn import XGBClassifier
from sklearn import cross_validation
import pandas as pd
import numpy as np
import os.path
import random
path = "/"


## loading data
name_of_response = 'HGSC_prot'  
name_of_features = 'HGSC_rna'  

## loading data
RES = pd.read_csv(path + name_of_response, index_col = 0) ;  RES = RES.transpose()
features = pd.read_csv(path + name_of_features, index_col = 0) 

nfolds = 10
 
    
num_round = 10
result_prediction = []
for i in range (0, 5):
    for t in range (0, 5 ):  ## len(RES.iloc[0,:])
     
        pp_by_protein = []
        kf = cross_validation.KFold(len(RES.iloc[:,1]), n_folds = nfolds, shuffle = True,random_state = random.randint(1, 1000) )
       
        for train_index, test_index in kf:
            
            features_train, features_test = features.iloc[ train_index  , : ], features.iloc[ test_index , : ]
            RES_train, RES_test = RES.iloc[ train_index, t ] , RES.iloc[ test_index, t ]
            
            ii = np.flatnonzero(np.isfinite( RES_train ))
            features_train = features_train.iloc[ii, :] ;  RES_train = RES_train[ii] 
            xgtrain = xgb.DMatrix( features_train , label= RES_train )
           
            ii = np.flatnonzero(np.isfinite( RES_test ))
            features_test = features_test.iloc[ii, :] ;  RES_test = RES_test[ii] 
            xgbtest = xgb.DMatrix( features_test , label= RES_test )
    
            xgb1 = XGBClassifier(
                 learning_rate =0.3,
                 n_estimators=30,
                 max_depth=4,
                 min_child_weight=1,
                 gamma=0,
                 subsample=0.8,
                 colsample_bytree=0.8,
                 objective= 'reg:linear',
                 scale_pos_weight=1,
                 seed = random.randint(1, 1000) )
            
            xgb_params = xgb1.get_xgb_params()
            xgbooster = xgb.Booster()
              
            bst = xgb.train(xgb_params, xgtrain , num_round)
            pred = bst.predict(xgbtest)
                    
            ### compute pearson correlation by protein ###
            pcorr = stats.pearsonr( RES_test  , pred ) [0]
            pp_by_protein.append(pcorr)
                                   
        result_prediction.append(np.mean(pp_by_protein))
##  np.mean(result_prediction)


result_prediction= pd.DataFrame(result_prediction)
#result_prediction.to_csv(path + 'prediction_result_' + str(random.randint(1, 1000)))
result_prediction.to_csv(path + 'output/prediction.csv') 

                
                         
#######################################################  AVERAGING RESULT FROM MULTIPLE RUNS #######################################################

# prefixed = [filename for filename in os.listdir(path) if filename.startswith('prediction_result')]

# iteration=3
# if len(prefixed) >= iteration:
    
#     prefixed = [filename for filename in os.listdir(path) if filename.startswith('prediction_result')]
#     frame = pd.DataFrame()
#     list = []
#     for file_ in prefixed:
#         df = pd.read_csv(path + file_,index_col=None, header=0)
#         list.append(df)
#     mean = pd.concat([each.stack() for each in list],axis=1).apply(lambda x:x.mean(),axis=1).unstack() ; mean = mean.iloc[ : , 1 ]
#     mean.to_csv(path + '/prediction_result'+'_'+str(iteration)+'ite')



