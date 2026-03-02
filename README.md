# MONAN Analysis

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

## Installation

### 1. Clone the repository

```
git clone https://github.com/GAMA-INPE/monan_analysis.git
cd monan_analysis
```

### 2. Set up conda environment

# If necessary, load Anaconda module
```
module load anaconda
```

 


