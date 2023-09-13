#!/bin/bash
set -e

rm -f ../results/resultsCache_session6_center_median.pkl
python eval_session6_center_oft.py -rc
