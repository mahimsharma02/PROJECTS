#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install openai')

import openai

# Paste your OpenAI API key here
openai.api_key = ""

def generate_resume_summary(name, skills, role):
    prompt = f"""
    Generate a professional resume summary for {name} who is applying for the role of {role}. 
    Skills: {skills}. Keep it under 100 words.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

def generate_cover_letter(name, role, company, skills):
    prompt = f"""
    Write a short and personalized cover letter for {name} applying for the role of {role} at {company}. 
    Highlight these skills: {skills}.
    Keep it under 150 words and make it sound human, confident, and professional.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

# === USER INPUT ===
name = input("Enter your name: ")
skills = input("Enter your skills (comma separated): ")
role = input("Enter job role: ")
company = input("Enter target company: ")

print("\n--- Resume Summary ---\n")
print(generate_resume_summary(name, skills, role))

print("\n--- Cover Letter ---\n")
print(generate_cover_letter(name, role, company, skills))

