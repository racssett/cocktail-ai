from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def get_cocktail_suggestion(ingredients):
    prompt = f"""
    You are an expert bartender at a modern agave-focused cocktail bar. Based on the following available ingredients, suggest one creative cocktail recipe using tequila or mezcal. 

    Please include:
    - A creative cocktail name
    - Ingredient list with measurements
    - Preparation instructions
    - A brief, customer-friendly description
    
    Use only the ingredients listed, or suggest close substitutions if something key is missing.

    

    Available ingredients: {ingredients}
    """

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=0.7
)

st.subheader("Here’s Your Cocktail:")
st.write(response.choices[0].message.content)

# --- Run it ---
if __name__ == "__main__":
    print("Welcome to the Agave Assistant 🍹")
    ingredients = input("Enter a list of available ingredients (comma-separated):\n")
    recipe = get_cocktail_suggestion(ingredients)
    print("\nSuggested Cocktail:\n")
    print(recipe)
