#!/bin/bash
set -e

rm -f ../results/resultsCache_session5_left_median.pkl
python eval_session5_left.py -rc
