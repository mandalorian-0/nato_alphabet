import pandas as pd

# Read the NATO phonetic alphabet CSV
try:
    nato_phonetic = pd.read_csv("nato_phonetic_alphabet.csv")
except FileNotFoundError:
    print("Error: The file 'nato_phonetic_alphabet.csv' was not found. Please ensure it's in the correct directory.")
    exit(1)

# Create a dictionary mapping letters to codes
nato_phonetic_dict = {row.letter: row.code for _, row in nato_phonetic.iterrows()}

# Validate and process user input
name = input("Enter your name: ").strip()

# Handle empty or whitespace-only input
if not name:
    print("No name entered. Exiting.")
    exit(0)

# Convert each character to NATO phonetic code, skipping non-alphabetic characters
name_to_nato_phonetic = []

for letter in name:
    if letter.isalpha():
        upper_letter = letter.upper()
        if upper_letter in nato_phonetic_dict:
            name_to_nato_phonetic.append(nato_phonetic_dict[upper_letter])
        else:
            print(f"Warning: '{letter}' is not a valid letter in the NATO phonetic alphabet and has been skipped.")
    else:
        print(f"Warning: '{letter}' is not a letter and has been skipped.")

# Output the result
if name_to_nato_phonetic:
    print("NATO phonetic codes:", name_to_nato_phonetic)
else:
    print("No valid letters found in the input.")
