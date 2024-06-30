import csv

def read_file(filename: str) -> list[dict]:
    with open(filename) as file:
        res_data = list(csv.DictReader(file))

    for data in res_data:
        data["floor_count"] = int(data["floor_count"])
        data["population"] = int(data["population"])
        data["heating_value"] = float(data["heating_value"])
        data["area_residential"] = float(data["area_residential"])
    return res_data


def classify_house(floor_count: int) -> str:
    if not isinstance(floor_count, int):
        raise TypeError("Количество этажей должно быть целым числом.")
    if floor_count <= 0:
        raise ValueError("Количество этажей должно быть положительным целым числом.")
    if floor_count <= 5:
        return "Малоэтажный"
    elif floor_count > 5 and floor_count <= 16:
        return "Среднеэтажный"
    else:
        return "Многоэтажный"


def get_classify_houses(houses: list[dict]) -> list[str]:
    return [classify_house(house["floor_count"]) for house in houses]


def get_count_house_categories(categories: list[str]) -> dict[str, int]:
    category_counts = {}
    for category in categories:
        if category not in category_counts:
            category_counts[category] = 0
        category_counts[category] += 1
    return category_counts


def min_area_residential(houses: list[dict]) -> str:
    min_house = min(houses, key=lambda house: house["area_residential"] / house["population"])
    return min_house["house_address"]


if __name__ == "__main__":
    houses_filename = "housing_data.csv"
    houses_data = read_file(houses_filename)

    house_categories = get_classify_houses(houses_data)
    count_categories = get_count_house_categories(house_categories)
    print(count_categories)

    house_address = min_area_residential(houses_data)
    print(house_address)
