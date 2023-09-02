#!/bin/bash
set -e

session=$1
python open-pkl-file.py $session > gt-txt-files/$session"_gt_file.txt"
