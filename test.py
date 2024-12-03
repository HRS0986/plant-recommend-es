from experta import Fact, Rule, KnowledgeEngine, MATCH

# Define a Fact class for books
class BookFact(Fact):
    title = str
    category = str
    author = str
    keywords = list
    rating = float
    target_audience = str
    language = str
    book_type = str

# Expert system engine
class LibraryExpertSystem(KnowledgeEngine):
    def __init__(self, knowledge_base):
        super().__init__()
        self.knowledge_base = knowledge_base  # Reference to the knowledge base
        self.inferred_books = []
        self.alternatives = []

    # Rule: Match exact book parameters
    @Rule(
        BookFact(
            category=MATCH.category,
            author=MATCH.author,
            target_audience=MATCH.target_audience,
            language=MATCH.language,
            book_type=MATCH.book_type,
        ),
        salience=10,  # High priority for exact matches
    )
    def exact_match(self, category, author, target_audience, language, book_type):
        self.inferred_books = [
            book for book in self.knowledge_base
            if book.category == category and
            book.author == author and
            book.target_audience == target_audience and
            book.language == language and
            book.book_type == book_type
        ]
        if self.inferred_books:
            print("\nExact Matches Found:")
            for book in self.inferred_books:
                print(book)

    # Rule: Suggest alternatives based on partial matches
    # @Rule(
    #     BookFact(keywords=MATCH.keywords, rating=MATCH.rating),
    #     salience=5,  # Medium priority for partial matches
    # )
    # def suggest_alternatives(self, keywords, rating):
    #     self.alternatives = [
    #         (book, len(set(keywords).intersection(book.keywords)), book.rating)
    #         for book in self.knowledge_base
    #         if book.rating >= rating - 0.5 and book.rating <= rating + 0.5
    #     ]
    #     self.alternatives.sort(key=lambda x: (-x[1], abs(x[2] - rating)))  # Sort by relevance
    #     if not self.inferred_books:
    #         print("\nNo exact matches found. Alternative recommendations:")
    #         for alt, relevance, _ in self.alternatives[:3]:
    #             print(f"{alt} (Relevance Score: {relevance})")


    @Rule(
        BookFact(keywords=MATCH.keywords, category=MATCH.category, target_audience=MATCH.target_audience, language=MATCH.language, rating=MATCH.rating),
        salience=5,
    )
    def suggest_alternatives(self, keywords, category, target_audience, language, rating):
        self.alternatives = []

        for book in self.knowledge_base:
            relevance_score = 0

            # Calculate relevance score
            # Match keywords
            relevance_score += len(book.keywords.intersection(keywords))

            # Match rating with tolerance
            if book.rating >= rating - 0.5 and book.rating <= rating + 0.5:
                relevance_score += 1

            # Match category, target audience, and language
            if book.category == category:
                relevance_score += 5
            if book.target_audience == target_audience:
                relevance_score += 1
            if book.language == language:
                relevance_score += 1

            # Add book to alternatives if relevance score > 0
            if relevance_score > 0:
                self.alternatives.append((book, relevance_score))

        # Sort by relevance score in descending order
        self.alternatives.sort(key=lambda x: x[1], reverse=True)

        # If no exact matches, suggest top alternatives
        if not self.inferred_books:
            print("\nNo exact matches found. Alternative recommendations:")
            for alt, relevance in self.alternatives[:3]:  # Limit to top 3 recommendations
                print(f"{alt} (Relevance Score: {relevance})")




    # Rule: Backward chaining to find book category
    @Rule(BookFact(title=MATCH.title), salience=8)
    def backward_chaining_category(self, title):
        matching_books = [book for book in self.knowledge_base if book.title.lower() == title.lower()]
        if matching_books:
            book = matching_books[0]
            print(f"\nBackward Chaining Result for '{title}':")
            print(f"Category: {book.category}")
            print(book)
        else:
            print(f"No book found with the title '{title}'.")

# Define Book class as per initial structure
class Book:
    def __init__(self, title, category, author, keywords, rating, target_audience, language, book_type):
        self.title = title
        self.category = category
        self.author = author
        self.keywords = set(keywords)
        self.rating = rating
        self.target_audience = target_audience
        self.language = language
        self.book_type = book_type

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Category: {self.category}, Rating: {self.rating}, Target Audience: {self.target_audience}, Language: {self.language}, Type: {self.book_type}"

# Knowledge base with 10 books
knowledge_base = [
    Book("The Great Adventure", "Fiction", "John Doe", ["adventure", "mystery"], 4.5, "Adults", "English", "Paperback"),
    Book("Learning Python", "Technology", "Mark Smith", ["programming", "python", "coding"], 4.7, "Beginners", "English", "Hardcover"),
    Book("AI for Everyone", "Technology", "Andrew Ng", ["AI", "artificial intelligence", "machine learning"], 4.8, "Adults", "English", "Paperback"),
    Book("The Joy of Cooking", "Cooking", "Julia Child", ["cooking", "recipes", "food"], 4.6, "Adults", "English", "Hardcover"),
    Book("The Silent World of Nicholas Quinn", "Mystery", "Colin Dexter", ["mystery", "detective", "suspense"], 4.2, "Adults", "English", "Paperback"),
    Book("The Psychology of Learning", "Psychology", "Sigmund Freud", ["psychology", "learning", "behavior"], 4.4, "Adults", "English", "Paperback"),
    Book("The Hobbit", "Fantasy", "J.R.R. Tolkien", ["fantasy", "adventure", "dragons"], 4.9, "Teens", "English", "Hardcover"),
    Book("JavaScript Essentials", "Technology", "David Flanagan", ["programming", "javascript", "web development"], 4.3, "Intermediate", "English", "Paperback"),
    Book("Cooking with Love", "Cooking", "Rachel Ray", ["cooking", "easy recipes", "family meals"], 4.5, "Family", "English", "Paperback"),
    Book("Deep Learning", "Technology", "Ian Goodfellow", ["AI", "deep learning", "neural networks"], 4.9, "Advanced", "English", "Hardcover"),
]

# Instantiate and populate the expert system
engine = LibraryExpertSystem(knowledge_base)

# Start forward chaining with user inputs
user_params = BookFact(
    category="Technology",
    author="Andrew Ng",
    keywords=["AI", "machine learning","recipes"],
    rating=4.5,
    target_audience="Adults",
    language="English",
    book_type="Paperback"
)

# Forward chaining for matching books
print("\n--- Forward Chaining ---")
engine.reset()
engine.declare(user_params)
engine.run()

# Backward chaining for a book title
print("\n--- Backward Chaining ---")
engine.reset()
engine.declare(BookFact(title="AI for Everyone"))
engine.run()
