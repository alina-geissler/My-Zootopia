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
    output += f'<div class="card__title" style="margin: 20;">{animal_obj["name"]}</div>\n'
    output += '<div class="card__text">\n'
    output += '<ul style="list-style-type:none;">\n'
    diet = animal_obj['characteristics'].get('diet')
    if diet:
        output += f'<li><strong>Diet:</strong> {diet}</li>\n'
    locations = animal_obj['locations']
    if locations:
        output += f'<li><strong>Location:</strong> {locations[0]}<li/>\n'
    habitat = animal_obj['characteristics'].get('habitat')
    if habitat:
        output += f'<li><strong>Habitat:</strong> {habitat}<li/>\n'
    animal_type = animal_obj['characteristics'].get('type')
    if animal_type:
        output += f'<li><strong>Type:</strong> {animal_type}<li/>\n'
    skin_type = animal_obj['characteristics'].get('skin_type')
    if skin_type:
        output += f'<li><strong>Skin:</strong> {skin_type}<li/>\n'
    color = animal_obj['characteristics'].get('color')
    if color:
        output += f'<li><strong>Color:</strong> {color}<li/>\n'
    output += '</ul>\n'
    output += '</div>\n'
    output += '</li>\n'
    return output


def select_skin_type(animals_data):
    """
    Let user decide which animals should appear on the website.
    :param animals_data: information about all animals
    :return: selected skin type
    """
    skin_types = list(set([animal["characteristics"].get("skin_type") for animal in animals_data]))
    while True:
        skin_type = input(f"Choose between {skin_types} or leave blank for all animals: ").capitalize().strip()
        if skin_type in skin_types or skin_type == "":
            return skin_type
        else:
            print("Please select an available type.")


def create_html_file(skin_type):
    """
    Generate HTML file based on user choice.
    :param skin_type: type selected by user
    """
    if skin_type == "":
        output = ''
        for animal_obj in animals_data:
            output += serialize_animal(animal_obj)
        html_with_data = template.replace("__REPLACE_ANIMALS_INFO__", output)
        with open("animals.html", "w") as handle:
            handle.write(html_with_data)
    else:
        output = ''
        for animal_obj in animals_data:
            if animal_obj["characteristics"].get("skin_type") == skin_type:
                output += serialize_animal(animal_obj)
        html_with_data = template.replace("__REPLACE_ANIMALS_INFO__", output)
        with open("animals.html", "w") as handle:
            handle.write(html_with_data)


def main():
    """
    Execute the main program: greet user, get skin type input and generate HTML file accordingly.
    """
    print("Welcome to your Animal Repository Generator!\n")
    print("Please select the SKIN TYPE you want the animals on your website to have.")
    skin_type = select_skin_type(animals_data)
    create_html_file(skin_type)
    print("\nYour HTML file has been created!")


if __name__ == "__main__":
    main()







