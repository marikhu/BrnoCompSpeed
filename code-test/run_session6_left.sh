#!/bin/bash
set -e

rm -f ../results/resultsCache_session6_left_median.pkl
python eval_session6_left.py
