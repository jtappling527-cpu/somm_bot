import streamlit as st

# --- LOGIC ENGINE ---


def get_recommendation(drink_choice, vibe, food_choice=None):
    # One master dictionary - No .update() needed
    recommendations = {
        "old fashioned": {
            "upscale": "Lyre's American Malt with alcohol-free bitters and an expressed orange peel.",
            "casual": "Strong ginger ale with a dash of bitters and a maraschino cherry.",
        },
        "margarita": {
            "upscale": "Agave-Lime Shrub: 1oz Agave nectar, 1oz fresh lime, a splash of Verjus for acidity, topped with sparkling water and a salt rim.",
            "casual": "Fresh lime juice, agave syrup, and a pinch of sea salt shaken and topped with club soda.",
        },
        "gin & tonic": {
            "upscale": "Wilderton Lustre (Botanical Distillate) with Fever-Tree Mediterranean Tonic and a bruised sprig of rosemary.",
            "casual": "High-quality Tonic water with a 'Shrub' (vinegar-based fruit syrup) like blackberry or grapefruit to mimic the botanical bite.",
        },
        "dark and stormy": {
            "upscale": "Blackberry & Balsamic Shrub topped with spicy ginger beer. The balsamic provides the 'funk' and depth usually found in dark rum.",
            "casual": "Ginger ale with a squeeze of lime and a drop of molasses for that dark, rich color and flavor.",
        },
        "ipa": {
            "upscale": "Athletic Brewing 'Free Wave' Hazy IPA. It nailed the Amarillo and Citra hop profile.",
            "casual": "Lagunitas IPNA. It has that classic piney, bitter punch you expect from a West Coast IPA.",
        },
        "pilsner": {
            "upscale": "Untitled Art 'Italian Style Pils'. Super crisp, high carbonation, and very clean.",
            "casual": "Heineken 0.0. It’s light, accessible, and tastes exactly like the original skunky pilsner.",
        },
        "stout": {
            "upscale": "Bravus Brewing Oatmeal Stout. Rich, chocolatey, and has the 'weight' a stout lover wants.",
            "casual": "Guinness 0. It is arguably the most successful 1-to-1 alcohol-free swap on the market.",
        },
        "whiskey_coke": {
            "upscale": "Free Spirits 'The Spirit of Bourbon'. Its strong vanilla and toasted oak notes stand up perfectly to the sweetness of a premium cola.",
            "casual": "Ritual Zero Proof Whiskey Alternative. It has a smoky sweetness that blends seamlessly with Coke.",
        },
        "whiskey_ginger": {
            "upscale": "Spiritless Kentucky 74 with a splash of ginger syrup. The oaky bite mimics the classic 'Highball' heat.",
            "casual": "Kentucky 74 or a dash of Apple Cider Vinegar in Ginger Ale for that fermented 'kick'.",
        },
    }

    food_pairings = {
        "steak": "A deep, tannic build: Pomegranate juice (unsweetened) mixed with a splash of cold-brew coffee and balsamic glaze to mimic a heavy Cabernet.",
        "sushi": "A crisp, high-acid build: Sparkling water with a Yuzu or Grapefruit extract and a touch of rice vinegar for that sharp, clean finish.",
        "spicy thai": "A cooling, floral build: Lemongrass-infused simple syrup with club soda and a dash of coconut water.",
        "oysters": "A saline, mineral build: Verjus (unfermented grape juice) topped with chilled sparkling mineral water and a twist of lemon.",
        "pizza": "A 'Bistro Red' build: Tart cherry juice diluted with sparkling water and a pinch of dried oregano. The acidity cuts right through the cheese and fats.",
        "burger": "The 'Draft Pour': A chilled Guinness 0 or a malty NA Stout. The roasted barley notes complement the charred beef.",
        "tacos": "The 'Agave Sharp': Fresh lime juice, club soda, and a tiny dash of liquid smoke or habanero bitters to mimic a Mezcal Paloma.",
        "dessert": "A 'Nightcap' build: Cold brew coffee, a splash of almond milk, and a dash of cinnamon—perfect for chocolate or creamy sweets.",
    }

    # Normalize input
    drink_choice = drink_choice.lower()

    # Handling shorthand
    if "cab" in drink_choice:
        drink_choice = "cabernet sauvignon"
    elif "pinot" in drink_choice:
        drink_choice = "pinot noir"
    elif "whiskey" in drink_choice or "whisky" in drink_choice:
        if "coke" in drink_choice or "cola" in drink_choice:
            drink_choice = "whiskey_coke"
        elif "ginger" in drink_choice:
            drink_choice = "whiskey_ginger"
        else:
            drink_choice = "whiskey"
    elif "ipa" in drink_choice:
        drink_choice = "ipa"
    elif "pilsner" in drink_choice or "lager" in drink_choice or "beer" in drink_choice:
        drink_choice = "pilsner"
    elif "stout" in drink_choice or "guinness" in drink_choice:
        drink_choice = "stout"

    # Get the drink recommendation
    drink_rec = recommendations.get(drink_choice, {}).get(
        vibe, "I'm still curating that alternative, but a Bitters & Soda is a classic."
    )

    # Get the food pairing if provided
    food_rec = None
    if food_choice:
        food_choice = food_choice.lower()
        for key in food_pairings:
            if key in food_choice:
                food_rec = food_pairings[key]
                break

    return drink_rec, food_rec


# --- STREAMLIT UI ---
st.set_page_config(page_title="Sober Sommelier", page_icon="🍷")
# --- BOUTIQUE HOTEL STYLING ---
st.markdown("""
  <style>
    /* 1. Define Theme Variables */
    :root {
        --burgundy: #2e0101;
        --gold: #d4af37;
        --cream: #fdf5e6;
        --dark-accent: #3d0202;
    }

    /* 2. Global App Styling */
    .stApp {
        background-color: var(--burgundy);
        color: var(--cream);
    }
    
    .block-container {
        max-width: 800px;
        padding-top: 2rem;
    }

    /* 3. Grouped Typography (Reduced Lines) */
    h1, h2, h3, .footer, .stTextInput label, .stSelectbox label {
        color: var(--gold) !important;
        font-family: 'Playfair Display', serif;
        text-align: center;
    }

    h1, h2, h3 {
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    /* 4. Input Fields */
    .stTextInput input {
        background-color: var(--dark-accent) !important;
        color: var(--cream) !important;
        border: 1px solid var(--gold) !important;
    }

    /* 5. Button Logic (Consolidated) */
    div.stButton > button {
        background-color: var(--gold);
        color: var(--burgundy);
        border: 2px solid #b8860b;
        border-radius: 0px;
        font-weight: bold;
        width: 100%;
        margin-top: 20px;
        transition: 0.3s; /* Smoother hover effect */
    }
    
    div.stButton > button:hover {
        background-color: var(--cream);
        color: var(--burgundy);
    }

    /* 6. Footer */
    .footer {
        font-size: 0.8rem;
        margin-top: 50px;
        border-top: 1px solid var(--gold);
        padding-top: 20px;
    }

</style>
    """, unsafe_allow_html=True)

# --- STREAMLIT UI ---
# Symbols to choose from: 🎷 | 🎀 | 👔 | 🛎️ | 🕯️ | 🍴
st.title("⚜️ THE SOBER SOMMELIER") 
st.subheader("ALCOHOL-FREE PAIRINGS")

st.markdown("<p style='text-align: center;'>Tell me what you usually enjoy, and what you're eating.</p>", unsafe_allow_html=True)

# Ensure this block only appears ONCE in your script to avoid the "Duplicate Element" error
col1, col2 = st.columns(2)
with col1:
    user_drink = st.text_input("What do you usually drink?", placeholder="e.g. Cabernet, Old Fashioned...", key="drink_input")
with col2:
    user_vibe = st.selectbox("What's the vibe?", ["upscale", "casual"], key="vibe_input")

user_food = st.text_input("What are you eating? (Optional)", placeholder="e.g. Steak, Sushi...", key="food_input")

if st.button("Get Recommendation"):
    if user_drink:
        with st.spinner('Consulting the cellar...'):
            drink_result, food_result = get_recommendation(user_drink, user_vibe, user_food)
            
            st.success("**Your Sommelier Recommends:**")
            st.write(drink_result)
            
            if food_result:
                st.divider()
                st.subheader("🍴 Food Pairing")
                st.write(food_result)
    else:
        st.warning("Please enter a drink so I can help you!")


# --- FOOTER (Replacing the Sidebar) ---
st.markdown("""
    <div class="footer">
        <p>Curated by a certified sommelier specializing in high-end non-alcoholic viticulture and mixology.<br>
    </div>
    """, unsafe_allow_html=True)


