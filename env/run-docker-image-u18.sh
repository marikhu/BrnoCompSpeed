#!/bin/bash
set -e
WORKDIR=/media/almond/works

xhost +

docker run --gpus all -it --rm --privileged --name u18 \
	-v /tmp/.X11-unix:/tmp/.X11-unix \
	-e DISPLAY=$DISPLAY \
	-w /home/deepstream-app \
	-e TZ=Asia/Bangkok \
	-v ${WORKDIR}:/works \
	marikhu/brnocompspeed:u18-py2.7 \
	bash

