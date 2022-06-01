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


#Set the templates for MATLAB
def init_temp():

    temp_file_name = input("Enter the file name for the template: ")
    temp_dir = input("Enter the directory path to the folder of the template: ")

    temp_fres = "\nFileName = " + "\'" + temp_file_name + "\';"
    temp_dirres = "\nFolderName = " + "\'" + temp_dir + "\';"


    #/gpfs/ysm/project/seo/phd24/sort/spikeinterface
    #rez2.mat
    #/gpfs/ysm/project/seo/phd24/sort/Kilosort

    with open(spike_path, 'a') as input_file:
        input_file.write(temp_fres)
        input_file.write(temp_dirres)

def init_data():
    #Use real dataset
    data_filename = input("Enter the directory path to the data: ")
    SX_gt = se.NwbSortingExtractor(str(data_filename))
    RX = se.NwbRecordingExtractor(str(data_filename))
    
    study_folder = 'study_folder'
    gt_dict = {'rec0' : (RX, SX_gt) }
    study = GroundTruthStudy.create(study_folder, gt_dict)
    spike_matching_run(study)


def init_test_data():
    #Create sample data
    rec0, gt_sorting0 = se.toy_example(num_channels=4, duration=10, seed=5, num_segments=1)
    gt_dict = {
    'rec0': (rec0, gt_sorting0),
    }
    study_folder = 'study_folder'
    study = GroundTruthStudy.create(study_folder, gt_dict)

    spike_matching_run(study)


#Do we want to run with initalized templates?
def use_temp():
    run_temp = input("Do you want to initalize KS2 with previously found templates? (Yes/No): ")
    run_temp = run_temp.lower()

    if run_temp == 'yes':
        run_temp_res = '\nsetTemplate = true;'
        init_temp()
    else:
        run_temp_res = '\nsetTemplate = false;'

    with open(spike_path, 'a') as input_file:
        input_file.write(run_temp_res)


def choose_data():
    use_data = input("Do you want to use your own dataset? (Yes/No) ")

    use_data = use_data.lower()

    if use_data == 'yes':
        init_data()
    else:
        print("Using test data")
        init_test_data()


def spike_matching_run(study):
    sorter_list = ['kilosort2']
    study.run_sorters(sorter_list, mode_if_folder_exists="keep")
    study.run_comparisons(exhaustive_gt=True)

    for (rec_name, sorter_name), comp in study.comparisons.items():
        print('*' * 10)
        print(rec_name, sorter_name)
        print(comp.count_score)  # raw counting of tp/fp/...
        comp.print_summary()



spike_path = input("Enter directory path to spikeinterface folder: ")
spike_path += '/spikeinterface/sorters/kilosort2/kilosort2_config.m'
use_temp()
choose_data()
