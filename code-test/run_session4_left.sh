#!/bin/bash
set -e

rm -f ../results/resultsCache_session4_left_median.pkl
rm -f ../results/resultsCache_session4_left_full.pkl
#python eval_session4_left.py -m full
python eval_session4_left.py
