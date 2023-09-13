#!/bin/bash
set -e

rm -f ../results/resultsCache_session2_right_median.pkl
python eval_session2_right_oft.py -rc
