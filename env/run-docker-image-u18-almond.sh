#!/bin/bash
set -e
USER=`whoami`
echo $USER
WORKDIR=/media/almond/works

xhost +

docker run --gpus all -it --rm --privileged --name python-2.7-u18 \
	-v /tmp/.X11-unix:/tmp/.X11-unix \
	-e DISPLAY=$DISPLAY \
	-e TZ=Asia/Bangkok \
	-v ${WORKDIR}:/works \
	-w /works/GitHub/BrnoCompSpeed \
	-e TZ=Asia/Bangkok \
	marikhu/brnocompspeed:u18-py2.7 \
	bash

