#!/bin/bash
set -e

rm -f ../results/resultsCache_session3_right_median.pkl
python eval_session3_right.py -rc
