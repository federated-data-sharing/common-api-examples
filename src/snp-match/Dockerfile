FROM continuumio/anaconda3

LABEL MAINTAINER="Common API team <info@fds-api.org>"

ENV CA_INPUT_FOLDER=/mnt/input/
ENV CA_OUTPUT_FOLDER=/mnt/output

WORKDIR /app

COPY snp-match.py /app
COPY top_mutations.csv /app

CMD ["python", "/app/snp-match.py"]
