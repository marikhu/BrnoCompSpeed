#!/bin/bash
set -e

rm -f ../results/resultsCache_session4_center_median.pkl
python eval_session4_center.py
