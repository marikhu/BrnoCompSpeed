# python open-pkl-file.py > session4_left_gt_data.txt

import pickle

with open('session4_left/gt_data.pkl', 'rb') as f:
    data = pickle.load(f)
    print (data)
