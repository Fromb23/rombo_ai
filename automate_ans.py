import json

# Load your scraped JSON data
with open("scraped.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Loop through all the data and add the "answer": "ANSWER HERE"
for item in data:
    # Set the default "answer" value
    item["answer"] = "ANSWER HERE"

# Save the updated data back to a new JSON file (training_data.json)
with open("training_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print("✅ All answers have been set to 'ANSWER HERE' automatically!")
