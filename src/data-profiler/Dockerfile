FROM continuumio/anaconda3

LABEL MAINTAINER="Common API team <info@fds-api.org>"

ENV CA_INPUT_FOLDER=/mnt/input/
ENV CA_OUTPUT_FOLDER=/mnt/output

WORKDIR /data

COPY data-profiler.py /data

CMD ["python", "/data/data-profiler.py"]
