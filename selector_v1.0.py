import pandas as pd

# Load CSV file
df = pd.read_csv('events.csv')

# Replace NaN values with 0
df.fillna(0, inplace=True)

# Convert relevant columns to integers
for column in df.columns[3:]:
    df[column] = df[column].apply(lambda x: int(x) if str(x).isdigit() else 0)

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

# Filter URLs based on selected categories
urls = df['URL']
selected_urls = urls[df[selected_categories].sum(axis=1) > 0]

# Write selected URLs to theSelected.txt
with open('theSelected.txt', 'w') as file:
    for url in selected_urls:
        file.write(f"{url}\n")

print("The URLs have been written to theSelected.txt")

