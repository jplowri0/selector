import pandas as pd

# Read DataFrame from the CSV file
df = pd.read_csv('events.csv')

# Display numbered list of header items (categories)
print("Categories:")
for i, category in enumerate(df.columns[3:]):
    print(f"{i + 1}. {category}")

# Select categories
selected_categories = []
while True:
    try:
        category_choice = int(input("Enter the number of the category to select (0 to stop): "))
        if category_choice == 0:
            break
        elif 1 <= category_choice <= len(df.columns[3:]):
            selected_categories.append(df.columns[2 + category_choice])
        else:
            print("Invalid choice. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Filter DataFrame based on selected categories (logical AND)
filtered_df = df[df[selected_categories].eq(1).all(axis=1)]

# Output to theSelected.txt
output_file_path = 'theSelected.txt'
with open(output_file_path, 'w') as output_file:
    # Redirect print to the file
    print("Selected URLs:", file=output_file)
    if not filtered_df.empty:
        for url in filtered_df['URL'].tolist():
            print(url, file=output_file)
    else:
        print("No matching rows found.", file=output_file)

# Inform the user
print(f"Output written to {output_file_path}")

