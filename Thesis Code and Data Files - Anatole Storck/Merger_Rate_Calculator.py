# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 07:42:06 2021

@author: Anatole Storck
"""

"""
This file calculates the merger rate of our population and aims to normalize it
to the Milky Way. Merger rate goal is 42 Myr^(-1).
"""

import random
import math
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable
import cmocean
import Merger_Calculator as MC
#Plot formating stuff
plt.rcParams['axes.linewidth'] = 2.15
plt.rcParams["font.family"] = 'Courier New'
plt.rcParams.update({'font.size': 16})
cmap = cmocean.cm.solar
newcmap = cmocean.tools.crop_by_percent(cmap, 7, which='max', N=None)
color = newcmap
#Importing the data
NSNS_data = pd.read_csv(r'C:\Users\storc\OneDrive\Thesis Work\Data\nsns.doubleAcc.DAT', sep=' ')
Merger_Time = pd.read_csv(r'C:\Users\storc\OneDrive\Thesis Work\Data\DNSB_Data_Merger_Time.csv')
#Elements in order: a, e, m1, m2, Vx, Vy, Vz
NSNS_full = ([], [], [], [], [], [], [])
for k in range(0, 1):
    for i in range(0, 2857):
        #Exporting the data to lists
        NSNS_full[0].append(NSNS_data.at[i, '#a/Rsun'])
        NSNS_full[1].append(NSNS_data.at[i, 'e'])
        NSNS_full[2].append(NSNS_data.at[i, 'm1/Msun'])
        NSNS_full[3].append(NSNS_data.at[i, 'm2/Msun'])
        NSNS_full[4].append(NSNS_data.at[i, 'vx/kms'])
        NSNS_full[5].append(NSNS_data.at[i, 'vy/kms'])
        NSNS_full[6].append(NSNS_data.at[i, 'vz/kms'])
#Elements in order: a, e, m1, m2, t_birth, t1, t2
NSNS_visible_binary = ([], [], [], [], [], [], [])
#Elements in order: R, Phi, Vx, Vy, Vz
NSNS_visible_galactic = ([], [], [], [], [])
#Elements at present day: a, e, P
NSNS_visible_present = ([], [], [])
"""
Since merger time does not change for different birth times
we can calculate the binary integrator once and apply it to
the rest of the iterations
"""
scale_factor = 266
#counting the amount of visible binaries
count_merge = 0
for j in range(0, 100):
    for k in range(0, scale_factor):
        for i in range(0, 2857):
            #Assigning a birth time (-10e3 to 0e3 Myrs) for each binary
            t_birth = -1*random.random()*(10e3)
            if(-1 < Merger_Time.at[i, 'Merger Time'] + t_birth < 0):
                count_merge += 1
#Seeing if the scale factor yields the desired merger rate
print(count_merge/100)
        











