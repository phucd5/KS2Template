#Initilization
import os

os.environ["KILOSORT2_PATH"] = "./Kilosort"

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import pandas as pd
import seaborn as sns
from collections import defaultdict
from matplotlib_venn import venn3
import numpy as np

import spikeinterface as si 
import spikeinterface.extractors as se
import spikeinterface.toolkit as st
import spikeinterface.sorters as ss
import spikeinterface.comparison as sc
import spikeinterface.widgets as sw
from spikeinterface.comparison import GroundTruthStudy

#Do we want to run with initalized templates?
def use_temp():
    run_temp = input("Do you want to initalize KS2 with prviously found templates? (Yes/No): ")
    run_temp = run_temp.lower()

    if run_temp == 'yes':
        run_temp_res = '\nsetTemplate = true;'
        init_temp()
    else:
        run_temp_res = '\nsetTemplate = false;'

    with open(spike_path, 'a') as input_file:
        input_file.write(run_temp_res)

#Set the templates for MATLAB
def init_temp():

    temp_file_name = input("Enter the file name for the template: ")
    temp_dir = input("Enter the directory path for the template: ")

    temp_fres = "\nFileName = " + "\'" + temp_file_name + "\';"
    temp_dirres = "\nFolderName = " + "\'" + temp_dir + "\';"


    #/gpfs/ysm/project/seo/phd24/sort/spikeinterface
    #rez2.mat
    #/gpfs/ysm/project/seo/phd24/sort/Kilosort

    with open(spike_path, 'a') as input_file:
        input_file.write(temp_fres)
        input_file.write(temp_dirres)


def run_matching():
    rec0, gt_sorting0 = se.toy_example(num_channels=4, duration=10, seed=5,
num_segments=1)
    gt_dict = {
    'rec0': (rec0, gt_sorting0),
    }
    study_folder = 'a_study_folder'
    study = GroundTruthStudy.create(study_folder, gt_dict)
    sorter_list = ['kilosort2']
    study.run_sorters(sorter_list, mode_if_folder_exists="keep")
    study.run_comparisons(exhaustive_gt=True)

    for (rec_name, sorter_name), comp in study.comparisons.items():
        print('*' * 10)
        print(rec_name, sorter_name)
        print(comp.count_score)  # raw counting of tp/fp/...
        comp.print_summary()
        perf_unit = comp.get_performance(method='by_unit')
        perf_avg = comp.get_performance(method='pooled_with_average')
        m = comp.get_confusion_matrix()
        w_comp = sw.plot_agreement_matrix(comp)
        w_comp.ax.set_title(rec_name  + ' - ' + sorter_name)


spike_path = input("Enter directory path to spikeinterface folder ")
spike_path += '/spikeinterface/sorters/kilosort2/kilosort2_config.m'
use_temp()
run_matching()
