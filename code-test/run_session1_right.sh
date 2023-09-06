#!/bin/bash
set -e

rm -f ../results/resultsCache_session1_right_median.pkl
python eval_session1_right.py
