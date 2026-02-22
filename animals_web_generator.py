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


def serialize_animal(animal_obj):
    """
    Create HTML card element for an animal
    :param animal_obj: information to use for card element
    :return: HTML code for card element
    """
    output = ''
    output += '<li class="cards__item">\n'
    output += f'<div class="card__title">{animal_obj["name"]}</div>\n'
    output += '<p class="card__text">'
    diet = animal_obj['characteristics'].get('diet')
    if diet:
        output += f'<strong>Diet:</strong> {diet}<br/>\n'
    locations = animal_obj['locations']
    if locations:
        output += f'<strong>Location:</strong> {locations[0]}<br/>\n'
    habitat = animal_obj['characteristics'].get('habitat')
    if habitat:
        output += f'<strong>Habitat:</strong> {habitat}<br/>\n'
    animal_type = animal_obj['characteristics'].get('type')
    if animal_type:
        output += f'<strong>Type:</strong> {animal_type}<br/>\n'
    skin_type = animal_obj['characteristics'].get('skin_type')
    if skin_type:
        output += f'<strong>Skin:</strong> {skin_type}<br/>\n'
    color = animal_obj['characteristics'].get('color')
    if color:
        output += f'<strong>Color:</strong> {color}<br/>\n'
    output += '</p>\n'
    output += '</li>\n'
    return output


output = ''
for animal_obj in animals_data:
    output += serialize_animal(animal_obj)

html_with_data = template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w") as handle:
    handle.write(html_with_data)


