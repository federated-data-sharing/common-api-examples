# README - data-profiler

## Overview

This is a simple worked example of a summarisation task that can be wrapped up as a docker container. It is intended to work on any tabular data it finds in the input folder specified. This means it can be used for data explorations: it makes few assumptions on the source data other than it being valid CSV.

The script itself [data-profiler.py](./data-profiler.py) used the [pandas](https://pandas.pydata.org/) library to create a brief statistical profile of each field in the source data and write these to an output file.

## Step-by-step

Create an `input` and an `output` folder here. Put one or more CSV files in the `input` folder.

Run the script directly, on the command line:
```sh
rm output/*

export CA_INPUT_FOLDER=./input
export CA_OUTPUT_FOLDER=./output

python data-profiler.py
```
Look at the output files to see the statistical summaries.

Then, build the docker image
```sh
docker build . -t data-profiler
```

> Depending on your docker set up you may need to run this command prefixed by `sudo`

Then run the container on the same local file:
```sh
rm output/*

docker run -it\
     --mount type=bind,source="`realpath $(pwd)/input`",target=/mnt/input\
     --mount type=bind,source="`realpath $(pwd)/output`",target=/mnt/output\
     data-profiler:latest
```

> These commands are also provided as shell scripts

Running this as as a federated data sharing task

> TODO


