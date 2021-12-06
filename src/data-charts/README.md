# README - Data-charts

## Overview

This worked example is designed to show how an R script can be dockerised and could be deployed as a federated compute task with some basic characteristics that could be adapted to other use cases:

- use a common base R docker image
- install some dependencies
- use a single R script as the main computation
- configure an environment similar to the remote federated node

To build up an understanding of how to run the scripts, the same task can be run locally, then via local Docker.

The script itself finds any CSV files in the input folder, reads them in via `readr`, identifies numerical fields and plots histograms of each one.

## Pre-requisites

R 3.6.1 or greater should be installed locally for the example to be run locally. The base Docker image will include a suitable version of R.

## Step-by-step

Create an `input` and an `output` folder here. Put one or more CSV files in the `input` folder.

Run the script directly, on the command line:
```sh
rm output/*

export CA_INPUT_FOLDER=./input
export CA_OUTPUT_FOLDER=./output

Rscript data-charts.R
```
Look at the output files to see the charts produced.

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
     data-charts:latest
```

> These commands are also provided as shell scripts

Running this as as a federated data sharing task

> TODO
