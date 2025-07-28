#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install openai')

import openai

# ==== STEP 1: Set your OpenAI API key ====
openai.api_key = "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"  # Replace with your key from https://platform.openai.com/account/api-keys

# ==== STEP 2: User enters a topic ====
topic = input("Enter your YouTube video topic (e.g. Gym, Gaming, Finance): ")

# ==== STEP 3: Generate Title + Thumbnail Text ====
prompt = f"""
You are an expert YouTube content strategist. 
Give me a viral YouTube video title and short thumbnail text for this topic:
"{topic}"

Return it like:
Title: ...
Thumbnail Text: ...
"""

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # or use "gpt-4" if you have access
    messages=[{"role": "user", "content": prompt}],
    temperature=0.9,
    max_tokens=100
)

output = response.choices[0].message.content

