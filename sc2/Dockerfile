FROM ubuntu

## Installing dependencies

RUN apt-get update
RUN apt-get -y install r-base
RUN apt-get -y install aptitude libcurl4-openssl-dev  libxml2-dev libxml2-dev


## Make sure all files that your execution scripts need are in the Docker image

COPY DRY_RUN_02_prot_prediction.R /DRY_RUN_02_prot_prediction.R
COPY score_sc2.sh /score_sc2.sh
COPY model_storage /model_storage