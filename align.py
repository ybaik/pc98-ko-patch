import json


def main():
    with open("./list.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # Check statistics
    stat = dict()
    for k, v in data.items():
        if v["localization"] not in stat:
            stat[v["localization"]] = 1
        else:
            stat[v["localization"]] += 1

    stat = dict(sorted(stat.items(), key=lambda item: item[1], reverse=True))
    print(stat)
    print(f"Total: {len(data.keys())}")

    with open("list.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4, sort_keys=True)


if __name__ == "__main__":
    main()
