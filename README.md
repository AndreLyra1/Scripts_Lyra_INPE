monan_analysis/
│
├── README.md
├── pyproject.toml        # makes packages inside src/ installable
├── requirements.txt      # lists packages needed to run repo
├── .gitignore            # lists files to be ignored by git
│
├── src/                  # source code (installable package)
│   └── monan_analysis/   # namespace for importing libraries (e.g., from monan_analysis.utils import ...) 
│       ├── __init__.py   # python looks for this file when importing modules
│       ├── utils.py      # reusable general-purpose routines
│       ├── io.py         # reusable routines for reading input and saving output
│       ├── plotting.py   # reusable routines for plotting
│       └── stats.py      # reusable routines for calculating statistics
│
├── analyses/             # ready-to-use analysis code
│   ├── analysis1/
│   │   ├── run.py
│   │   └── run.sh
│   │
│   └── analysis2/
│       ├── run.py
│       └── run.sh
│
└── exploratory/          # exploratory (preliminary) scripts
