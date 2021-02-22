rm output/*

docker run -it\
     --mount type=bind,source="`realpath $(pwd)/input`",target=/mnt/input\
     --mount type=bind,source="`realpath $(pwd)/output`",target=/mnt/output\
     rmarkdown-report:latest
