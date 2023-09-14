#!/bin/bash
set -e
find . -name "*.json" | ack -x -i "]},]"
find . -name "*.json" -exec sed -i "s/]},]/]}]/g" {} \;

