from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def get_cocktail_suggestion(ingredients):
    prompt = (
        f"You are a world-class bartender. Based on the following ingredients: {ingredients}, "
        f"If the user shares ingredients, suggest a classic cocktail. The cocktail should not have more than four ingrediaents. Include the name, ingredients with measurements, and instructions. If they do not include ingredients, tell them 'real ingredients needed'"
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
