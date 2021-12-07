# README - Data-charts

## Overview

This worked example is designed to show how an R script can be wrapped up as a docker container. To see a workflow diagram of the steps taken below go to [Containerising a script as a federated compute task](https://github.com/federated-data-sharing/common-api/blob/master/doc/User_Guide_Containerising_Tasks.md#containerising-a-script-as-a-federated-compute-task).


To build up an understanding of how to run the scripts, the same task can be run locally, then via local Docker.

The script itself [data-charts.R](./data-charts.R) finds any CSV files in the input folder, reads them in via `readr`, identifies numerical fields and plots histograms of each one.

## Pre-requisites

- R 3.6.1 or greater should be installed locally for the example to be run locally. Depending on the operating system (Mac, Windows, Ubuntu, etc) you are using sreach for the relevent installation steps. 
- ``Rscript`` which is a R interpreter used to execute R commands saved in a file with extesion ".R" will be needed locally. 
- The base Docker image will include a suitable version of R.


## Step 1: Run script locally on command line

- Copy the repository on to your local machine. 

- Create an `input` and an `output` folder here. Put one or more CSV files in the `input` folder under the directory ```.../src/data-charts```.

![image](https://user-images.githubusercontent.com/91956839/144869174-6c533f6f-8772-4174-ab3a-8bbfb3279132.png)

- Put one or more CSV files in the `input` folder.

- Run the script directly, on the command line:
```sh
rm output/*

export CA_INPUT_FOLDER=./input
export CA_OUTPUT_FOLDER=./output

Rscript data-charts.R
```
Look at the output files to see the charts produced.

## Step 2: Run containerised script via docker commandline 

- Build the docker image

```sh
docker build . -t data-charts
```

> Depending on your docker set up you may need to run this command prefixed by `sudo`

- Then run the container on the same local file:
```sh
rm output/*

docker run -it\
     --mount type=bind,source="`realpath $(pwd)/input`",target=/mnt/input\
     --mount type=bind,source="`realpath $(pwd)/output`",target=/mnt/output\
     data-charts:latest
```

> These commands are also provided as shell scripts

## Step 3: Run containerised script via federated data sharing task

> TODO

moved this section from overview (didn't want to delete it for now) could be deployed as a federated compute task with some basic characteristics that could be adapted to other use cases:

- use a common base R docker image
- install some dependencies
- use a single R script as the main computation
- configure an environment similar to the remote federated node
