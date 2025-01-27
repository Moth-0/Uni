## Illustration of reading a *.txt file from picoscope ######################## 
#  
#  The example shows a way to reada file that was saved in *.txt format 
#  on pico-scope: 
#  the special structure of the data file from pico scope is decomposed with 
#  functions that manipulates text-strings and convert strings to numbers
#
#  See also Illustration_of_reading_a_matfile_from_picoscope.py 
#  the script is a little simple if you chose to save in *.mat format 
#
#   The data is delivered as nympy arrays 
#   1) t_A, V_A for channel A 
#   2) t_B, V_B for channel B
#
#                                                               HBP - nov. 2019
###############################################################################
# %% imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sc
import scipy.io
#import re

#Settings
plt.rc("axes", labelsize=18, titlesize=22)   # skriftstørrelse af `xlabel`, `ylabel` og `title`
plt.rc("xtick", labelsize=16, top=True, direction="in")  # skriftstørrelse af ticks, vis også ticks øverst og vend ticks indad
plt.rc("ytick", labelsize=16, right=True, direction="in") # samme som ovenstående
plt.rc("legend", fontsize=16) # skriftstørrelse af figurers legends 

# %% loading file and making the arrays of correct shape

# %& select a file 
#filename = 'Channel_A_only.txt'
filename = 'Channel_B_only.txt'
#filename = 'Channel_A_and_B.txt'


# %% open and read

# open and read the file as text
fid =open(filename,'r')
all_data=fid.read()
fid.close()

# identify indices of the channels
idx_A=all_data.find('Channel A')
idx_B=all_data.find('Channel B')

# if both channel A and B are present
if (idx_A>-1) & (idx_B>-1):
    print('got  both A and B data ')
    channel_A_str = all_data[:idx_B-1]                                  # excluses the last \n
    channel_B_str = all_data[idx_B-1:]
    
    idx_A_data = channel_A_str.find('(mV)\n')
    A_data    =  channel_A_str[idx_A_data+5:len(channel_A_str)-1]       # excludes \n
    
    idx_B_data = channel_B_str.find('(mV)\n')
    B_data    =  channel_B_str[idx_A_data+5:len(channel_B_str)-1]
    
    A=str.split(A_data, sep='\n')     # list with strings from channel A 
    la = len(A)                       # length of list   
    t_A = np.zeros(la)                # empty array for time data  
    V_A = np.zeros(la)                # empty array for voltage data  
    for ii in range(0,la,1):          # split the list in times and values
        a=str.split(A[ii],'\t')
        t_A[ii] =float(a[0])
        V_A[ii] =float(a[1])
    
    B=str.split(B_data, sep='\n')      # list with strings from channel A
    lb = len(B)                        # length of list 
    t_B = np.zeros(lb)                 # empty array for time data
    V_B = np.zeros(lb)                 # empty array for voltage data
    for ii in range(0,lb,1):           # split the list in times and values
        b=str.split(B[ii],'\t')
        t_B[ii] =float(b[0])
        V_B[ii] =float(b[1])


# if only channel A is present
if (idx_A>-1) & (idx_B==-1):
    print('got A data only')
    channel_A_str = all_data                                  # excluses the last \n
    
    idx_A_data = channel_A_str.find('(mV)\n')
    A_data    =  channel_A_str[idx_A_data+5:len(channel_A_str)-1]       # excludes \n
    
    
    A=str.split(A_data, sep='\n')     # list with strings from channel A 
    la = len(A)                       # length of list   
    t_A = np.zeros(la)                # empty array for time data  
    V_A = np.zeros(la)                # empty array for voltage data  
    for ii in range(0,la,1):          # split the list in times and values
        a=str.split(A[ii],'\t')
        t_A[ii] =float(a[0])
        V_A[ii] =float(a[1])
    


# if only channel B is present
if (idx_A==-1) & (idx_B>-1):
    print('got B data only')
    channel_B_str = all_data                                  # excluses the last \n
    
    idx_B_data = channel_B_str.find('(mV)\n')
    B_data    =  channel_B_str[idx_B_data+5:len(channel_B_str)-1]       # excludes \n
    
    
    B=str.split(B_data, sep='\n')     # list with strings from channel A 
    lb = len(B)                       # length of list   
    t_B = np.zeros(lb)                # empty array for time data  
    V_B = np.zeros(lb)                # empty array for voltage data  
    for ii in range(0,lb,1):          # split the list in times and values
        b=str.split(B[ii],'\t')
        t_B[ii] =float(b[0])
        V_B[ii] =float(b[1])
    





# %% Plotting to test the read
        
# make figure 
fig = plt.figure(1)                            # makes a figure; fig is a handle to the figure
fig.clf()                                      # clear the figure
fig.set_size_inches(6,5,forward=True)          # sets the image size (w,h) in inches (1inch = 2.54 cm)
plt.rc('xtick',labelsize=14)                   # rc ~ "Run and Configure" # set size of axis-numbers#
plt.rc('ytick',labelsize=14)                   # set the size of the axis-numbers
   
# make an axis and plot data   
ax = fig.add_subplot(1,1,1)                                # makes a subplot; ax is the handle to the axes #


if (idx_A>-1) & (idx_B>-1):                                                           # NB use \ to continue command on the next line#
    h1 = ax.plot(t_A,  V_A,label='channel A',\
             color ='b',marker=None,\
             markersize=10, linewidth=2)                   # simple plotting #h1 is handle to this plot
    h1 = ax.plot(t_B,  V_B,label='channel B',\
             color ='r',marker=None,\
             markersize=10, linewidth=2)                   # simple plotting #h1 is handle to this plot



if (idx_A>-1) & (idx_B==-1):                                                           # NB use \ to continue command on the next line#
    h1 = ax.plot(t_A,  V_A,label='channel A',\
             color ='b',marker=None,\
             markersize=10, linewidth=2)                   # simple plotting #h1 is handle to this plot
          

if (idx_A==-1) & (idx_B>-1):                                                           # NB use \ to continue command on the next line#
    h1 = ax.plot(t_B,  V_B,label='channel B',\
             color ='r',marker=None,\
             markersize=10, linewidth=2)                   # simple plotting #h1 is handle to this plot
          

ax.set_title('Data fra picoscop',fontsize=20)  # set a title

ax.set_xlabel(r'Time $t$ [ns]',fontsize=14)                  # set the label on the x-axis
ax.set_ylabel(r'Voltage [mV]',fontsize=14)       # set the label on the y-axis
ax.legend(loc='upper left')   
