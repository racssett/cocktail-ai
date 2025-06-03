import streamlit as st
from suggestions import get_cocktail_suggestion

st.set_page_config(page_title="Agave Cocktail Assistant", page_icon="🍹")

st.title("🍸 Cocktail Suggestion Tool")
st.write("Enter a list of ingredients (comma-separated), and get a custom cocktail recipe!")

ingredients = st.text_input("Ingredients (e.g. tequila, lime, agave):")

if ingredients:
    with st.spinner("Shaking up something delicious..."):
        try:
            recipe = get_cocktail_suggestion(ingredients)
            st.subheader("Here’s Your Cocktail:")
            st.write(recipe)
        except Exception as e:
            st.error(f"Something went wrong: {e}")
