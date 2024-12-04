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
            if sunlight in ",".join(plant["sunlight"]).lower()
               and soil in ",".join(plant["soil"]).lower()
               and water == plant["water"].lower()
               and (flowering == "Any".lower() or flowering == plant["flowering"].lower())
               and humidity == plant["humidity"].lower()
        ]
        if self.recommended_plants:
            print("\n\n\n##### These plants are good for your environment")
            for plant in self.recommended_plants:
                print(f">> + ##### {plant['name']}")
            print("---")
            print(PlantFact.get_reason_for_exact_match(self.recommended_plants[0]))

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
                if sunlight in ",".join(plant["sunlight"]).lower():
                    relevance_score += 1
                # Match soil type
                if soil in ",".join(plant["soil"]).lower():
                    relevance_score += 1
                # Match water requirement
                if water == plant["water"].lower():
                    relevance_score += 1
                if humidity == plant["humidity"].lower():
                    relevance_score += 1
                # Match flowering preference
                if flowering == "Any".lower() or flowering == plant["flowering"].lower():
                    relevance_score += 1
                if relevance_score > 0:
                    alternatives.append((plant, relevance_score))
            alternatives.sort(key=lambda x: x[1], reverse=True)

            print(f"\n###### Sorry, it seems there are no plants fit for your needs. But these plant may be fit for your needs:")
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