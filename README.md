# Setup

Install the program with:

```
git clone https://github.com/phucd5/KS2Template
```

Install SpikeInterface:

```
cd ks2template
pip install -e ./spikeinterface
```

__Note__: If there are errors make sure the following dependencies are installed:

- numpy
- neo>=0.9.0
- joblib
- probeinterface
- tqdm
- scipy
- h5py
- pandas
- sklearn
- matplotlib
- networkx
- datalad
- MEArec


# Template Requirements

- __U__: low-rank components of the spatial masks for each template


- __W__: low-rank components of the temporal masks for each template


- __mu__: mean amplitude for each template

This needs to be stored in a struct named ‘rez’ with variables U, W, mu. 

__Note__: If you want use templates founded by a previous run of Kilosort just use the outputted rez folder as the template file 

# Initializing Templates

- Step 1: Enter the directory path to the spike interface folder 
- Step 2: Enter “Yes” when asked if you want to initialize Kilosort 2 with templates
- Step 3: Enter the file name for the template
- Step 4: Enter the directory path to the folder that the template is in

Example:

```
Enter directory path to spikeinterface folder: /gpfs/ysm/project/seo/phd24/KS2Template/spikeinterface
Do you want to initialize KS2 with previously found templates? (Yes/No): Yes
Enter the file name for the template: rez2.mat
Enter the directory path to the folder of the template: /gpfs/ysm/project/seo/phd24/KS2Template             
```

__Note__: If you enter "No" for the initialization of templates, then Kilosort will run normally. The 'rez2.mat' folder is a sample template. 

# Running Kilosort


```
Do you want to use your own dataset? (Yes/No): Yes
Enter the directory path to the data: /gpfs/ysm/project/seo/phd24/sort/sub-MEAREC-250neuron-Neuropixels_ecephys.nwb
```

__Note__: If you enter no, Kilosort will generate a dataset for you to use to test the program. 