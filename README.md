# MONAN analysis

Project to centralize code for analyses of simulations with the MONAN model.

## Structure
```
monan_analysis/
├── README.md             
├── pyproject.toml        # makes packages inside src/ installable
├── requirements.txt      # lists libraries needed to run repo
├── .gitignore            # lists files to be ignored by git
├── src/                  # source code (installable packages)
│   └── monan_analysis/   # namespace for monan_analysis package
│       ├── __init__.py   # python looks for this file when importing modules
│       ├── utils.py      # reusable general-purpose routines
│       ├── io.py         # reusable routines for reading input and saving output
│       ├── plotting.py   # reusable routines for plotting
│       └── stats.py      # reusable routines for calculating statistics
├── analyses/             # ready-to-use analysis code
│   ├── analysis1/
│   │   ├── run.py        # exemplary main script for analysis1
│   │   └── run.sh        # exemplary helper shell script for analysis1
│   └── analysis2/
│       ├── run.py        # exemplary main script for analysis2
│       └── run.sh        # exemplary helper shell script for analysis2
└── exploratory/          # exploratory (preliminary) scripts
```
____________

## Installation guide

### 1. Clone the repository

```
git clone https://github.com/GAMA-INPE/monan_analysis.git
cd monan_analysis
```

### 2. Set up conda environment

2.1) If using an HPC system, load Anaconda (or other conda)  module
```
module load anaconda
```
2.2) Create conda environment to install project packages
```
conda create -n gama
```
2.3) Activate conda environment
```
conda activate gama
```
2.4) Install python inside that conda environment
```
conda install python=3.12
```
2.5) Make sure python is installed in the conda env
```
which python
```
If the above points to your recently created conda environment, proceed to step 3.

### 3. Install project-specific dependencies
All project-specific dependencies, including own project packages under `src/`, are listed in `requirements.txt`. Depending on whether you have external dependencies already installed, you can follow two options: 

a) If you do not yet have external dependencies installed, you can install all those dependencies plus the project packages by running
```
python -m pip install -r requirements.txt
```

b) If you already have the needed external dependencies but want to install only the project packages under `src/`, you can do this by running
```
python -m pip install -e .
```
inside your conda environment.

After this installation by option a) or b), you should be able to import in particular modules from the packages under `src/` in your analysis scripts. You can test this by running from the project's root
```
python exploratory/import_test/example_analysis.py
```
If the packages have been installed correctly, this test should return you
```
this is a function imported from the utils.py module.
this is a function imported from the io.py module.
this is a function imported from the plots.py module.
this is a function imported from the stats.py module.
```
