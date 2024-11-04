import pandas as pd
from datetime import datetime, timedelta

# Load CSV file
df = pd.read_csv('events.csv')

# Replace NaN values with 0
df.fillna(0, inplace=True)

# Convert relevant columns to integers
for column in df.columns[3:]:
    df[column] = df[column].apply(lambda x: int(x) if str(x).isdigit() else 0)

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce', dayfirst=True)

# Prompt user to select categories
print("Available categories:")
categories = df.columns[3:]
for i, category in enumerate(categories):
    print(f"{i + 1}. {category}")

selected_indices = []
while True:
    user_input = input("Enter the number of the category you want to select (or 0 to finish): ")
    if user_input == '0':
        break
    try:
        index = int(user_input.strip()) - 1
        if 0 <= index < len(categories):
            selected_indices.append(index)
        else:
            print("Invalid selection, please try again.")
    except ValueError:
        print("Invalid input, please enter a number.")

selected_categories = categories[selected_indices]

# Ask the user for AND or OR filtering
print("Choose the filtering logic:")
print("1. AND (all selected categories)")
print("2. OR (any selected category)")
filter_choice = input("Enter 1 for AND or 2 for OR: ").strip()

# Determine filter type based on user input
urls = df['URL']
if filter_choice == '1':
    # AND logic
    selected_urls = urls[(df[selected_categories] > 0).all(axis=1)]
else:
    # OR logic
    selected_urls = urls[(df[selected_categories] > 0).any(axis=1)]

# Ask the user to filter by date
print("Date filtering options:")
print("1. All dates")
print("2. Past year")
print("3. This calendar year")
print("4. Past 3 months")
print("5. Past month")
print("6. Enter a date range")
date_choice = input("Select a date filter option (1-6): ").strip()

# Get the current date for dynamic date range calculations
current_date = datetime.now()

# Filter based on the selected date option
if date_choice == '2':  # Past year
    start_date = current_date - timedelta(days=365)
    selected_urls = selected_urls[df['Date'] >= start_date]

elif date_choice == '3':  # This calendar year
    start_date = datetime(current_date.year, 1, 1)
    selected_urls = selected_urls[df['Date'] >= start_date]

elif date_choice == '4':  # Past 3 months
    start_date = current_date - timedelta(days=90)
    selected_urls = selected_urls[df['Date'] >= start_date]

elif date_choice == '5':  # Past month
    start_date = current_date - timedelta(days=30)
    selected_urls = selected_urls[df['Date'] >= start_date]

elif date_choice == '6':  # Custom date range
    start_date = input("Enter the start date (DD-MM-YYYY): ").strip()
    end_date = input("Enter the end date (DD-MM-YYYY): ").strip()
    try:
        start_date = pd.to_datetime(start_date, format="%d-%m-%Y")
        end_date = pd.to_datetime(end_date, format="%d-%m-%Y")
        selected_urls = selected_urls[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    except ValueError:
        print("Invalid date format. Please use DD-MM-YYYY.")

# Write selected URLs to theSelected.txt
with open('theSelected.txt', 'w') as file:
    for url in selected_urls:
        file.write(f"{url}\n")

print("The URLs have been written to theSelected.txt")

