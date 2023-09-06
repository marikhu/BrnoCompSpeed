# -*- coding: utf-8 -*-
import os
import platform
    

"""
Paths to dataset and result dir
"""
if platform.system() == "Windows":        
    TRANS_PATH = lambda p: p
else:
    TRANS_PATH = lambda p: p

DATASET_BASE_PATH = TRANS_PATH("../dataset/")
RESULTS_DIR = TRANS_PATH("../results/")

DATASET_SESSIONS = {
    "session1": {
        "recordings": {        
            "center": {"fps": 50.0}
        }
    }
}





ALL_SESSIONS = set(DATASET_SESSIONS.keys())

ALL_VIDEOS = []
for _sId in sorted(DATASET_SESSIONS):
    for _rId in ("center",):
        ALL_VIDEOS.append((_sId, _rId))

SPLIT_TRAIN_SESSIONS = {}
SPLIT_TRAIN_SESSIONS["A"] = {"session0"}
#SPLIT_TRAIN_SESSIONS["B"] = SPLIT_TRAIN_SESSIONS["A"] | {"session1", "session2"}
#SPLIT_TRAIN_SESSIONS["C"] = SPLIT_TRAIN_SESSIONS["B"] | {"session3"}

SPLIT_TEST_SESSIONS = dict(map(lambda i: (i[0], ALL_SESSIONS-i[1]), SPLIT_TRAIN_SESSIONS.items()))

SPLIT_TRAIN_VIDEOS = dict(map(lambda i: (i[0], filter(lambda j: j[0] in i[1], ALL_VIDEOS)), SPLIT_TRAIN_SESSIONS.items()))
SPLIT_TEST_VIDEOS = dict(map(lambda i: (i[0], filter(lambda j: j[0] in i[1], ALL_VIDEOS)), SPLIT_TEST_SESSIONS.items()))

def getPathForRecording(session, recording):
    return os.path.join(DATASET_BASE_PATH, "%s_%s"%(session, recording))
