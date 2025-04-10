import tkinter as tk
from tkinter import messagebox

# Sample recipes data (name, ingredients)
recipes = [
    {"name": "Spaghetti Bolognese", "ingredients": ["spaghetti", "ground beef", "tomato sauce", "onion", "garlic"]},
    {"name": "Chicken Salad", "ingredients": ["chicken", "lettuce", "tomato", "cucumber", "olive oil"]},
    {"name": "Vegetable Stir Fry", "ingredients": ["broccoli", "carrot", "tofu", "soy sauce", "ginger"]},
    {"name": "Grilled Cheese Sandwich", "ingredients": ["bread", "cheese", "butter"]},
    {"name": "Tuna Wrap", "ingredients": ["tuna", "wrap", "lettuce", "mayo"]},
    {"name": "Pancakes", "ingredients": ["flour", "milk", "eggs", "syrup"]},
    {"name": "Rice and Beans", "ingredients": ["rice", "black beans", "onion", "garlic"]},
    {"name": "Chicken Curry", "ingredients": ["chicken", "curry powder", "onion", "coconut milk"]},
    {"name": "Omelette", "ingredients": ["eggs", "cheese", "spinach"]},
    {"name": "Beef Tacos", "ingredients": ["taco shells", "ground beef", "lettuce", "cheese", "salsa"]},
    {"name": "Tomato Soup", "ingredients": ["tomatoes", "onion", "garlic", "cream"]},
]

# Create main window
root = tk.Tk()
root.title("🍽️ Recipe Finder & Meal Planner 🍴")
root.geometry("800x600")
root.configure(bg="#f4e1d2")  # peach background

# Days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Store meal plan variables
meal_plan_vars = []

# Frames for different pages
main_frame = tk.Frame(root, bg="#f4e1d2")
meal_timetable_frame = tk.Frame(root, bg="#f4e1d2")
shopping_list_frame = tk.Frame(root, bg="#f4e1d2")

def show_main_page():
    meal_timetable_frame.pack_forget()
    shopping_list_frame.pack_forget()
    main_frame.pack(fill="both", expand=True)

def show_meal_timetable():
    update_meal_plan()
    main_frame.pack_forget()
    shopping_list_frame.pack_forget()
    meal_timetable_frame.pack(fill="both", expand=True)

def show_shopping_list():
    generate_shopping_list()
    main_frame.pack_forget()
    meal_timetable_frame.pack_forget()
    shopping_list_frame.pack(fill="both", expand=True)

# Update Meal Plan
def update_meal_plan():
    meal_plan_text = ""
    for i, var in enumerate(meal_plan_vars):
        recipe = var.get()
        if recipe:
            meal_plan_text += f"{days[i]}: {recipe}\n"
        else:
            meal_plan_text += f"{days[i]}: No recipe selected\n"
    meal_plan_label.config(text=meal_plan_text)

# Generate Shopping List
def generate_shopping_list():
    shopping_list = set()
    for var in meal_plan_vars:
        recipe_name = var.get()
        if recipe_name:
            recipe = next((r for r in recipes if r["name"] == recipe_name), None)
            if recipe:
                shopping_list.update(recipe["ingredients"])
    if shopping_list:
        shopping_text = "\n".join(sorted(shopping_list))
        shopping_list_label.config(text=f"🛒 Shopping List:\n\n{shopping_text}")
    else:
        shopping_list_label.config(text="❌ No recipes selected yet!")

# ------------------ MAIN FRAME ------------------
title_label = tk.Label(main_frame, text="🍽️ Meal Planner", font=("Helvetica", 20, "bold"), fg="#6a4c9c", bg="#f4e1d2")
title_label.pack(pady=20)

# Frame for days and dropdowns
meal_entry_frame = tk.Frame(main_frame, bg="#f4e1d2")
meal_entry_frame.pack(pady=10)

# Add meal dropdowns
for i, day in enumerate(days):
    label = tk.Label(meal_entry_frame, text=day, font=("Helvetica", 12), fg="#6a4c9c", bg="#f4e1d2")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")

    var = tk.StringVar()
    dropdown = tk.OptionMenu(meal_entry_frame, var, *[r["name"] for r in recipes])
    dropdown.config(bg="#fbeee6", fg="#6a4c9c", font=("Helvetica", 11))
    dropdown.grid(row=i, column=1, padx=10, pady=5, sticky="w")
    meal_plan_vars.append(var)

# Buttons below the form
update_button = tk.Button(main_frame, text="✅ Update Meal Plan", font=("Helvetica", 12, "bold"), bg="#6a4c9c", fg="white", command=update_meal_plan)
update_button.pack(pady=10)

# Navigation buttons (left corner)
nav_frame = tk.Frame(main_frame, bg="#f4e1d2")
nav_frame.place(x=10, y=10)

timetable_btn = tk.Button(nav_frame, text="🗓️ Meal Timetable", font=("Helvetica", 10, "bold"), bg="#d9b8ff", fg="#4b0082", command=show_meal_timetable)
timetable_btn.pack(pady=5, anchor="w")

shopping_btn = tk.Button(nav_frame, text="🛒 Shopping List", font=("Helvetica", 10, "bold"), bg="#ffb3ab", fg="#a02b43", command=show_shopping_list)
shopping_btn.pack(pady=5, anchor="w")

# ------------------ MEAL TIMETABLE FRAME ------------------
meal_timetable_title = tk.Label(meal_timetable_frame, text="🍽️ Weekly Meal Timetable", font=("Helvetica", 24, "bold"), fg="#6a4c9c", bg="#f4e1d2")
meal_timetable_title.pack(pady=30)

meal_plan_card = tk.Frame(meal_timetable_frame, bg="#fff0f5", bd=2, relief="ridge", padx=20, pady=20)
meal_plan_card.pack(padx=30, pady=10, fill="both", expand=True)

meal_plan_label = tk.Label(meal_plan_card, text="📅 Your Meal Plan will appear here", font=("Helvetica", 14), fg="#6a4c9c", bg="#fff0f5", justify="left", anchor="nw")
meal_plan_label.pack(anchor="nw")

back_button_1 = tk.Button(meal_timetable_frame, text="↩️ Back to Main", font=("Helvetica", 14, "bold"), bg="#ff9a8b", fg="white", command=show_main_page)
back_button_1.pack(pady=25)

# ------------------ SHOPPING LIST FRAME ------------------
shopping_title = tk.Label(shopping_list_frame, text="🛍️ Shopping List", font=("Helvetica", 24, "bold"), fg="#6a4c9c", bg="#f4e1d2")
shopping_title.pack(pady=30)

shopping_list_label = tk.Label(shopping_list_frame, text="🛒 Shopping List will appear here", font=("Helvetica", 14), fg="#6a4c9c", bg="#f4e1d2", justify="left")
shopping_list_label.pack(pady=10)

back_button_2 = tk.Button(shopping_list_frame, text="↩️ Back to Main", font=("Helvetica", 14, "bold"), bg="#ff9a8b", fg="white", command=show_main_page)
back_button_2.pack(pady=25)

# Start with main page
main_frame.pack(fill="both", expand=True)

root.mainloop()




