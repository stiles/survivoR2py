# survivoR2py: Survivor data for Python users

### About

This repository converts data files in an R package devoted to the Survivor television series from `.rda` to `.csv` formats so that Python users can enjoy them. 

The [survivoR](https://github.com/doehm/survivoR) R package has numerous datasets about the game, including an episode summary, castaway listing, challenge results and vote history, among many.

### Process

- `scripts/convert_data.py`: Fetches all the latest `.rda` files from the source, stores copies locally in `data/raw/csv` and converts them to comma-delimited text files in `data/raw/csv`.
    - See the [original repo](https://github.com/doehm/survivoR/blob/master/README.md) for metadata about the indiviual files.
    - **Note:** Other than the format change, the content of data downloaded, processed and stored in the `raw` directory will remain unchained from the original repo.

### Data sources

The data in this repository is sourced from the [survivoR](https://github.com/doehm/survivoR) package created by [David Ohm](https://github.com/doehm), et al. The original data is provided under the MIT License, and this repository retains that license.

### Usage

To use this data in your Python projects, simply clone the repository and load the CSV files using Pandas or your preferred data analysis library.