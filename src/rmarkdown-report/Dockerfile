FROM rocker/tidyverse

LABEL MAINTAINER="Common API team <info@fds-api.org>"

# If we were using rocker/r-base we'd have to do this
# RUN R -e "install.packages(c('readr', 'dplyr', 'ggplot2'), dependencies=TRUE, repos='https://cloud.r-project.org/')"

ENV CA_INPUT_FOLDER=/mnt/input/
ENV CA_OUTPUT_FOLDER=/mnt/output

WORKDIR /data

COPY report.Rmd /data
COPY report.R /data

CMD ["Rscript", "/data/report.R"]
