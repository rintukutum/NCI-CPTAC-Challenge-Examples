FROM ubuntu

## Installing dependencies

RUN apt-get update
RUN apt-get -y install python
RUN apt-get -y install r-base
RUN apt-get -y install aptitude libcurl4-openssl-dev  libxml2-dev libxml2-dev

RUN python -e ‘pip install os’
RUN python -e ‘pip install scipy’
RUN python -e ‘pip install xgboost’
RUN python -e ‘pip install sklearn’
RUN python -e ‘pip install pandas’
RUN python -e ‘pip install numpy’
RUN python -e ‘pip install random’

## Make sure all files that your execution scripts need are in the Docker image

COPY DRY_RUN_02_prot_example.py /DRY_RUN_02_example.py
