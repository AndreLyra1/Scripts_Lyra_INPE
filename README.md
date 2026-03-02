# Project structure
```
monan_analysis/
├── README.md             # this file
├── pyproject.toml        # makes packages inside src/ installable
├── requirements.txt      # lists packages needed to run repo
├── .gitignore            # lists files to be ignored by git
├── src/                  # source code (installable package)
│   └── monan_analysis/   # namespace for importing libraries
│       ├── __init__.py   # python looks for this file when importing modules
│       ├── utils.py      # reusable general-purpose routines
│       ├── io.py         # reusable routines for reading input and saving output
│       ├── plotting.py   # reusable routines for plotting
│       └── stats.py      # reusable routines for calculating statistics
├── analyses/             # ready-to-use analysis code
│   ├── analysis1/
│   │   ├── run.py        # main script for analysis1
│   │   └── run.sh        # helper shell script for analysis1
│   └── analysis2/
│       ├── run.py        # main script for analysis2
│       └── run.sh        # helper shell script for analysis2
└── exploratory/          # exploratory (preliminary) scripts
```
