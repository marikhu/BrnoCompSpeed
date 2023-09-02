# python open-pkl-file.py > session4_left_gt_data.txt

import pickle
import sys

args = sys.argv
#print 'Number of arguments:', len(args), 'arguments.'
#print 'Argument List:', str(args)

gt_file=args[1] + '/gt_data.pkl'
with open(gt_file, 'rb') as f:
    data = pickle.load(f)
    print (data)
