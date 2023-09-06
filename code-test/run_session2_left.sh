#!/bin/bash
set -e

rm -f ../results/resultsCache_session2_left_median.pkl
python eval_session2_left.py
