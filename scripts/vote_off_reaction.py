import os
import pandas as pd

"""
FETCH & SCORE
How did contestants respond after their torch was doused? 
This script fetches the growing log and scores the acknowlegement of his/her tribe.
"""

# Define URL for Google Sheets CSV
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQfmJJvr0TdW6fZ-wDdTadFDY5wTm2S6cnr9-n2D3cS6-eRGbIySzVokY97bON66_BXDIc0jnSjch82/pub?gid=120496879&single=true&output=csv'

# Read CSV from URL
df = pd.read_csv(url)

# Define acknowledgment columns
ack_columns = ['ack_gesture', 'ack_speak', 'ack_look', 'ack_smile']

# Calculate acknowledgment score as the count of True values in the acknowledgment columns
df['ack_score'] = df[ack_columns].sum(axis=1)

# Output paths
csv_output_path = 'data/raw/other/vote_offs/log.csv'
json_output_path = 'data/raw/other/vote_offs/log.json'

# Save to CSV
df.to_csv(csv_output_path, index=False)

# Save to JSON
df.to_json(json_output_path, orient='records', lines=False, indent=4)

print(f"Data saved to {csv_output_path} and {json_output_path}")
