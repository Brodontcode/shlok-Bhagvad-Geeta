import random

import requests

import textwrap

import pickle

master=[]

# Function to align text to restrict to 80 words per line
def align_text(text):
    """
    Aligns the given text to restrict to 80 words per line.
    """
    wrapped_text = textwrap.wrap(text, width=80)
    aligned_text = '\n'.join(f'{line:{80}}' for line in wrapped_text)
    return aligned_text

# Generate random chapter and verse numbers
#chapter = random.randint(1, 18)
#verses = 0

# Determine the number of verses in the selected chapter
v=[47,72,43,42,29,47,30,28,34,42,55,20,35,27,20,24,28,78]
for chapter in range(1,19):
    for verses in range(v[chapter-1]):
        try:
            # Construct the URL for the Bhagavad Gita API
            url = f"https://bhagavad-gita3.p.rapidapi.com/v2/chapters/{chapter}/verses/{verses}/"

            headers = {
                "X-RapidAPI-Key": "14c1a49a87mshfce8345f77f3c8dp1339bbjsn8ebe0f5af81d",
                "X-RapidAPI-Host": "bhagavad-gita3.p.rapidapi.com"
            }

            # Make a GET request to the API
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                # Extract the verse text and other information from the response
                verse_data = response.json()
                verse = verse_data["text"]
                transliteration = verse_data["transliteration"]
                translation = align_text(verse_data["translations"][0]['description'])
                # Print the selected verse
                master.append([f"{chapter}.{verses}",verse,transliteration,translation])
                
        except requests.exceptions.RequestException as e:
            # Handle any exceptions that occur during the API request
            print("Error occurred:", e)
    print(chapter)
with open("Bhagwat gita.txt","wb") as file:
    pickle.dump(master,file)
