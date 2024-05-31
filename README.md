# survivoR2py: Survivor data for Python users

### About the project

The code in this repository converts data files in an R package devoted to the Survivor television series from `.rda` to `.csv` formats so that Python users can enjoy them. There's also a script here for downloading and parsing show transcripts.

### Sources

The data comes from the [survivoR](https://github.com/doehm/survivoR) package created by [David Ohm](https://github.com/doehm), et al. They have organized and created numerous detailed and useful datasets about the history of the show, including an episode summary, castaway listing, challenge results and vote history. Transcripts come from [subslikescript](https://subslikescript.com/series/Survivor-239195). 

### Processes

Two scripts for now process the data for use with Python-friendly data science tools. 

- `scripts/convert_data.py`: The script converts the survivoR data by fetching all the latest `.rda` files from the source, stores copies locally in `data/raw/rda` and converts them to comma-delimited text files in `data/raw/csv`.
    - See the [original repo](https://github.com/doehm/survivoR/blob/master/README.md) for metadata about the indiviual files.
    - **Note:** Other than the format change, the content of data downloaded, processed and stored in the `raw` directory will remain unchained from the original repo.

- `scripts/fetch_transcripts.py`: The script collects all episode transcript urls, converts the urls to metadata (episode number, season, episode title, url, etc.), fetches the full transcript for each episode and parses the text for what contestants said after Jeff's famous line, "The tribe has spoken". All of it is stored in a dataframe and exported to CSV and JSON. The goal is to refine the dataset enough so it might be useful enough to offer back to the survivoR folks. 

- More analysis/visualization/scripts **TK**.

### Usage

To use this data in your Python projects, simply clone the repository and load the `csv` files your preferred data analysis library. Questions? [Please let me know](mailto:mattstiles@gmail.com). 
