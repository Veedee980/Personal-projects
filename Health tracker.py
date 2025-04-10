import csv
import os
from datetime import datetime
from colorama import Fore, Back, Style, init
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas

# Initialize colorama
init(autoreset=True)

# File to store data
FILE_NAME = "health_tracker.csv"
PDF_FILE = "health_summary.pdf"

# Initialize the CSV file with headers if it doesn't exist
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Exercise", "Duration (min)", "Calories", "Water (liters)"])

# Function to log data
def log_data(exercise, duration, calories, water):
    date = datetime.now().strftime("%Y-%m-%d")
    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, exercise, duration, calories, water])

# Function to display summary in terminal
def display_summary():
    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            print(Back.BLUE + Fore.WHITE + "\n📊 Health Tracker Summary:\n")
            for row in reader:
                print(
                    Fore.CYAN +
                    f"📅 Date: {row[0]}\n"
                    f"🏋️ Exercise: {row[1]}\n"
                    f"⏱️ Duration: {row[2]} min\n"
                    f"🔥 Calories: {row[3]} kcal\n"
                    f"💧 Water: {row[4]} liters\n"
                    + "-" * 40
                )
    except FileNotFoundError:
        print(Fore.RED + "🚫 No data found. Start logging your health activities!")

# Function to export to a beautiful, styled PDF
def export_to_pdf():
    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)

            c = canvas.Canvas(PDF_FILE, pagesize=letter)
            width, height = letter

            # Header banner
            c.setFillColor(colors.HexColor("#4B0082"))  # Indigo
            c.rect(0, height - 100, width, 100, fill=1)
            c.setFillColor(colors.white)
            c.setFont("Helvetica-Bold", 20)
            c.drawString(50, height - 60, "🏋️ Health Tracker Summary Report")
            c.setFont("Helvetica", 12)
            c.drawString(50, height - 80, f"Exported on: {datetime.now().strftime('%Y-%m-%d %H:%M')}")

            # Table starting position
            y = height - 130
            row_height = 22
            col_spacing = [50, 140, 240, 360, 460]  # X positions

            # Draw column headers
            c.setFillColor(colors.black)
            c.setFont("Helvetica-Bold", 12)
            for i, header in enumerate(headers):
                c.drawString(col_spacing[i], y, header)
            y -= row_height

            # Draw data rows
            c.setFont("Helvetica", 11)
            row_num = 0
            for row in reader:
                if y < 80:
                    c.showPage()
                    y = height - 50
                if row_num % 2 == 0:
                    c.setFillColorRGB(0.95, 0.95, 1)  # Light purple
                    c.rect(45, y - 4, width - 90, row_height, fill=1, stroke=0)
                c.setFillColor(colors.black)
                for i, item in enumerate(row):
                    c.drawString(col_spacing[i], y, str(item))
                y -= row_height
                row_num += 1

            # Footer
            c.setFont("Helvetica-Oblique", 10)
            c.setFillColor(colors.gray)
            c.drawString(50, 30, "Generated with Health Tracker 💪")

            c.save()
            print(Fore.GREEN + f"\n✅ Beautiful PDF report saved as: {PDF_FILE}\n")

    except FileNotFoundError:
        print(Fore.RED + "🚫 No data to export. Please log some entries first.")

# Header in terminal
def show_header():
    print(Back.MAGENTA + Fore.WHITE + "\n💪 Welcome to Your Health Tracker App 💪\n")

# Main menu
def main():
    initialize_file()
    while True:
        show_header()
        print(Fore.YELLOW + "Please select an option:")
        print(Fore.GREEN + "[1] ➕ Log Today's Activity")
        print(Fore.BLUE + "[2] 📖 View Health Summary")
        print(Fore.CYAN + "[3] 📄 Export to PDF")
        print(Fore.RED + "[4] ❌ Exit\n")

        choice = input(Fore.YELLOW + "Your choice: ")

        if choice == "1":
            print(Back.GREEN + Fore.BLACK + "\nLet's log today's activity!\n")
            exercise = input(Fore.CYAN + "🏋️ Type of Exercise: ")
            duration = input(Fore.CYAN + "⏱️ Duration (in minutes): ")
            calories = input(Fore.CYAN + "🔥 Calories Burned: ")
            water = input(Fore.CYAN + "💧 Water Consumed (in liters): ")
            log_data(exercise, duration, calories, water)
            print(Fore.GREEN + "\n✅ Data logged successfully!\n")
        elif choice == "2":
            display_summary()
        elif choice == "3":
            export_to_pdf()
        elif choice == "4":
            print(Fore.MAGENTA + "\n👋 Exiting Health Tracker. Stay active and hydrated!\n")
            break
        else:
            print(Fore.RED + "⚠️ Invalid choice. Please enter 1, 2, 3, or 4.\n")

if __name__ == "__main__":
    main()


