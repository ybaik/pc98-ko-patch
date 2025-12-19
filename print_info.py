import json
from rich.console import Console
from rich.table import Table
from rich.text import Text


def get_target_keys(data: dict, developer_selection: list) -> list:
    out_list = list()
    for k, v in data.items():
        developer = v.get("developer", "N/A").lower()
        if len(developer_selection) and developer not in developer_selection:
            continue
        out_list.append(k)
    return out_list


def data_read(file_name: str, developer_selection: list) -> tuple[list, dict]:
    with open(file_name, "r", encoding="utf-8") as f:
        data = json.load(f)
        data_keys = get_target_keys(data, developer_selection)

    return data_keys, data


def put_data_to_table(
    key: str, data: dict, table: Table, developer_selection: list, stat: dict
):
    v = data[key]
    developer = v.get("developer", "N/A").lower()
    if len(developer_selection) and developer not in developer_selection:
        pass
    else:
        localization = v.get("localization", "N/A")

        persons = localization.replace("*", "").split(",")
        for p in persons:
            if p not in stat:
                stat[p] = 1
            else:
                stat[p] += 1

        if "*" in localization:
            localization = Text(localization.replace("*", ""), style="bright_green")

        table.add_row(
            key,
            v.get("developer", "N/A"),
            v.get("release", "N/A").split("-")[0],
            v.get("platform", "N/A"),
            localization,
            v.get("loc_url", ""),
        )


def main():
    platform_selection = ["pc98"]
    developer_selection = []

    dos_list = []
    pc98_list = []
    data_dos = {}
    data_pc98 = {}

    stat = dict()

    if "dos" in platform_selection:
        dos_list, data_dos = data_read("./list_dos.json", developer_selection)
    if "pc98" in platform_selection:
        pc98_list, data_pc98 = data_read("./list_pc98.json", developer_selection)

    target_list = list(set(dos_list) | set(pc98_list))
    target_list.sort()

    console = Console()
    table = Table(title="List of games")
    table.add_column("타이틀", justify="left", style="bright_white")
    table.add_column("제작", justify="left", style="cyan")
    table.add_column("릴리즈", justify="left", style="blue")
    table.add_column("플랫폼", justify="left", style="bright_red")
    table.add_column("한글화", justify="left", style="yellow")
    table.add_column("패치 주소", justify="left", style="bright_white")

    for k in target_list:
        if "dos" in platform_selection:
            if k in dos_list:
                put_data_to_table(k, data_dos, table, developer_selection, stat)

        if "pc98" in platform_selection:
            if k in pc98_list:
                put_data_to_table(k, data_pc98, table, developer_selection, stat)

    console.print(table)

    # To check contribution
    stat = dict(sorted(stat.items(), key=lambda item: item[1], reverse=True))
    for i, (k, v) in enumerate(stat.items(), start=1):
        print(f"{i:02d}: {k} ({v})")


if __name__ == "__main__":
    main()
