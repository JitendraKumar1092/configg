import json
import random

# Open the JSONL file
with open('shop.jsonl', 'r') as file:
    lines = file.readlines()

# Shuffle the lines to randomize the data
random.shuffle(lines)

# Calculate 20% of the total lines for evaluation
eval_lines = int(0.2 * len(lines))

# Extract the evaluation data
eval_data = lines[:eval_lines]

# Write the evaluation data to a new JSONL file
with open('shop_validation.jsonl', 'w') as file:
    file.writelines(eval_data)

print("Evaluation data extracted successfully!")
