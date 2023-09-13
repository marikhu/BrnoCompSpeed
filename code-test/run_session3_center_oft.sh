#!/bin/bash
set -e

rm -f ../results/resultsCache_session3_center_median.pkl
python eval_session3_center_oft.py -rc
