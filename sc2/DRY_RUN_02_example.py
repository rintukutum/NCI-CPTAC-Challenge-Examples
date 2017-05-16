#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 14:10:26 2017
@author: miyang
"""
import xgboost as xgb
from xgboost.sklearn import XGBClassifier
from sklearn import cross_validation
import pandas as pd
import numpy as np
import os
import random
path = "/"

## loading data
name_of_response = 'HGSC_prot'  
name_of_features = 'HGSC_rna'  
## loading data
RES = pd.read_csv(path + '/training_data/' + name_of_response, index_col = 0)
features = pd.read_csv(path + '/training_data/' + name_of_features, index_col = 0) 
## load evaluation data
features_EVAL = pd.read_csv(path + '/evaluation_data/HGSC_rna_EVAL', index_col = 0) 
## choose a subset of 5 proteins
RES = RES.iloc[:,0:5] 

nfolds = 10    
num_round = 10
prediction_result = []  ## store result of each run, for all proteins

for t in range (0, len(RES.iloc[0,:]) ):  
 
    kf = cross_validation.KFold(len(RES.iloc[:,1]), n_folds = nfolds, shuffle = True,random_state = random.randint(1, 1000) )
    
    prediction_for_1 = [] ## prediction for 1 protein over k fold cross validation
    
    for train_index, test_index in kf:
        
        features_train, features_test = features.iloc[ train_index  , : ], features.iloc[ test_index , : ]
        RES_train, RES_test = RES.iloc[ train_index, t ] , RES.iloc[ test_index, t ]
        
        remove_NA = np.flatnonzero(np.isfinite( RES_train ))
        features_train = features_train.iloc[remove_NA, :] ;  RES_train = RES_train[remove_NA] 
        xgtrain = xgb.DMatrix( features_train , label= RES_train )
       
        features_EVAL_xgb = xgb.DMatrix(features_EVAL)

        xgb1 = XGBClassifier(
             learning_rate =0.3,
             n_estimators=30,
             max_depth=3,
             min_child_weight=3,
             gamma=0,
             subsample=0.8,
             colsample_bytree=0.8,
             objective= 'reg:linear',
             scale_pos_weight=1,
             seed = random.randint(1, 1000) )
        
        xgb_params = xgb1.get_xgb_params()
                 
        model = xgb.train(xgb_params, xgtrain , num_round)                     
        pred = model.predict(features_EVAL_xgb)
        prediction_for_1.append(pred)
        
    prediction_for_1 = pd.DataFrame(prediction_for_1)
    prediction_for_1 = prediction_for_1.mean(axis=0)  ## average over k fold
    
    prediction_result.append(prediction_for_1)
               
############################## save result ##############################
prediction_result = pd.DataFrame(prediction_result)  
prediction_result.to_csv(path + 'output/prediction.csv')






