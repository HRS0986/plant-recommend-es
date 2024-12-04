import streamlit as st
from experta import Fact, KnowledgeEngine, MATCH

# Import the existing expert system and facts
from inference_engine import GardeningExpertSystem, PlantFact
from facts import plants

def main():
    st.title("🌱 Garden Plant Recommender")

    # Sidebar for input parameters
    st.sidebar.header("Plant Selection Criteria")

    # Sunlight options
    sunlight = st.sidebar.selectbox(
        "Sunlight Preference",
        ["Full", "Partial", "Shade"]
    )

    # Soil options
    soil = st.sidebar.selectbox(
        "Soil Type",
        ["Well-drained", "Clay", "Sandy", "Loamy"]
    )

    # Water requirement
    water = st.sidebar.selectbox(
        "Water Requirement",
        ["Low", "Moderate", "High"]
    )

    # Flowering preference
    flowering = st.sidebar.selectbox(
        "Flowering Preference",
        ["Any", "Yes", "No"]
    )

    # Humidity
    humidity = st.sidebar.selectbox(
        "Humidity Level",
        ["Low", "Medium", "High"]
    )

    # Recommend button
    if st.sidebar.button("Find Plants"):
        # Create the expert system
        engine = GardeningExpertSystem(plants)

        # Reset and declare facts
        engine.reset()
        engine.declare(PlantFact(
            sunlight=sunlight,
            soil=soil,
            water=water,
            flowering=flowering,
            humidity=humidity
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

        # Display results
        st.subheader("Recommended Plants")

        # Capture and parse markdown results
        markdown_results = result.getvalue()
        st.markdown(markdown_results if markdown_results.strip() else "No plants match your criteria.")

    # Specific Plant Lookup
    st.sidebar.header("Specific Plant Lookup")
    specific_plant = st.sidebar.text_input("Enter Plant Name")

    if st.sidebar.button("Look Up Plant"):
        if specific_plant:
            # Create the expert system
            engine = GardeningExpertSystem(plants)

            # Reset and declare facts
            engine.reset()
            engine.declare(PlantFact(name=specific_plant))

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
            st.subheader(f"Details for {specific_plant}")
            markdown_results = result.getvalue()
            st.markdown(markdown_results if markdown_results.strip() else f"No information found for {specific_plant}.")

if __name__ == "__main__":
    main()