# README - data-profiler

## Overview

This is a simple worked example of a summarisation task that can be wrapped up as a docker container. To see a workflow diagram of the steps taken below go to [Containerising a script as a federated compute task](https://github.com/federated-data-sharing/common-api/blob/master/doc/User_Guide_Containerising_Tasks.md#containerising-a-script-as-a-federated-compute-task).

This example is intended to work on any tabular data it finds in the input folder specified. This means it can be used for data explorations: it makes few assumptions on the source data other than it being valid CSV. 

The script itself [data-profiler.py](./data-profiler.py) uses the [pandas](https://pandas.pydata.org/) library to create a brief statistical profile of each field in the source data and write these to an output file.

## Step 1: Run script locally on command line

- Copy the repository on to your local machine. 

- Create an `input` and an `output` folder under the directory ```.../src/data-profiler```. 

![image](https://user-images.githubusercontent.com/91956839/140361598-e4eb71b2-f058-457c-9066-93022acb5e48.png)

- Put one or more CSV files in the `input` folder.

- Run the script directly, on the command line:
```sh
rm output/*

export CA_INPUT_FOLDER=./input
export CA_OUTPUT_FOLDER=./output

python data-profiler.py
```
Look at the output files to see the statistical summaries.

## Step 2: Run containerised script via docker commandline 

- Build the docker image

```sh
docker build . -t data-profiler
```

> Depending on your docker set up you may need to run this command prefixed by `sudo`

- Then run the container on the same local file:
```sh
rm output/*

docker run -it\
     --mount type=bind,source="`realpath $(pwd)/input`",target=/mnt/input\
     --mount type=bind,source="`realpath $(pwd)/output`",target=/mnt/output\
     data-profiler:latest
```
Look at the output files to see the statistical summaries.

> These commands are also provided as shell scripts

## Step 3: Run containerised script via federated data sharing task

> TODO
