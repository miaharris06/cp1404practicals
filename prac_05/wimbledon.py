INDEX_CHAMPION = 2
INDEX_COUNTRY = 1


def main():
    records = extract_data()
    champion_to_wins, countries = process_data(records)
    display_data(champion_to_wins, countries)


def display_data(champion_to_wins, countries):
    print("Wimbledon Champions: ")
    for name, wins in champion_to_wins.items():
        print(name, wins)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


def process_data(records):
    countries = set()
    champion_to_wins = {}
    for record in records:
        countries.add(record[INDEX_COUNTRY])
        try:
            champion_to_wins[record[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_to_wins[record[INDEX_CHAMPION]] = 1
    return countries


def extract_data():
    records = []
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            data = line.strip().split(",")
            records.append(data)
    return records


main()
