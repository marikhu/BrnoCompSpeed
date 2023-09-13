#!/bin/bash
set -e

rm -f ../results/resultsCache_session5_center_median.pkl
python eval_session5_center_oft.py -rc
