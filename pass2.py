import json

def read_json_file(file_path):
    """
    Reads a JSON file and returns a list of dictionaries containing its content.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        list: A list of dictionaries containing the JSON data.
    """
    try:
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        print("File not found:", file_path)
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON from file:", file_path)
        return []

# Example usage:
file_path = "data.json"
intermediateList = read_json_file(file_path)
print(intermediateList) 
