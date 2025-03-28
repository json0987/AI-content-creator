"""
Author: [Your Name]  
Course: [Course Name]  
Assignment: [Assignment Name]  
Date: [Date]  

Description:
This program generates Instagram post content using OpenAI's API based on a user-defined theme.
It also integrates the Edamam API for nutrition analysis of generated recipes.
A simple UI is built using Streamlit for ease of use.
"""

import openai
import streamlit as st
import requests
import json

# Set API keys (replace with actual keys)
OPENAI_API_KEY = "your_openai_api_key"
EDAMAM_APP_ID = "your_edamam_app_id"
EDAMAM_APP_KEY = "your_edamam_app_key"

# OpenAI function to generate post content
def generate_content(theme):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an Instagram content creator."},
            {"role": "user", "content": f"Generate an engaging Instagram post about {theme}."}
        ],
        temperature=0.7,
        max_tokens=150
    )
    return response["choices"][0]["message"]["content"].strip()

# Edamam function to fetch nutrition details
def get_nutrition(ingredient):
    url = f"https://api.edamam.com/api/nutrition-data?app_id={EDAMAM_APP_ID}&app_key={EDAMAM_APP_KEY}&ingr={ingredient}"
    response = requests.get(url)
    data = response.json()
    if "calories" in data:
        return f"Calories: {data['calories']} kcal"
    return "Nutrition data unavailable."

# Streamlit UI
st.title("Instagram Content Creator AI")
theme = st.text_input("Enter your post theme (e.g., anime-inspired recipe, fitness tip):")

if st.button("Generate Post"):
    post_content = generate_content(theme)
    st.subheader("Generated Post:")
    st.write(post_content)

    if "recipe" in theme.lower():
        ingredient = st.text_input("Enter a key ingredient for nutrition analysis:")
        if st.button("Get Nutrition Info"):
            nutrition_info = get_nutrition(ingredient)
            st.subheader("Nutrition Info:")
            st.write(nutrition_info)

st.write("\n\n© [Your Name], [Year]")
