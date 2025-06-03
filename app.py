import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("Cocktail Assistant 🍸")
st.write("Get a unique tequila or mezcal cocktail recipe based on what’s behind the bar.")

ingredients = st.text_input("Enter available ingredients (comma-separated):")

if st.button("Generate Cocktail"):
    if ingredients:
        with st.spinner("Shaking things up..."):
            prompt = f"""
            You are an expert bartender at an agave-focused cocktail bar. Based on these ingredients, suggest a cocktail using tequila or mezcal. 
            Include a fun name, ingredients, instructions, and a short customer-friendly description.

            Available: {ingredients}
            """

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7
            )

            st.subheader("Here’s Your Cocktail:")
            st.write(response['choices'][0]['message']['content'])
    else:
        st.warning("Please enter some ingredients.")
