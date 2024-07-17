# survivoR2py: Survivor data for Python users

## About

The code in this repository converts data files in an R package devoted to the Survivor television series from `.rda` to `.csv` formats so that Python users can enjoy them.

## Sources

The data comes from the [survivoR](https://github.com/doehm/survivoR) package created by [David Ohm](https://github.com/doehm), et al. They have organized and created numerous detailed and useful datasets about the history of the show, including an episode summary, castaway listing, challenge results and vote history, among many others. 

## Process

### Convert survivoR data

- `scripts/convert_data.py`: This script converts the survivoR data by fetching the latest `.rda` files from the source, storing copies locally in `data/raw/rda`, and then converting them to comma-delimited text files in `data/processed/csv`.

*Notes: The converted `.rda` data files from the [original project](https://github.com/doehm/survivoR/blob/master/README.md) are stored in this repo's `processed/csv` directory. The content of those files <ins>won't change</ins> — only the file formats. Any value errors can be flagged as issues there. They are typically resolved quickly. Also: Please see the [original repo](https://github.com/doehm/survivoR/blob/master/README.md) for metadata about the individual files.*

## Related repositories

- [survivor-voteoffs](https://github.com/stiles/survivor-voteoffs): *How did each castaway react to his or her torch getting snuffed? There's data for that.*
- [survivor-transcripts](https://github.com/stiles/survivor-voteoffs): *Fetching and storing complete transcripts for each episode of the American television show and analyzing the text for keyword/phrase frequency.*

## Questions? Corrections? 

[Please let me know](mailto:mattstiles@gmail.com).