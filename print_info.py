import json
from rich.console import Console
from rich.table import Table


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


def put_data_to_table(key: str, data: dict, table: Table, developer_selection: list):
    v = data[key]
    developer = v.get("developer", "N/A").lower()
    if len(developer_selection) and developer not in developer_selection:
        pass
    else:
        table.add_row(
            key,
            v.get("developer", "N/A"),
            v.get("platform", "N/A"),
            v.get("localization", "N/A"),
        )


def main():
    platform_selection = ["dos", "pc98"]
    developer_selection = []

    dos_list = []
    pc98_list = []
    data_dos = {}
    data_pc98 = {}

    if "dos" in platform_selection:
        dos_list, data_dos = data_read("./list_dos.json", developer_selection)
    if "pc98" in platform_selection:
        pc98_list, data_pc98 = data_read("./list_pc98.json", developer_selection)

    target_list = list(set(dos_list) | set(pc98_list))
    target_list.sort()

    console = Console()
    table = Table(title="List of games")
    table.add_column("Title", justify="center", style="cyan")
    table.add_column("Developer", justify="center", style="cyan")
    table.add_column("Platform", justify="center", style="cyan")
    table.add_column("Localization", justify="center", style="cyan")

    for k in target_list:
        if "dos" in platform_selection:
            if k in dos_list:
                put_data_to_table(k, data_dos, table, developer_selection)

        if "pc98" in platform_selection:
            if k in pc98_list:
                put_data_to_table(k, data_pc98, table, developer_selection)

    console.print(table)


if __name__ == "__main__":
    main()
