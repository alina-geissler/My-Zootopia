import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')


def load_template(file_path):
    """ Loads an HTML template """
    with open(file_path, "r") as handle:
        return handle.read()


template = load_template("animals_template.html")

# create a string with the animal data
output = ""

for animal in animals_data:
    output += f"Name: {animal["name"]}\n"
    diet = animal["characteristics"].get("diet")
    if diet:
        output += f"Diet: {diet}\n"
    locations = animal["locations"]
    if locations:
        output += f"Location: {locations[0]}\n"
    animal_type = animal["characteristics"].get("type")
    if animal_type:
        output += f"Type: {animal_type}\n"


html_with_data = template.replace("__REPLACE_ANIMALS_INFO__", output)
print(html_with_data)

with open("animals.html", "w") as handle:
    handle.write(html_with_data)
