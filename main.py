import streamlit as st

# Import the existing expert system and facts
from inference_engine import GardeningExpertSystem, PlantFact
from facts import plants

def main():
    # Set page config (e.g., wider layout)
    st.set_page_config(page_title="🌱 Urban Gardening Expert", layout="wide")

    # Custom styling for background and text colors
    st.markdown(
        """
        <style>
        /* App background color */
        .stApp {
            background-color: #f0f8e8;  /* Light greenish background */
        }

        /* Sidebar styling */
        .sidebar .sidebar-content {
            background-color: #e8f5e9;  /* Light green background for sidebar */
            color: #388e3c;  /* Dark green text */
        }

        /* Title and header font color */
        h1, h2, h3, h4, h5, .st-subheader {
            color: #2c6e2f;  /* Dark green text */
        }

        /* Input fields styling */
        .stTextInput input, .stButton button {
            background-color: #ffffff;  /* White background for input fields */
            color: #2c6e2f;  /* Dark green font color */
        }

        /* Markdown text (outputs) */
        .stMarkdown, .stText {
            color: #333333;  /* Dark gray text for better readability */
        }
        
        div[data-testid="stSidebarCollapseButton"] {
            display: none;
        }

        /* Plant-specific input fields (color distinction) */
        .stTextInput input:focus {
            border-color: #76b041;  /* Focused input border in light green */
        }
        
        .stAppHeader {
            display: none;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    # Title with a gardening touch
    st.markdown(
        "<h1 style='text-align:center;'>🌿 Urban Gardening Expert 🌿</h1>",
        unsafe_allow_html=True
    )

    # Sidebar with gardening-friendly colors
    st.sidebar.markdown(
        "<h2 style='color:#388e3c;'>What kind of plant are you looking for?</h2>",
        unsafe_allow_html=True
    )

    # Input fields
    sunlight = st.sidebar.text_input(
        "🌞 How much sunlight does your space get throughout the day? (Full, Medium, Low)",
    )

    soil = st.sidebar.text_input(
        "🌱 What kind of soil do you typically have in your gardening area or yard? (Well-drained, Sandy, Loam, Rich, Moist)",
    )

    water = st.sidebar.text_input(
        "💧 How much water does your plant need to thrive? (Low, Moderate, High)",
    )

    flowering = st.sidebar.text_input(
        "🌸 Are you looking for a plant that flowers, or do you prefer a non-flowering plant? (Any, Yes, No)",
    )

    humidity = st.sidebar.text_input(
        "💨 How humid is the environment where you plan to keep your plant? (Low, Medium, High)",
    )

    # Recommend button with a nature-inspired color
    if st.sidebar.button("Find Plants", key="recommend"):
        # Create the expert system
        engine = GardeningExpertSystem(plants)

        # Reset and declare facts
        engine.reset()
        engine.declare(PlantFact(
            sunlight=sunlight.strip().lower(),
            soil=soil.strip().lower(),
            water=water.strip().lower(),
            flowering=flowering.strip().lower(),
            humidity=humidity.strip().lower()
        ))

        # Capture output
        import sys
        from io import StringIO

        # Redirect stdout to capture print statements
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result

        # Run the expert system
        engine.run()

        # Restore stdout
        sys.stdout = old_stdout

        # Capture and parse markdown results
        markdown_results = result.getvalue()
        st.markdown(markdown_results if markdown_results.strip() else "No plants match your criteria.")

    # Specific Plant Lookup Section
    st.sidebar.markdown(
        "<h2 style='color:#388e3c;'>Want to know about a plant?</h2>",
        unsafe_allow_html=True
    )

    specific_plant = st.sidebar.text_input("🌿 Enter Plant Name")

    if st.sidebar.button("Find Details", key="lookup"):
        if specific_plant:
            # Create the expert system
            engine = GardeningExpertSystem(plants)

            # Reset and declare facts
            engine.reset()
            engine.declare(PlantFact(name=specific_plant.strip()))

            # Capture output
            import sys
            from io import StringIO

            # Redirect stdout to capture print statements
            old_stdout = sys.stdout
            result = StringIO()
            sys.stdout = result

            # Run the expert system
            engine.run()

            # Restore stdout
            sys.stdout = old_stdout

            # Display results
            markdown_results = result.getvalue()
            st.markdown(f"###### Here are some details about {specific_plant}. If you're planning to plant a {specific_plant} in your garden, make sure the environment meets the following conditions")
            st.markdown(markdown_results if markdown_results.strip() else f"No information found for {specific_plant}.")

if __name__ == "__main__":
    main()
