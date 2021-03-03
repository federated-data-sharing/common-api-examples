FROM rocker/tidyverse

LABEL MAINTAINER="Common API team <info@fds-api.org>"

# If we were using rocker/r-base we'd have to do this
# RUN R -e "install.packages(c('readr', 'dplyr', 'ggplot2'), dependencies=TRUE, repos='https://cloud.r-project.org/')"

ENV CA_INPUT_FOLDER=/mnt/input/
ENV CA_OUTPUT_FOLDER=/mnt/output

WORKDIR /data

# This creates the R markdown output
COPY generate-report.R /data
# This is likely to change most often:
COPY report.Rmd /data

CMD ["Rscript", "/data/generate-report.R"]
