#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install openai')

import openai

openai.api_key = "sk-..."  # Paste your OpenAI API key here

# Set the custom personality
personality = "You are a sarcastic gym bro who never breaks character."

# User prompt
user_input = "How do I get abs?"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": personality},
        {"role": "user", "content": user_input}
    ]
)

reply = response['choices'][0]['message']['content']
print("🤖 Bot says:\n")
print(reply)


# In[ ]:




