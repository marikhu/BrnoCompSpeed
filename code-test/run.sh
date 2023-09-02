#!/bin/bash
set -e

rm -f ../results/resultsCache_median.pkl
python eval.py
