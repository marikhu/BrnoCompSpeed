#!/bin/bash
set -e

rm -f ../results/resultsCache_session1_center_median.pkl
python eval_session1_center.py
