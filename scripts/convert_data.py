import os
import requests
import pyreadr
import pandas as pd

# List of data sets with the potential old and new file names
# ("challnege_summary" is mispelled but there's a pending PR to fix)
data_sets = [
    ("advantage_movement", "advantage_movement"),
    ("advantage_details", "advantage_details"),
    ("boot_mapping", "boot_mapping"),
    ("castaway_details", "castaway_details"),
    ("castaways", "castaways"),
    ("challenge_results", "challenge_results"),
    ("challenge_description", "challenge_description"),
    ("challenge_summary", "challnege_summary"),  # New name, old name
    ("confessionals", "confessionals"),
    ("jury_votes", "jury_votes"),
    ("season_summary", "season_summary"),
    ("survivor_auction", "survivor_auction"),
    ("tribe_colours", "tribe_colours"),
    ("tribe_mapping", "tribe_mapping"),
    ("episodes", "episodes"),
    ("vote_history", "vote_history"),
    ("auction_details", "auction_details"),
    ("screen_time", "screen_time"),
    ("season_palettes", "season_palettes"),
]

# Base URL to survivoR repo
base_url = "https://github.com/doehm/survivoR/raw/master/data/"

# Directory to save the CSV files
output_dir = "../data/raw/csv"
original_dir = "../data/raw/rda"

os.makedirs(output_dir, exist_ok=True)
os.makedirs(original_dir, exist_ok=True)

for new_name, old_name in data_sets:
    for file_name in (new_name, old_name):
        try:
            # Construct the URL
            url = f"{base_url}{file_name}.rda"

            # Fetch the .rda file with requests
            rda_file = os.path.join(original_dir, f"{file_name}.rda")
            response = requests.get(url)
            response.raise_for_status()  # Check for HTTP errors
            with open(rda_file, "wb") as file:
                file.write(response.content)

            # Read the .rda file using the pyreadr tool
            result = pyreadr.read_r(rda_file)

            # Check the contents of the .rda file
            if len(result) == 0:
                raise ValueError(f"No data found in {rda_file}")

            # Extract the first (and typically the only) object from the result
            df = next(iter(result.values()))

            # Ensure the object is a dataframe
            if not isinstance(df, pd.DataFrame):
                raise ValueError(f"Unexpected data type {type(df)} in {rda_file}")

            # Save the dataframe to a CSV
            csv_file = os.path.join(output_dir, f"{new_name}.csv")
            df.to_csv(csv_file, index=False)
            print(f"Successfully converted {new_name} (from {file_name}) to CSV.")

            break  # Exit the loop
        except requests.exceptions.RequestException as e:
            print(f"HTTP error for {file_name}: {e}")
        except ValueError as e:
            print(f"Data error for {file_name}: {e}")
        except Exception as e:
            print(f"Unexpected error for {file_name}: {e}")

print("Conversion completed!")