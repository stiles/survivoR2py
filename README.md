# survivoR2py: Survivor data for Python users

## About

The code in this repository converts data files in an R package devoted to the Survivor television series from `.rda` to `.csv` and `.json` formats for users who prefer Python or other data sceience tools. 

## Sources

The data comes from the canonical [survivoR](https://github.com/doehm/survivoR) package created by [David Ohm](https://github.com/doehm), et al, which contains detailed datasets about the history of the show, including an episode summary, castaway listing, challenge results and vote history, among many others. 

## Process

### Convert survivoR data

- `scripts/convert_data.py`: This script converts the survivoR data by fetching the latest `.rda` files from the source, storing copies locally in `data/raw/rda`, and then converting them to comma-delimited text files in `data/processed/csv`. A Gihub Actions workflow also runs the script once daily at 8 pm Pacific Time to keep the files fresh during a season, storing data in the repo and also on S3.

### Storage

The latest version of each table can be downloaded here: 

- `advantage_details`: [json](https://stilesdata.com/survivor/survivoR2py/processed/json/advantage_details.json), [csv](http:stilesdata.com/survivor/survivor2py/processed/csv/advantage_details)
- `advantage_movement`: [json](https://stilesdata.com/survivor/survivoR2py/processed/json/advantage_movement.json), [csv](http:stilesdata.com/survivor/survivor2py/processed/csv/advantage_movement)
- `auction_details`: [json](https://stilesdata.com/survivor/survivoR2py/processed/json/auction_details.json), [csv](http:stilesdata.com/survivor/survivor2py/processed/csv/auction_details)
- `boot_mapping`: [json](https://stilesdata.com/survivor/survivoR2py/processed/json/boot_mapping.json), [csv](http:stilesdata.com/survivor/survivor2py/processed/csv/boot_mapping)
- `castaway_details`: [json](https://stilesdata.com/survivor/survivoR2py/processed/json/castaway_details.json), [csv](http:stilesdata.com/survivor/survivor2py/processed/csv/castaway_details)
- `castaways`: [json](https://stilesdata.com/survivor/survivoR2py/processed/json/castaways.json), [csv](http:stilesdata.com/survivor/survivor2py/processed/csv/castaways)
- `challenge_description`: [json](https://stilesdata.com/survivor/survivoR2py/processed/json/challenge_description.json), [csv](http:stilesdata.com/survivor/survivor2py/processed/csv/challenge_description)
- `challenge_results`: [json](https://stilesdata.com/survivor/survivoR2py/processed/json/challenge_results.json), [csv](http:stilesdata.com/survivor/survivor2py/processed/csv/challenge_results)
- `challenge_summary`: [json](https://stilesdata.com/survivor/survivoR2py/processed/json/challenge_summary.json), [csv](http:stilesdata.com/survivor/survivor2py/processed/csv/challenge_summary)
- `confessionals`: [json](https://stilesdata.com/survivor/survivoR2py/processed/json/confessionals.json), [csv](http:stilesdata.com/survivor/survivor2py/processed/csv/confessionals)
- `episodes`: [json](https://stilesdata.com/survivor/survivoR2py/processed/json/episodes.json), [csv](http:stilesdata.com/survivor/survivor2py/processed/csv/episodes)
- `jury_votes`: [json](https://stilesdata.com/survivor/survivoR2py/processed/json/jury_votes.json), [csv](http:stilesdata.com/survivor/survivor2py/processed/csv/jury_votes)
- `screen_time`: [json](https://stilesdata.com/survivor/survivoR2py/processed/json/screen_time.json), [csv](http:stilesdata.com/survivor/survivor2py/processed/csv/screen_time)
- `season_palettes`: [json](https://stilesdata.com/survivor/survivoR2py/processed/json/season_palettes.json), [csv](http:stilesdata.com/survivor/survivor2py/processed/csv/season_palettes)
- `season_summary`: [json](https://stilesdata.com/survivor/survivoR2py/processed/json/season_summary.json), [csv](http:stilesdata.com/survivor/survivor2py/processed/csv/season_summary)
- `survivor_auction`: [json](https://stilesdata.com/survivor/survivoR2py/processed/json/survivor_auction.json), [csv](http:stilesdata.com/survivor/survivor2py/processed/csv/survivor_auction)
- `tribe_colours`: [json](https://stilesdata.com/survivor/survivoR2py/processed/json/tribe_colours.json), [csv](http:stilesdata.com/survivor/survivor2py/processed/csv/tribe_colours)
- `tribe_mapping`: [json](https://stilesdata.com/survivor/survivoR2py/processed/json/tribe_mapping.json), [csv](http:stilesdata.com/survivor/survivor2py/processed/csv/tribe_mapping)
- `vote_history`: [json](https://stilesdata.com/survivor/survivoR2py/processed/json/vote_history.json), [csv](http:stilesdata.com/survivor/survivor2py/processed/csv/vote_history)

*Notes: The converted `.rda` data files from the [original project](https://github.com/doehm/survivoR/blob/master/README.md) are stored in this repo's `raw/csv` directory. The content of those files <ins>won't change</ins> — only the file formats. Any value errors can be flagged as issues there. They are typically resolved quickly. Also: Please see the [original repo](https://github.com/doehm/survivoR/blob/master/README.md) for metadata about the individual files.*

## Related repositories

- [survivor-voteoffs](https://github.com/stiles/survivor-voteoffs): *How did each castaway react to his or her torch getting snuffed? There's data for that.*
- [survivor-transcripts](https://github.com/stiles/survivor-transcripts): *Fetching and storing complete transcripts for each episode of the American television show and analyzing the text for keyword/phrase frequency.*


## Questions? Corrections? 

[Please let me know](mailto:mattstiles@gmail.com).
