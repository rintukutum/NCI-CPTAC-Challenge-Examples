FROM ubuntu

## Installing dependencies

RUN apt-get update
RUN apt-get -y install python
RUN apt-get -y install aptitude libcurl4-openssl-dev  libxml2-dev libxml2-dev
RUN apt-get -y install python-pip python-pandas python-scipy python-numpy
RUN pip install --upgrade pip
RUN pip install xgboost
RUN pip install sklearn

## Make sure all files that your execution scripts need are in the Docker image

COPY DRY_RUN_02_example.py /DRY_RUN_02_example.py
COPY score_sc2.sh /score_sc2.sh