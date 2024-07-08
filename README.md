# survivoR2py: Survivor data for Python users

## About the project

The code in this repository converts data files in an R package devoted to the Survivor television series from `.rda` to `.csv` formats so that Python users can enjoy them. There are also scripts here for downloading and parsing show transcripts. This latter process isn't fulled baked and is living here until it finds a home elsewhere.

## Sources

The data comes from the [survivoR](https://github.com/doehm/survivoR) package created by [David Ohm](https://github.com/doehm), et al. They have organized and created numerous detailed and useful datasets about the history of the show, including an episode summary, castaway listing, challenge results, and vote history. Transcripts come from [subslikescript](https://subslikescript.com/series/Survivor-239195) and CBS/Paramount.

## Processes

These scripts process data.

### Convert survivoR data

- `scripts/convert_data.py`: This script converts the survivoR data by fetching all the latest `.rda` files from the source, storing copies locally in `data/raw/rda`, and converting them to comma-delimited text files in `data/raw/csv`.
    - See the [original repo](https://github.com/doehm/survivoR/blob/master/README.md) for metadata about the individual files.
    - **Note:** Other than the format change, the content of data downloaded, processed, and stored in the `raw` directory will remain unchanged from the original repo.

### Fetch transcripts

- `scripts/fetch_transcripts.py`: This script collects all episode transcript URLs, converts the URLs to metadata (episode number, season, episode title, URL, etc.), fetches the full transcript for each episode, and parses the text for what contestants said after Jeff's famous line, "The tribe has spoken." All of it is stored in a dataframe and exported to CSV and JSON. The goal is to refine the dataset enough so it might be useful to offer back to the survivoR folks.

## Questions? Corrections? 

[Please let me know](mailto:mattstiles@gmail.com).

## Related
- [survivor-voteoffs](https://github.com/stiles/survivor-voteoffs)