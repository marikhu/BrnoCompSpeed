#!/bin/bash
set -e

rm -f ../results/resultsCache_session5_right_median.pkl
python eval_session5_right.py -rc
