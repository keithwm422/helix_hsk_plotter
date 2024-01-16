#!/usr/bin/python

import time
import pprint
import pandas as pd
import numpy as np
from numpy.polynomial.polynomial import polyfit
import matplotlib.pyplot as plt
import os
from pip import main

print(os.getcwd())
print(os.path.dirname(__file__))
data_path=os.path.dirname(__file__)
#file_name="testing_cleanup.csv"
file_name="hv_data_spare_tom_dcthsk.csv"
name_to_read=os.path.join(data_path,file_name)

temp_df=pd.read_csv(name_to_read)

print(temp_df.head())
#fit a line...

b, m = polyfit(temp_df.Control_DAC, 1000*temp_df.DMM_wakely_V, 1)
print(b)
print(m)
x=np.arange(np.min(temp_df.Control_DAC),np.max(temp_df.Control_DAC))
y=m*x+b
# Now make a plot
fig = plt.figure(figsize=(14, 10), dpi=200)
axs=fig.add_subplot(111)

#gs = fig.add_gridspec(1, 1)
#axs = gs.subplots(sharex=True, sharey=False)
#axs = gs.subplots()
#axs[0].scatter(times, pressure, marker='.')
#axs[0].set_ylabel("Pressure (Torr)")
#axs[0].set_ylim([1, 759])

#labelling=["Dishy top","Dishy mount plate","Cold plate", "PoE PCB"]
#labelling=["Cold Plate","Dummy load","HSK Box rail", "Heatsink"]
#temp1 is 0 which is cold plate, temp2 is D0 ois thermal braid
axs.plot(x,y,'k')

axs.scatter(temp_df.Control_DAC, 1000*temp_df.DMM_wakely_V, marker='*', s=20) #this is a temp by the inflections.

#axs.scatter(temp_df.RealTimes, temp_df.temp2, marker='*', color='k', s=3,label = labelling[1]) #this is a temp by the inflections.
#axs.scatter(temp_df.RealTimes, temp_df.temp3, marker='+', color='r', s=3,label = labelling[2]) #this is a temp by the inflections.
#axs.scatter(temp_df.RealTimes, temp_df.temp4, marker='o', color='m', s=3,label = labelling[3]) #this is a temp by the inflections.
#pretesting=800
#cold_plating=3700
#power_on=4750
#power_off=8220
#setpoint_adj=9550
#axs.axvline(x=pretesting-5,ymin=0, ymax=1, ls=':', color='Brown')
#axs.text(pretesting, -17, "Test Power", color='Brown', rotation=90, fontsize=8)
#axs.axvline(x=cold_plating-5,ymin=0, ymax=1, ls=':', color='Brown')
#axs.text(cold_plating, -17, "Test Power", color='Brown', rotation=90, fontsize=8)
#axs.axvline(x=power_on,ymin=0, ymax=1, ls=':', color='Brown')
#axs.text(power_on, -17, "TVAC Start (stp -10)", color='Brown', rotation=90, fontsize=8)
#axs.axvline(x=power_off,ymin=0, ymax=1, ls=':', color='Brown')
#axs.text(power_off-350, 20, "Power On", color='Brown', rotation=90, fontsize=8)
#axs.axvline(x=setpoint_adj,ymin=0, ymax=1, ls=':', color='Brown')
#axs.text(setpoint_adj-350, 20, "Setpoint -20", color='Brown', rotation=90, fontsize=8)
#axs.axvspan(higher_power, ending, alpha=0.1, color='cyan', label="Worst Case")
#axs.axvspan(hot_case_start,hot_case_end , alpha=0.1, color='firebrick', label="hot case")
#axs.axvspan(kickflip_start,kickflip_end , alpha=0.3, hatch="XXX", color='darkorange', label="flipped hot case")

#axs[1].axvline(x=discharge_magnet,ymin=0, ymax=1, ls=':',color='Brown')
#axs[1].axvline(x=cold_wall_fill_start,ymin=0, ymax=1, color='black',label="cold wall fill start")
#axs[1].axvline(x=cold_wall_fill_end,ymin=0, ymax=1, color='black',label="cold wall fill start")

#axs.scatter(temp_df[temp_df.addr=="DA"].RealTimes, temp_df[temp_df.addr=="D1"].temp, marker='*',color='k',s=3,label="Copper Plate") #this is a temp by the inflections.
#axs.scatter(temp_df[temp_df.addr=="D0"].RealTimes, temp_df[temp_df.addr=="62"].temp, marker='+',color='r',s=3,label="Wedgelock") #this is a temp by the inflections.
#axs.scatter(temp_df[temp_df.addr=="10"].RealTimes, temp_df[temp_df.addr=="22"].temp, marker='o',s=3,color='m',label="TURFIO Heatsink back") #this is a temp by the inflections.

#dataframe[dataframe['Percentage'] > 70] 
#axs.scatter(times, magnetflows_array[:,0], marker='.',s=3) #this is a dictionary in each element of the array
#axs.scatter(times, Xadc_array[:,0], marker='.',s=3) #these are xadc for FPGA so array of voltages and temps somewhere
#axs.scatter(times, df['payload.fSFCStatus.fATX_V33'], marker='.',s=3) #this one is always 0
#axs.scatter(times, df['payload.fSFCStatus.fMB_V33SB'], marker='.',s=3) #this one is always 3.2 ish
#axs.scatter(times, df['payload.fSFCStatus.fMB_V33'], marker='.',s=3) #this one is always 2.56
plt.xlabel("DAC (count)")
plt.ylabel("DMM (V)")
plt.ylim([0,10000])
plt.xlim([0,4095])
plt.grid()
#handles, labels = axs.get_legend_handles_labels()
#lgd = axs.legend(handles, labels)
#lgd=fig.legend(handles, labels, loc='upper center', ncol=5, fontsize=8)
#for legend_handle in lgd.legendHandles:
    ###legend_handle.set_sizes([20])
#labels[6]._legmarker.set_markersize(6)
#lgd=fig.legend(handles, labels, loc='upper center', ncol=5, fontsize=8)
# as many of these as axs[1].scatter above


#lgd.legendHandles[-14].set_sizes([60])
#lgd.legendHandles[-13].set_sizes([60])
#lgd.legendHandles[-12].set_sizes([60])
#lgd.legendHandles[-11].set_sizes([60])
#lgd.legendHandles[-10].set_sizes([60])
#lgd.legendHandles[-9].set_sizes([60])
#lgd.legendHandles[-8].set_sizes([60])
#lgd.legendHandles[-7].set_sizes([60])
#lgd.legendHandles[-4].set_sizes([60])
#lgd.legendHandles[-3].set_sizes([60])
#lgd.legendHandles[-2].set_sizes([60])
#lgd.legendHandles[-1].set_sizes([60])
#lgd.legendHandles[-2].set_sizes([60])
#lgd.legendHandles[-1].set_sizes([60])#

#plt.savefig("plot_timeline_south.pdf", bbox_inches='tight')

#plt.savefig("plot_timeline_south.png")

plt.show()

#plt.xticks(rotation=45)
#plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %d - %H:%M'))
#plt.gcf().autofmt_xdate()
#axs[0].grid()
#axs.grid()
#handles, labels = axs.get_legend_handles_labels()
#lgd = axs[1].legend(handles, labels)
#for legend_handle in lgd.legendHandles:
#    legend_handle.set_sizes([20])
#labels[6]._legmarker.set_markersize(6)
#lgd=fig.legend(handles, labels, loc='upper center', ncol=5, fontsize=8)
# as many of these as axs[1].scatter above
#lgd.legendHandles[-14].set_sizes([60])
#lgd.legendHandles[-13].set_sizes([60])
#lgd.legendHandles[-12].set_sizes([60])
#lgd.legendHandles[-11].set_sizes([60])
#lgd.legendHandles[-10].set_sizes([60])
#lgd.legendHandles[-9].set_sizes([60])
#lgd.legendHandles[-8].set_sizes([60])
#lgd.legendHandles[-7].set_sizes([60])
#lgd.legendHandles[-6].set_sizes([60])
#lgd.legendHandles[-5].set_sizes([60])
#lgd.legendHandles[-4].set_sizes([60])
#lgd.legendHandles[-3].set_sizes([60])
#lgd.legendHandles[-2].set_sizes([60])
#lgd.legendHandles[-1].set_sizes([60])#
#plt.savefig("plot_timeline_south.pdf", bbox_inches='tight')
#plt.savefig("plot_timeline_south.png")
#plt.show()
