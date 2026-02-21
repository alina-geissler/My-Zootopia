import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')


def print_information(data):
    for animal in data:
        print(f"Name: {animal["name"]}")
        diet = animal["characteristics"].get("diet")
        if diet:
            print(f"Diet: {diet}")
        locations = animal["locations"]
        if locations:
            print(f"Location: {locations[0]}")
        animal_type = animal["characteristics"].get("type")
        if animal_type:
            print(f"Type: {animal_type}")
        print()



def main():
    print_information(animals_data)


if __name__ == "__main__":
    main()