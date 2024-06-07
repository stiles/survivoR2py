# survivoR2py: Survivor data for Python users

### About the project

The code in this repository converts data files in an R package devoted to the Survivor television series from `.rda` to `.csv` formats so that Python users can enjoy them. There are also scripts here for downloading and parsing show transcripts and documenting vote-off moments. These latter two aren't fully baked and are living here until they find a home elsewhere.

### Sources

The data comes from the [survivoR](https://github.com/doehm/survivoR) package created by [David Ohm](https://github.com/doehm), et al. They have organized and created numerous detailed and useful datasets about the history of the show, including an episode summary, castaway listing, challenge results, and vote history. Transcripts come from [subslikescript](https://subslikescript.com/series/Survivor-239195).

### Processes

Three scripts, for now, process the data.

##### Convert survivoR data

- `scripts/convert_data.py`: This script converts the survivoR data by fetching all the latest `.rda` files from the source, storing copies locally in `data/raw/rda`, and converting them to comma-delimited text files in `data/raw/csv`.
    - See the [original repo](https://github.com/doehm/survivoR/blob/master/README.md) for metadata about the individual files.
    - **Note:** Other than the format change, the content of data downloaded, processed, and stored in the `raw` directory will remain unchanged from the original repo.

##### Fetch transcripts

- `scripts/fetch_transcripts.py`: This script collects all episode transcript URLs, converts the URLs to metadata (episode number, season, episode title, URL, etc.), fetches the full transcript for each episode, and parses the text for what contestants said after Jeff's famous line, "The tribe has spoken." All of it is stored in a dataframe and exported to CSV and JSON. The goal is to refine the dataset enough so it might be useful to offer back to the survivoR folks.

##### Add vote-off logs

- `scripts/vote_off_reaction.py`: Fetches a [public Google Sheet](https://docs.google.com/spreadsheets/d/1nys0mCWArUCtPKYIVBrbjmv7eAWkmOce4cBlyHm8b0c/edit?usp=sharing) where vote-off reactions are being hand-logged. This is growing *slowly* and needs contributors. The goal is to build a dataset that shows all voted-off players' reactions *after* Jeff doused their torches and *before* they walked out of the Tribal Council.

**Dataset description**

| Column         | Description                                                                                               | Type    |
|----------------|-----------------------------------------------------------------------------------------------------------|---------|
| season         | Season number                                                                                             | `string`  |
| vote           | Vote number that season                                                                                   | `string`  |
| contestant     | First name                                                                                                | `string`  |
| acknowledge    | Did the contestant acknowledge their teammates *in any way* after dousing — or just walk away?              | `boolean` |
| gesture        | Category of `acknowledge`. Did the contestant gesture to their former teammates, i.e., a wave, smile, nod  | `boolean` |
| words          | Category of `acknowledge`. Did the contestant say anything to their teammates?                            | `boolean` |
| words_desc     | Optional: What, if anything, the contestant said *after the dousing and before walking away*              | `string`  |
| notes          | Optional: Any notes about the moment, caveats about the log, etc.                                         | `string`  |
| log            | Date when data was logged (%Y-%m-%d)                                                                      | `date`    |

**Dataset example**

| season | vote | contestant | acknowledge | gesture | words | words_desc | notes | log        |
|--------|------|------------|-------------|---------|-------|------------|-------|------------|
| 11     | 1    | Jim       | true        | false   | false |       | Looked back silently  | 2024-06-04 |

**Scenario explanation**

- Jim looked back at the tribe that voted him off, so he acknowledged their decision, but he didn't wave (or otherwise gesture) and he remained silent. Poor Jim.

### Questions?

[Please let me know](mailto:mattstiles@gmail.com).
