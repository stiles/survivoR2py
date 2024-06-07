
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

"""
VOTE OFF REACTION LOGS
How did contestants respond after their torch was doused? 
"""

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQfmJJvr0TdW6fZ-wDdTadFDY5wTm2S6cnr9-n2D3cS6-eRGbIySzVokY97bON66_BXDIc0jnSjch82/pub?gid=0&single=true&output=csv'

df = pd.read_csv(url)

df.to_csv('data/raw/other/vote_offs/log.csv', index=False)