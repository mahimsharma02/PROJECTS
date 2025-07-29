#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Mood dataset
data = {
    'mood': [
        'I am feeling happy', 'I am sad', 'feeling energetic', 'feeling low',
        'I am relaxed', 'angry and frustrated', 'super excited', 'bored and lazy',
        'I feel peaceful', 'I am anxious', 'I feel motivated', 'I feel depressed'
    ],
    'category': [
        'happy', 'sad', 'energetic', 'sad',
        'relaxed', 'angry', 'energetic', 'bored',
        'relaxed', 'anxious', 'motivated', 'depressed'
    ]
}

df = pd.DataFrame(data)

# ML Pipeline
model = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])
model.fit(df['mood'], df['category'])

# Song suggestion dictionary
song_recommendations = {
    'happy': ['Happy – Pharrell Williams', 'Can’t Stop the Feeling – Justin Timberlake'],
    'sad': ['Someone Like You – Adele', 'Fix You – Coldplay'],
    'energetic': ['Stronger – Kanye West', 'Eye of the Tiger – Survivor'],
    'relaxed': ['Weightless – Marconi Union', 'Sunflower – Post Malone'],
    'angry': ['Numb – Linkin Park', 'Break Stuff – Limp Bizkit'],
    'bored': ['Blinding Lights – The Weeknd', 'Radioactive – Imagine Dragons'],
    'anxious': ['Let It Be – The Beatles', 'Breathe Me – Sia'],
    'motivated': ['Till I Collapse – Eminem', 'The Champion – Carrie Underwood'],
    'depressed': ['1-800-273-8255 – Logic', 'Creep – Radiohead']
}

# User input
user_input = input("How are you feeling today?\n>> ")
predicted_category = model.predict([user_input])[0]
songs = song_recommendations.get(predicted_category, [])

# Output
print(f"\nMood detected: {predicted_category.upper()}")
print("Recommended Songs:")
for song in songs:
    print(f"🎵 {song}")


# In[ ]:




