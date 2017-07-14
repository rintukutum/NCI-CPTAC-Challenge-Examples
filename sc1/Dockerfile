FROM ubuntu

## Installing dependencies

RUN apt-get update
RUN apt-get -y install r-base
RUN apt-get -y install aptitude libcurl4-openssl-dev  libxml2-dev libxml2-dev
RUN echo "r <- getOption('repos'); r['CRAN'] <- 'http://cran.us.r-project.org'; options(repos = r);" > ~/.Rprofile
RUN Rscript -e "install.packages('pamr')"


## Make sure all files that your execution scripts need are in the Docker image

COPY DRY_RUN_01_prot_prediction.R /DRY_RUN_01_prot_prediction.R
COPY score_sc1.sh /score_sc1.sh
COPY imputation_function.R /imputation_function.R