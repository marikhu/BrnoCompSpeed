#!/bin/bash
set -e

rm -f ../results/resultsCache_session2_center_median.pkl
python eval_session2_center.py
