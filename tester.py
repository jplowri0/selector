import pandas as pd

# Load CSV file
df = pd.read_csv('events.csv')

# Replace NaN values with 0
df.fillna(0, inplace=True)

# Convert relevant columns to integers (debugging step added)
for column in df.columns[3:]:
    df[column] = df[column].apply(lambda x: int(x) if str(x).isdigit() else 0)
    print(f"Column '{column}' converted values: {df[column].unique()}")  # Debugging: print unique values after conversion

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
            if index not in selected_indices:
                selected_indices.append(index)
            else:
                print(f"Category '{categories[index]}' already selected.")
        else:
            print("Invalid selection, please try again.")
    except ValueError:
        print("Invalid input, please enter a number.")

# Get the selected categories by index
selected_categories = categories[selected_indices]
print(f"Selected categories: {selected_categories}")  # Debugging: print selected categories

# Filter URLs based on selected categories
urls = df['URL']
print(f"Data before filtering: \n{df[selected_categories].head()}")  # Debugging: Check if data looks correct

# Filter the rows where the sum of selected categories is greater than 0
selected_urls = urls[df[selected_categories].sum(axis=1) > 0]
print(f"Selected URLs based on categories: {selected_urls}")  # Debugging: print URLs that match

# Write selected URLs to theSelected.txt
with open('theSelected.txt', 'w') as file:
    for url in selected_urls:
        file.write(f"{url}\n")

print("The URLs have been written to theSelected.txt")

