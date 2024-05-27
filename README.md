# survivoR2py: Survivor data for Python users

### About

The code in this repository converts data files in an R package devoted to the Survivor television series from `.rda` to `.csv` formats so that Python users can enjoy them. 

### Source

The data comes from the [survivoR](https://github.com/doehm/survivoR) package created by [David Ohm](https://github.com/doehm), et al. They have organized and created numerous detailed and useful datasets about the history of the show, including an episode summary, castaway listing, challenge results and vote history. 

The original data is provided under the MIT License, and this repository retains that license.

### Process

For now, a simple script converts the data files and stores them for use with other Python data science tools, including Pandas. 

- `scripts/convert_data.py`: Fetches all the latest `.rda` files from the source, stores copies locally in `data/raw/rda` and converts them to comma-delimited text files in `data/raw/csv`.
    - See the [original repo](https://github.com/doehm/survivoR/blob/master/README.md) for metadata about the indiviual files.
    - **Note:** Other than the format change, the content of data downloaded, processed and stored in the `raw` directory will remain unchained from the original repo.
- More analysis/visualization scripts **TK**.

### Usage

To use this data in your Python projects, simply clone the repository and load the `csv` files your preferred data analysis library. Questions? [Please let me know](mailto:mattstiles@gmail.com). 