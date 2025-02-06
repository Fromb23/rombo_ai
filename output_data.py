import json

# Save the data to a new JSON file
output_data_dict = [{"title": input_data[i], "answer": output_data[i]} for i in range(len(input_data))]

# Specify the file name where you want to save
with open("output_data.json", "w", encoding="utf-8") as f:
    json.dump(output_data_dict, f, indent=4)

print("Data has been saved to output_data.json")
