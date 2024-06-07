# survivoR2py: Survivor data for Python users

## About the project

The code in this repository converts data files in an R package devoted to the Survivor television series from `.rda` to `.csv` formats so that Python users can enjoy them. There are also scripts here for downloading and parsing show transcripts and documenting vote-off moments. These latter two aren't fully baked and are living here until they find a home elsewhere.

### Sources

The data comes from the [survivoR](https://github.com/doehm/survivoR) package created by [David Ohm](https://github.com/doehm), et al. They have organized and created numerous detailed and useful datasets about the history of the show, including an episode summary, castaway listing, challenge results, and vote history. Transcripts come from [subslikescript](https://subslikescript.com/series/Survivor-239195). Vote-off logs are created by me with eventual support from other fans, I hope. 

### Processes

Two scripts for now process the data for use with Python-friendly data science tools.

### Convert survivoR data

- `scripts/convert_data.py`: This script converts the survivoR data by fetching all the latest `.rda` files from the source, storing copies locally in `data/raw/rda`, and converting them to comma-delimited text files in `data/raw/csv`.
    - See the [original repo](https://github.com/doehm/survivoR/blob/master/README.md) for metadata about the individual files.
    - **Note:** Other than the format change, the content of data downloaded, processed, and stored in the `raw` directory will remain unchanged from the original repo.

### Fetch transcripts

- `scripts/fetch_transcripts.py`: This script collects all episode transcript URLs, converts the URLs to metadata (episode number, season, episode title, URL, etc.), fetches the full transcript for each episode, and parses the text for what contestants said after Jeff's famous line, "The tribe has spoken." All of it is stored in a dataframe and exported to CSV and JSON. The goal is to refine the dataset enough so it might be useful to offer back to the survivoR folks.

### Vote-off logs

- `scripts/vote_off_reaction.py`: Fetches a [public Google Sheet](https://docs.google.com/spreadsheets/d/1nys0mCWArUCtPKYIVBrbjmv7eAWkmOce4cBlyHm8b0c/edit?usp=sharing) where vote-off reactions are being hand-logged. This is growing *slowly* and needs contributors. The goal is to build a dataset that shows all voted-off players' reactions *after* Jeff doused their torches and *before* they walked out of the Tribal Council.

**Data collection**

To ensure accurate data collection and prevent sabotage, I'm considering using a controlled method like a Google Form for submitted entries. For now, I'm doing it by hand. 

**Format**

| Column         | Description                                                                                               | Type    |
|----------------|-----------------------------------------------------------------------------------------------------------|---------|
| season         | Season number                                                                                             | `string`  |
| vote           | Vote number that season                                                                                   | `string`  |
| contestant     | First name                                                                                                | `string`  |
| acknowledge    | Did the contestant acknowledge their teammates *in any way* after dousing — or just walk away?              | `boolean` |
| ack_gesture    | Category of `acknowledge`. Did the contestant gesture to their former teammates, i.e., a wave, smile, nod  | `boolean` |
| ack_speak      | Category of `acknowledge`. Did the contestant say anything to their teammates?                            | `boolean` |
| ack_look       | Category of `acknowledge`. Did the contestant make eye contact with their teammates?                       | `boolean` |
| ack_smile      | Category of `acknowledge`. Did the contestant smile at their teammates?                                    | `boolean` |
| ack_speak_notes| Optional: What, if anything, the contestant said *after the dousing and before walking away*               | `string`  |
| notes          | Optional: Any notes about the moment, caveats about the log, etc.                                          | `string`  |
| log            | Date when data was logged (%Y-%m-%d)                                                                       | `date`    |

**Notes about acknowledgment**

*Acknowledgment* after being voted off in Survivor — that moment between torch dousing and leaving Tribal Council — is categorized into four Boolean fields (each action is recorded as TRUE if performed, otherwise FALSE): 

- `ack_gesture`: for any physical gestures towards the tribe (e.g., waving, nodding, or hands in prayer)
- `ack_speak`: for any verbal communication with the tribe
- `ack_look`: for making eye contact with the tribe
- `ack_smile`: for smiling at the tribe

**Dataset example**

| season | vote | contestant | acknowledge | ack_gesture | ack_speak | ack_look | ack_smile | ack_speak_notes | notes               | log        |
|--------|------|------------|-------------|-------------|-----------|----------|-----------|-----------------|---------------------|------------|
| 11     | 1    | Jim        | TRUE        | FALSE       | FALSE     | TRUE     | FALSE     |                 | Silently looked back | 2024-06-06 |

**Scenario explanation**

- Jim, from season 11, was the first person voted off. He acknowledged his team by looking back but didn't wave, say anything, or smile. So, his acknowledgment would be true, but his score would only be one because all he did was look.

**Acknowledge score calculation**

The score is derived from the four subcategories of acknowledgment: words, look, gesture, and smile. Each `true` value in these categories adds 1 to the score. For example:

- If a contestant says words while looking back, waves, and smiles, their score is 4.
- If a contestant does nothing, their score is 0.

### Questions?

[Please let me know](mailto:mattstiles@gmail.com).
