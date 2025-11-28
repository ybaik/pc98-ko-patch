import json


def main():
    with open("./list.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # Check statistics
    stat = dict()
    for k, v in data.items():
        persons = v.get("localization", "").split(",")
        for p in persons:
            if p not in stat:
                stat[p] = 1
            else:
                stat[p] += 1

    stat = dict(sorted(stat.items(), key=lambda item: item[1], reverse=True))
    print(f"Total: {len(data.keys())}")
    for i, (k, v) in enumerate(stat.items()):
        print(f"{i:02d}: {k} ({v})")

    # Check list for a person
    person = "낭만엘리"
    titles = []
    for k, v in data.items():
        if person in v.get("localization", ""):
            titles.append(k)
    print(f"{person}'s works:")
    for i, t in enumerate(titles, start=1):
        print(f"{i:02d}: {t}")

    with open("list.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4, sort_keys=True)


if __name__ == "__main__":
    main()
