"""
Copyright (c) 2018 Grumpy Cat Software S.L.

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""
########################################################################################################################
# IMPORT
########################################################################################################################
from scipy.io import loadmat
import os
import time
import tsa.tsa_datasets as a
from tsa.grumpy import grumpyAnaliser
import pandas as pd
########################################################################################################################

#data preprocessing
data = loadmat(os.path.join(a.__path__[0], 'sel102m.mat'))
ta=data["val"][0]
print(ta)
print(len(ta))


analiser_cat = grumpyAnaliser()
for i in range(10):
    print("-----")
    print("stomp")
    print("-----")
    start = time.time()
    #data analysis
    mp = analiser_cat.stomp(ta[0:13000],ta[0:13000],256)
    print(str(time.time() -start))
