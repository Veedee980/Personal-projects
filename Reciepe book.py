from fpdf import FPDF

class Recipe:
    def __init__(self, name, ingredients, steps, cuisine=None, meal_type=None):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps
        self.cuisine = cuisine
        self.meal_type = meal_type

class RecipeBook:
    def __init__(self):
        self.recipes = []
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)

    # Add recipe to the book
    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    # Generate the PDF with all recipes
    def generate_pdf(self, filename="recipe_book.pdf"):
        self.pdf.add_page()
        self.pdf.set_font("Arial", 'B', 16)
        self.pdf.cell(200, 10, "Recipe Book", ln=True, align='C')
        self.pdf.ln(10)  # Line break

        for recipe in self.recipes:
            self.pdf.add_page()
            self.pdf.set_font("Arial", 'B', 14)
            self.pdf.cell(200, 10, recipe.name, ln=True, align='C')
            self.pdf.ln(5)

            self.pdf.set_font("Arial", '', 12)
            if recipe.cuisine:
                self.pdf.cell(200, 10, f"Cuisine: {recipe.cuisine}", ln=True)
            if recipe.meal_type:
                self.pdf.cell(200, 10, f"Meal Type: {recipe.meal_type}", ln=True)
            self.pdf.ln(5)

            self.pdf.cell(200, 10, "Ingredients:", ln=True)
            self.pdf.set_font("Arial", '', 10)
            for ingredient in recipe.ingredients:
                self.pdf.cell(200, 10, f"- {ingredient}", ln=True)
            self.pdf.ln(5)

            self.pdf.set_font("Arial", '', 12)
            self.pdf.cell(200, 10, "Preparation Steps:", ln=True)
            self.pdf.multi_cell(0, 10, recipe.steps)
            self.pdf.ln(10)

        self.pdf.output(filename)
        print(f"Recipe book saved as '{filename}'")

# Create a RecipeBook instance
recipe_book = RecipeBook()

# Sample recipes
recipe1 = Recipe(
    "Spaghetti Bolognese",
    ["Spaghetti", "Ground Beef", "Tomato Sauce", "Garlic", "Onion", "Olive Oil", "Parmesan"],
    "1. Cook spaghetti according to package instructions.\n2. In a pan, cook ground beef with chopped garlic and onion.\n3. Add tomato sauce and let simmer for 10 minutes.\n4. Serve the sauce over the spaghetti and sprinkle with parmesan.",
    cuisine="Italian",
    meal_type="Dinner"
)

recipe2 = Recipe(
    "Vegetable Stir Fry",
    ["Broccoli", "Carrots", "Bell Peppers", "Soy Sauce", "Ginger", "Garlic", "Olive Oil"],
    "1. Heat olive oil in a pan.\n2. Add chopped garlic and ginger, stir-fry for 1 minute.\n3. Add the vegetables and stir-fry until tender.\n4. Add soy sauce and cook for another 2 minutes.",
    cuisine="Asian",
    meal_type="Lunch"
)

# Add recipes to the recipe book
recipe_book.add_recipe(recipe1)
recipe_book.add_recipe(recipe2)

# Generate and save the PDF recipe book
recipe_book.generate_pdf("my_recipe_book.pdf")



