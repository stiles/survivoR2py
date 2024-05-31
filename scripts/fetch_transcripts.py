import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

"""
SURVIVOR TRANSCRIPTS
Fetch each transcript url from a directory page
https://subslikescript.com/series/Survivor-239195
Go to each transcritp and grab the transcript
Capture what was said after "The tribe has spoken"
Put it all in a dataframe and store it 
"""

# Function to get a list of episode transcript urls
def get_filtered_urls(base_url):
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    urls = []

    # For loop that iterates over all the <li> tags
    for h in soup.findAll('li'):
        # looking for anchor tag inside the <li>tag
        a = h.find('a')
        try:
            # looking for href inside anchor tag
            if 'href' in a.attrs:
                # storing the value of href in a separate variable
                url = "https://subslikescript.com" + a.get('href')
                # appending the url to the output list
                urls.append(url)
        # if the list does not have an anchor tag or an anchor tag does not have a href params we pass
        except:
            pass

    # Filter URLs that contain both "series" and "season"
    filtered_urls = [url for url in urls if 'series' in url and 'season' in url]
    return filtered_urls

# Function to fetch and extract the full transcript from the URL
def fetch_transcript(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    transcript_div = soup.find('div', class_='full-script')
    if transcript_div:
        transcript = transcript_div.get_text(separator="\n").strip()
        return transcript
    return ""

# Function to extract lines following "The tribe has spoken"
def extract_post_voteoff_lines(transcript, num_lines=3):
    lines = transcript.split('\n')
    for i, line in enumerate(lines):
        if "The tribe has spoken" in line:
            # Capture subsequent lines
            post_voteoff_lines = lines[i:i+num_lines+1]
            return " ".join(post_voteoff_lines).strip()
    return ""

# Get the urls from the main page 
base_url = 'https://subslikescript.com/series/Survivor-239195'
filtered_urls = get_filtered_urls(base_url)

# Create a DataFrame
df = pd.DataFrame(filtered_urls, columns=['url'])

# Extract season, episode, and title
df[['season', 'episode', 'title']] = df['url'].str.extract(r'season-(\d+)/episode-(\d+)-(.+)', expand=True)

# Clean the title by replacing underscores with spaces
df['title'] = df['title'].str.replace('_', ' ')

# Convert season and episode to integers
df['season'] = df['season'].astype(int)
df['episode'] = df['episode'].astype(int)

# Fetch transcripts with progress bar
tqdm.pandas()
df['transcript'] = df['url'].progress_apply(fetch_transcript)

# Extract post-voteoff lines
df['post_voteoff_lines'] = df['transcript'].apply(lambda x: extract_post_voteoff_lines(x, num_lines=3))

# Display the resulting DataFrame
print(df[['season', 'episode', 'title', 'post_voteoff_lines']])

# Optional: save to CSV
df.to_csv('survivor_transcripts.csv', index=False)
df.to_json('survivor_transcripts.csv', indent=4, lines=False, orient='records')