import json

# Step 1: Read the data from your training JSON file
with open("training_data.json", "r", encoding="utf-8") as f:
    training_data = json.load(f)

# Step 2: Extract question titles and answers into separate lists
input_data = [entry["title"] for entry in training_data]
output_data = [entry["answer"] for entry in training_data]  # These will all be "ANSWER HERE" for now

# Step 3: Combine them into a dictionary
output_data_dict = [{"title": input_data[i], "answer": output_data[i]} for i in range(len(input_data))]

# Step 4: Save the combined data to a new JSON file
with open("output_data.json", "w", encoding="utf-8") as f:
    json.dump(output_data_dict, f, indent=4)

print("Data has been saved to output_data.json")
