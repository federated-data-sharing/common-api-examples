rm -r ../../output/*

docker run -it\
     --mount type=bind,source="`realpath $(pwd)/../../input`",target=/mnt/input\
     --mount type=bind,source="`realpath $(pwd)/../../output`",target=/mnt/output\
     data-profiler:latest
