import pickle
pickleFile = open("gt_data.pkl","rb")
gt_data = pickle.load(pickleFile)
print(gt_data)
