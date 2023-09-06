#!/bin/bash
set -e

rm -f ../results/resultsCache_session4_right_median.pkl
python eval_session4_right.py
