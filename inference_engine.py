from experta import Rule, KnowledgeEngine, MATCH
from facts import PlantFact

# Expert system engine
class GardeningExpertSystem(KnowledgeEngine):
    def __init__(self, knowledge_base):
        super().__init__()
        self.knowledge_base = knowledge_base  # Reference to the knowledge base
        self.recommended_plants = []

    # Rule: Exact match for plant recommendations
    @Rule(
        PlantFact(
            sunlight=MATCH.sunlight,
            soil=MATCH.soil,
            water=MATCH.water,
            flowering=MATCH.flowering,
            humidity=MATCH.humidity,
        ),
        salience=10,
    )
    def exact_match(self, sunlight, soil, water, flowering, humidity):
        self.recommended_plants = [
            plant for plant in self.knowledge_base
            if sunlight in plant["sunlight"]
               and soil in plant["soil"]
               and water == plant["water"]
               and (flowering == "Any" or flowering == plant["flowering"])
               and humidity == plant["humidity"]
        ]
        if self.recommended_plants:
            print("\nFound matching plants:")
            for plant in self.recommended_plants:
                print(PlantFact.get_plant_info(plant))

    # Rule: Suggest alternatives based on partial matches
    @Rule(
        PlantFact(sunlight=MATCH.sunlight, soil=MATCH.soil, water=MATCH.water, flowering=MATCH.flowering, humidity=MATCH.humidity),
        salience=5,
    )
    def suggest_alternatives(self, sunlight, soil, water, flowering, humidity):
        if not self.recommended_plants:
            alternatives = []
            for plant in self.knowledge_base:
                relevance_score = 0
                # Match sunlight
                if sunlight in plant["sunlight"]:
                    relevance_score += 1
                # Match soil type
                if soil in plant["soil"]:
                    relevance_score += 1
                # Match water requirement
                if water == plant["water"]:
                    relevance_score += 1
                if humidity == plant["humidity"]:
                    relevance_score += 1
                # Match flowering preference
                if flowering == "Any" or flowering == plant["flowering"]:
                    relevance_score += 1
                if relevance_score > 0:
                    alternatives.append((plant, relevance_score))
            alternatives.sort(key=lambda x: x[1], reverse=True)

            print("\nNo exact matches found. Alternative recommendations:")
            for plant, score in alternatives[:3]:
                print(f"{PlantFact.get_plant_info(plant, score)}")

    # Rule: Backward chaining to find plants for specific conditions
    @Rule(PlantFact(name=MATCH.name), salience=8)
    def backward_chaining(self, name):
        matches = [p for p in self.knowledge_base if p["name"].lower() == name.lower()]
        if matches:
            print(PlantFact.get_plant_info(matches[0]))
        else:
            print(f"No plant found with the name '{name}'.")