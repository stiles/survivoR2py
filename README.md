# survivoR2py: Survivor data for Python users

## About

The code in this repository converts data files in an R package devoted to the Survivor television series from `.rda` to `.csv` formats so that Python users can enjoy them. A

## Sources

The data comes from the [survivoR](https://github.com/doehm/survivoR) package created by [David Ohm](https://github.com/doehm), et al. They have organized and created numerous detailed and useful datasets about the history of the show, including an episode summary, castaway listing, challenge results and vote history, among many others. 

## Process

### Convert survivoR data

- `scripts/convert_data.py`: This script converts the survivoR data by fetching the latest `.rda` files from the source, storing copies locally in `data/raw/rda`, and then converting them to comma-delimited text files in `data/processed/csv`. A Gihub Actions workflow also runs the script once daily to keep it fresh during the seasons, storing the data locally in the repo and also pushing it to S3.

**The data files can be downloaded here:** 

- [advantage_details.csv](https://stilesdata.com/survivor/survivor2py/processed/csv/advantage_details.csv)
- [advantage_movement.csv](https://stilesdata.com/survivor/survivor2py/processed/csv/advantage_movement.csv)
- [auction_details.csv](https://stilesdata.com/survivor/survivor2py/processed/csv/auction_details.csv)
- [boot_mapping.csv](https://stilesdata.com/survivor/survivor2py/processed/csv/boot_mapping.csv)
- [castaway_details.csv](https://stilesdata.com/survivor/survivor2py/processed/csv/castaway_details.csv)
- [castaways.csv](https://stilesdata.com/survivor/survivor2py/processed/csv/castaways.csv)
- [challenge_description.csv](https://stilesdata.com/survivor/survivor2py/processed/csv/challenge_description.csv)
- [challenge_results.csv](https://stilesdata.com/survivor/survivor2py/processed/csv/challenge_results.csv)
- [challenge_summary.csv](https://stilesdata.com/survivor/survivor2py/processed/csv/challenge_summary.csv)
- [confessionals.csv](https://stilesdata.com/survivor/survivor2py/processed/csv/confessionals.csv)
- [episodes.csv](https://stilesdata.com/survivor/survivor2py/processed/csv/episodes.csv)
- [jury_votes.csv](https://stilesdata.com/survivor/survivor2py/processed/csv/jury_votes.csv)
- [screen_time.csv](https://stilesdata.com/survivor/survivor2py/processed/csv/screen_time.csv)
- [season_palettes.csv](https://stilesdata.com/survivor/survivor2py/processed/csv/season_palettes.csv)
- [season_summary.csv](https://stilesdata.com/survivor/survivor2py/processed/csv/season_summary.csv)
- [survivor_auction.csv](https://stilesdata.com/survivor/survivor2py/processed/csv/survivor_auction.csv)
- [tribe_colours.csv](https://stilesdata.com/survivor/survivor2py/processed/csv/tribe_colours.csv)
- [tribe_mapping.csv](https://stilesdata.com/survivor/survivor2py/processed/csv/tribe_mapping.csv)
- [vote_history.csv](https://stilesdata.com/survivor/survivor2py/processed/csv/vote_history.csv)

*Notes: The converted `.rda` data files from the [original project](https://github.com/doehm/survivoR/blob/master/README.md) are stored in this repo's `raw/csv` directory. The content of those files <ins>won't change</ins> — only the file formats. Any value errors can be flagged as issues there. They are typically resolved quickly. Also: Please see the [original repo](https://github.com/doehm/survivoR/blob/master/README.md) for metadata about the individual files.*

## Related repositories

- [survivor-voteoffs](https://github.com/stiles/survivor-voteoffs): *How did each castaway react to his or her torch getting snuffed? There's data for that.*
- [survivor-transcripts](https://github.com/stiles/survivor-transcripts): *Fetching and storing complete transcripts for each episode of the American television show and analyzing the text for keyword/phrase frequency.*


## Questions? Corrections? 

[Please let me know](mailto:mattstiles@gmail.com).
