from experta import KnowledgeEngine, Rule, Fact

knowledge_base = [
    {
        "plant": "Basil",
        "sunlight": ["Full"],
        "soil": ["Well-drained", "loam"],
        "water": "Moderate",
        "flowering": "No",
        "humidity": "Medium"
    },
    {
        "plant": "Mint",
        "sunlight": ["Medium"],
        "soil": ["Moist", "rich"],
        "water": "High",
        "flowering": "Yes",
        "humidity": "High"
    },
    {
        "plant": "Thyme",
        "sunlight": ["Full"],
        "soil": ["Well-drained","sandy"],
        "water": "Low",
        "flowering": "Yes",
        "humidity": "Low"
    },
    {
        "plant": "Marigolds",
        "sunlight": ["Full"],
        "soil": ["Well-drained","loam"],
        "water": "Moderate",
        "flowering": "Yes",
        "humidity": "Low to Medium"
    },
    {
        "plant": "Rosemary",
        "sunlight": ["Full"],
        "soil": ["Well-drained", "loam"],
        "water": "Low",
        "flowering": "Yes",
        "humidity": "Low"
    },
    {
        "plant": "Parsley",
        "sunlight": ["Medium"],
        "soil": ["Moist"],
        "water": "Moderate",
        "flowering": "No",
        "humidity": "Medium"
    },
    {
        "plant": "Petunias",
        "sunlight": ["Full"],
        "soil": ["well-drained"],
        "water": "Moderate",
        "flowering": "Yes",
        "humidity": "Medium"
    },
    {
        "plant": "Geraniums",
        "sunlight": ["Full", "Medium"],
        "soil": ["Well-drained"],
        "water": "Moderate",
        "flowering": "Yes",
        "humidity": "Medium"
    },
    {
        "plant": "Impatiens",
        "sunlight": ["Medium"],
        "soil": ["Moist"],
        "water": "High",
        "flowering": "Yes",
        "humidity": "High"
    },
    {
        "plant": "Snake Plant",
        "sunlight": ["Low"],
        "soil": ["Well-drained","loam"],
        "water": "Low",
        "flowering": "No",
        "humidity": "Low"
    },
    {
        "plant": "Spider Plant",
        "sunlight": ["Medium"],
        "soil": ["Well-drained"],
        "water": "Moderate",
        "flowering": "No",
        "humidity": "Medium"
    },
    {
        "plant": "ZZ Plant (Zanzibar Gem)",
        "sunlight": ["Low", "Medium"],
        "soil": ["Well-drained"],
        "water": "Low",
        "flowering": "No",
        "humidity": "Low"
    },
    {
        "plant": "Peace Lily",
        "sunlight": ["Low", "Medium"],
        "soil": ["Moist"],
        "water": "Moderate",
        "flowering": "Yes",
        "humidity": "High"
    },
    {
        "plant": "Lavender",
        "sunlight": ["Full"],
        "soil": ["Sandy"],
        "water": "Low",
        "flowering": "Yes",
        "humidity": "Low"
    },
    {
        "plant": "Aloe Vera",
        "sunlight": ["Full"],
        "soil": ["Well-drained","sandy"],
        "water": "Low",
        "flowering": "Yes",
        "humidity": "Low"
    },
    {
        "plant": "Pothos",
        "sunlight": ["Low", "Medium"],
        "soil": ["Standard", "potting mix"],
        "water": "Moderate",
        "flowering": "No",
        "humidity": "Medium"
    },
    {
        "plant": "Rose",
        "sunlight": ["Full"],
        "soil": ["Well-drained"],
        "water": "Moderate",
        "flowering": "Yes",
        "humidity": "Medium"
    },
    {
        "plant": "Begonias",
        "sunlight": ["Medium"],
        "soil": ["well-drained"],
        "water": "Moderate",
        "flowering": "Yes",
        "humidity": "Medium"
    },
    {
        "plant": "Cactus",
        "sunlight": ["Full"],
        "soil": ["Sandy", "well-drained"],
        "water": "Low",
        "flowering": "Yes",
        "humidity": "Low"
    },
    {
        "plant": "Zinnias",
        "sunlight": ["Full"],
        "soil": ["Well-drained","loam"],
        "water": "Moderate",
        "flowering": "Yes",
        "humidity": "Medium"
    }
]

class InferenceEngine(KnowledgeEngine):
    @Rule(Fact(action='recommend'))
    def recommend_plants_procedural(self):
        """Step-by-step plant recommendation system."""

        # Step 1: Ask for Sunlight
        valid_sunlight = {sun for plant in knowledge_base for sun in plant["sunlight"]}
        while True:
            sunlight = input(f"Enter sunlight requirement ({', '.join(valid_sunlight)}): ").strip().capitalize()
            if sunlight in valid_sunlight:
                break
            print(f"Invalid input. Please choose from: {', '.join(valid_sunlight)}.")

        # Step 2: Ask for Soil Type
        valid_soil = {soil.lower() for plant in knowledge_base for soil in plant["soil"]}
        while True:
            soil = input(f"Enter soil type ({', '.join(valid_soil)}): ").strip().lower()
            if soil in valid_soil:
                break
            print(f"Invalid input. Please choose from: {', '.join(valid_soil)}.")

        # Step 3: Ask for Water Requirement
        valid_water = {plant["water"].lower() for plant in knowledge_base}
        while True:
            water = input(f"Enter water requirement ({', '.join(valid_water)}): ").strip().lower()
            if water in valid_water:
                break
            print(f"Invalid input. Please choose from: {', '.join(valid_water)}.")

        # Step 4: Ask for Flowering Preference (Optional)
        flowering = input("Do you prefer flowering plants? (Yes/No/Any): ").strip().capitalize()
        if flowering not in {"Yes", "No", "Any"}:
            flowering = "Any"

        # Step 5: Filter Plants
        filtered_plants = [
            plant for plant in knowledge_base
            if sunlight in plant["sunlight"]
               and soil in (s.lower() for s in plant["soil"])
               and water == plant["water"].lower()
               and (flowering == "Any" or flowering == ("Yes" if plant["flowering"] == "Yes" else "No"))
        ]

        # Step 6: Display Results
        if filtered_plants:
            print("\nRecommended plants:")
            for plant in filtered_plants:
                print(f"- {plant['plant']}")
        else:
            print("No plants match your criteria. Please adjust your inputs and try again.")

# Create an instance of the inference engine and run the recommendation process
engine = InferenceEngine()
engine.reset()
engine.declare(Fact(action='recommend'))
engine.run()