#!/bin/bash
set -e

rm -f ../results/resultsCache_session6_right_median.pkl
python eval_session6_right.py
