#!/usr/bin/python

import time
import pprint
import pandas as pd
import numpy as np
from numpy.polynomial.polynomial import polyfit
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import os
from pip import main

print(os.getcwd())
print(os.path.dirname(__file__))
data_path=os.path.dirname(__file__)
#file_name="testing_cleanup.csv"
file_name="hv_data_IMON_all_configs_plot_transposed.csv"
name_to_read=os.path.join(data_path,file_name)

temp_df=pd.read_csv(name_to_read)

print(temp_df.head())
column_names=temp_df.keys()
print(column_names[0])
#quit()
#quit()
#dac=np.linspace(0,4000,8,endpoint=True)
#print(dac[-1])
#print(len(dac))
#temp_df.DAC=dac
#fit a line...

#b, m = polyfit(temp_df.Control_DAC, 1000*temp_df.DMM_wakely_V, 1)
#print(b)
#print(m)
#x=np.arange(np.min(temp_df.Control_DAC),np.max(temp_df.Control_DAC))
#y=m*x+b

#which_HV="Cathode"
which_HV="Potential"

pdf = PdfPages(which_HV+'_variation_IMON.pdf')
#pdf = PdfPages('Cathode_variation_DMM.pdf')
# Now make a plot

i=1
while i < 10:

    fig = plt.figure(figsize=(14, 10), dpi=200)
    plt.clf()
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
    #axs.plot(x,y,'k')
    #axs.hist(temp_df['Cat-AB'])
    if which_HV=="Cathode":
        axs.scatter(temp_df.Config.values[0:7], temp_df[column_names[i]].values[0:7], marker='D', s=30,
                label='DAC set to '+column_names[i]) #this is a temp by the inflections.
    else:
        axs.scatter(temp_df.Config.values[7:], temp_df[column_names[i]].values[7:], marker='D', s=30,
                label='DAC set to '+column_names[i]) #this is a temp by the inflections.
    #axs.scatter(temp_df.DAC, temp_df['C,O,O,S'], marker='o', s=20,label='Cathode/Drift O,O,S') #this is a temp by the inflections.
    #axs.scatter(temp_df.DAC, temp_df['C,O,S,O'], marker='.', s=20,label='Cathode/Drift O,S,O') #this is a temp by the inflections.
    
    plt.ylabel("IMON (ADC)")
    plt.xlabel("Configuration (DCT HSK, ToM++, Cable)")
    #plt.ylim([0,0.06])
    #plt.xlim([0,4095])
    plt.grid()
    handles, labels = axs.get_legend_handles_labels()
    lgd = axs.legend(handles, labels)
    lgd=fig.legend(handles, labels, loc='upper center', ncol=5, fontsize=8)
    lgd.legend_handles[-1].set_sizes([60])
    #plt.savefig("cathode_variation_DAC_"+column_names[i]+".pdf", bbox_inches='tight')
    pdf.savefig(fig)
    #plt.show()
    i+=1

pdf.close()

