import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')


def load_template(file_path):
    """ Loads an HTML template """
    with open(file_path, "r") as handle:
        return handle.read()


template = load_template("animals_template.html")

# create a string with the animal data
output = ''

for animal in animals_data:
    output += '<li class="cards__item">\n'
    output += f'<div class="card__title">{animal["name"]}</div>\n'
    output += '<p class="card__text">'
    diet = animal['characteristics'].get('diet')
    if diet:
        output += f'<strong>Diet:</strong> {diet}<br/>\n'
    locations = animal['locations']
    if locations:
        output += f'<strong>Location:</strong> {locations[0]}<br/>\n'
    animal_type = animal['characteristics'].get('type')
    if animal_type:
        output += f'<strong>Type:</strong> {animal_type}<br/>\n'
    output += '</p>\n'
    output += '</li>\n'


html_with_data = template.replace("__REPLACE_ANIMALS_INFO__", output)
print(html_with_data)

with open("animals.html", "w") as handle:
    handle.write(html_with_data)
