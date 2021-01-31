FROM rocker/tidyverse

LABEL MAINTAINER="Common API team <info@fds-api.org>"

ENV CA_INPUT_FOLDER=/mnt/input/
ENV CA_OUTPUT_FOLDER=/mnt/output

WORKDIR /data

COPY data-charts.R /data

CMD ["Rscript", "/data/data-charts.R"]
