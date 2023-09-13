#!/bin/bash
set -e

rm -f ../results/resultsCache_session3_left_median.pkl
python eval_session3_left_oft.py -rc
