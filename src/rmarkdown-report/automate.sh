#!/bin/bash

SECONDS=0

if [ $# -eq 0 ]; then
	echo "Usage: $0 <taskfile.json>"
	exit 1
fi

# If 2nd argument is 'true' then print JSON responses
VERBOSE=${2:false}

# Check that the task file is available
_taskfile=$1
if [[ ! -f "$_taskfile" ]]; then
    echo "Task file missing: $_taskfile"
    exit 1
fi

# Check the necessary environment variables are set
if [ -z "$FDS_API_ENDPOINT" ]; then
    echo "Missing environment variable: FDS_API_ENDPOINT"
    exit 1
fi
if [ -z "$FDS_API_TOKEN" ]; then
    echo "Missing environment variable: FDS_API_ENDPOINT"
    exit 1
fi

# For info only
_container=`cat $_taskfile | jq -r '.task.container.name'`
_container_tag=`cat $_taskfile | jq -r '.task.container.tag'`
_container_registry=`cat $_taskfile | jq -r '.task.container.registry'`
_query=`cat $_taskfile | jq '.task.queryInput.selectionQuery'`

echo "$(date +%Y%m%d-%H%M%S) - File: $_taskfile"
echo "$(date +%Y%m%d-%H%M%S) - Container: $_container_registry/$_container:$_container_tag"
echo "$(date +%Y%m%d-%H%M%S) - Query: $_query"

# 1. Build the docker container
# echo "$(date +%Y%m%d-%H%M%S) - Building container"
# docker build . -t $_container

# 2. Push the container to the registry
# echo "$(date +%Y%m%d-%H%M%S) - Push container to the registry"
# sudo docker tag $_container "$_container_registry/$_container:$_container_tag"
# sudo docker push "$_container_registry/$_container:latest"

# Post the task, check the status
_response=`curl -s -H "Authorization: Bearer $FDS_API_TOKEN" -H "Content-Type: application/json" -X POST -d @"$_taskfile" "$FDS_API_ENDPOINT/tasks"`
if [ $VERBOSE ]; then
    echo $_response | jq '.'
fi

_taskid=`echo $_response | jq -r '.data.id'`
_taskstatus=`echo $_response | jq -r '.data.status'`

echo "$(date +%Y%m%d-%H%M%S) - $_taskid: $_taskstatus"

# If still running, wait 2 seconds, then try again, loop if necessary
while [[ $_taskstatus == "Running" ]]; do
	echo "$(date +%Y%m%d-%H%M%S) - sleep"
	sleep 5

    # Get task status
	_response=`curl -s -H "Authorization: Bearer $FDS_API_TOKEN" "$FDS_API_ENDPOINT/tasks/$_taskid"`
	if [ $VERBOSE ]; then
        echo $_response | jq '.'
    fi
	_taskstatus=`echo $_response | jq -r '.status'`

	echo "$(date +%Y%m%d-%H%M%S) - $_taskid: $_taskstatus"
done

if [[ $_taskstatus == "complete" ]]; then 
    _output_file="./output/$_taskid.zip"

    echo "$(date +%Y%m%d-%H%M%S) - $_taskid: Fetching result into $_output_file"

    curl -s --output "$_output_file"  -H "Authorization: Bearer $FDS_API_TOKEN" -H "Accept: application/gzip"   "$FDS_API_ENDPOINT/tasks/$_taskid/result"

    echo "$(date +%Y%m%d-%H%M%S) - $_taskid: Output zipfile contents:"
    unzip -l "$_output_file"

    output_extract_folder="./output/$_taskid"
    mkdir -p "$output_extract_folder"
    cd "$output_extract_folder"
    unzip "../$_taskid.zip"
    cd ../..
    echo "$(date +%Y%m%d-%H%M%S) - $_taskid: Output zipfile extracted to: $output_extract_folder"

else
    echo "$(date +%Y%m%d-%H%M%S) - $_taskid: Task did not complete: $_taskstatus"
fi

duration=$SECONDS
echo "$(date +%Y%m%d-%H%M%S) - $_taskid: Duration $(($duration / 60))m $(($duration % 60))s"
