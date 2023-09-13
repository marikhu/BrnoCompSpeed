#!/bin/bash
set -e

rm -f ../results/resultsCache_session3_right_median.pkl
python eval_session3_right_oft.py -rc
