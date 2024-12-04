from experta import Fact


class PlantFact(Fact):
    name = str
    sunlight = list
    soil = list
    water = str
    flowering = str
    humidity = str

    @staticmethod
    def get_plant_info(plant, score = None):
        """
        Generate a markdown-formatted string of plant information
        """
        if score is not None:
            score = (score / 5) * 100
        return (
            f"### {plant['name']} {' - Relevance is '+str(score) + '%' if score is not None else ''}\n\n"
            f"- **Sunlight:** {' or '.join(plant['sunlight'])}\n"
            f"- **Soil Type:** {' or '.join(plant['soil'])}\n"
            f"- **Water Requirements:** {plant['water']}\n"
            f"- **Flowering:** {plant['flowering']}\n"
            f"- **Humidity:** {plant['humidity']}\n"
            f"---"
        )
    @staticmethod
    def get_reason_for_exact_match(plant):
        return (f"These are the best plants for your environment. Because, these plants also need,\n\n"
        f">> + {' or '.join(plant['sunlight'])} sunlight \n\n"
        f">> + {' or '.join(plant['soil'])} soil type\n\n"
        f">> + {plant['water']} level of water\n\n"
        f">> + {plant['humidity']} humidity level")


plants = (
    PlantFact(name="Basil", sunlight=["Full"], soil=["Well-drained", "Loam"], water="Moderate", flowering="No",
              humidity="Medium"),
    PlantFact(name="Mint", sunlight=["Medium"], soil=["Moist", "Rich"], water="High", flowering="Yes", humidity="High"),
    PlantFact(name="Thyme", sunlight=["Full"], soil=["Well-drained", "Sandy"], water="Low", flowering="Yes",
              humidity="Low"),
    PlantFact(name="Marigolds", sunlight=["Full"], soil=["Well-drained", "Loam"], water="Moderate", flowering="Yes",
              humidity="Low to Medium"),
    PlantFact(name="Rosemary", sunlight=["Full"], soil=["Well-drained", "Loam"], water="Low", flowering="Yes",
              humidity="Low"),
    PlantFact(name="Parsley", sunlight=["Medium"], soil=["Moist"], water="Moderate", flowering="No", humidity="Medium"),
    PlantFact(name="Petunias", sunlight=["Full"], soil=["Well-drained"], water="Moderate", flowering="Yes",
              humidity="Medium"),
    PlantFact(name="Geraniums", sunlight=["Full", "Medium"], soil=["Well-drained"], water="Moderate", flowering="Yes",
              humidity="Medium"),
    PlantFact(name="Impatiens", sunlight=["Medium"], soil=["Moist"], water="High", flowering="Yes", humidity="High"),
    PlantFact(name="Snake Plant", sunlight=["Low"], soil=["Well-drained", "Loam"], water="Low", flowering="No",
              humidity="Low"),
    PlantFact(name="Spider Plant", sunlight=["Medium"], soil=["Well-drained"], water="Moderate", flowering="No",
              humidity="Medium"),
    PlantFact(name="Zanzibar Gem", sunlight=["Low", "Medium"], soil=["Well-drained"], water="Low",
              flowering="No", humidity="Low"),
    PlantFact(name="Peace Lily", sunlight=["Low", "Medium"], soil=["Moist"], water="Moderate", flowering="Yes",
              humidity="High"),
    PlantFact(name="Lavender", sunlight=["Full"], soil=["Sandy"], water="Low", flowering="Yes", humidity="Low"),
    PlantFact(name="Aloe Vera", sunlight=["Full"], soil=["Well-drained", "Sandy"], water="Low", flowering="Yes",
              humidity="Low"),
    PlantFact(name="Pothos", sunlight=["Low", "Medium"], soil=["Standard", "Potting Mix"], water="Moderate",
              flowering="No", humidity="Medium"),
    PlantFact(name="Rose", sunlight=["Full"], soil=["Well-drained"], water="Moderate", flowering="Yes",
              humidity="Medium"),
    PlantFact(name="Begonias", sunlight=["Medium"], soil=["Well-drained"], water="Moderate", flowering="Yes",
              humidity="Medium"),
    PlantFact(name="Cactus", sunlight=["Full"], soil=["Sandy", "Well-drained"], water="Low", flowering="Yes",
              humidity="Low"),
    PlantFact(name="Zinnias", sunlight=["Full"], soil=["Well-drained", "Loam"], water="Moderate", flowering="Yes",
              humidity="Medium"),
)
