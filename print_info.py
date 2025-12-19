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


def main():
    developer_selection = []

    platform = "dos"
    with open(f"./list_{platform}.json", "r", encoding="utf-8") as f:
        data_dos = json.load(f)
        dos_list = get_target_keys(data_dos, developer_selection)

    platform = "pc98"
    with open(f"./list_{platform}.json", "r", encoding="utf-8") as f:
        data_pc98 = json.load(f)
        pc98_list = get_target_keys(data_pc98, developer_selection)

    target_list = list(set(dos_list) | set(pc98_list))
    target_list.sort()

    console = Console()
    table = Table(title="List of games")
    table.add_column("Title", justify="center", style="cyan")
    table.add_column("Developer", justify="center", style="cyan")
    table.add_column("Platform", justify="center", style="cyan")
    table.add_column("Localization", justify="center", style="cyan")

    for k in target_list:
        if k in dos_list:
            v = data_dos[k]
            developer = v.get("developer", "N/A").lower()
            if len(developer_selection) and developer not in developer_selection:
                pass
            else:
                table.add_row(
                    k,
                    v.get("developer", "N/A"),
                    v.get("platform", "N/A"),
                    v.get("localization", "N/A"),
                )
        if k in pc98_list:
            v = data_pc98[k]
            developer = v.get("developer", "N/A").lower()
            if len(developer_selection) and developer not in developer_selection:
                pass
            else:
                table.add_row(
                    k,
                    v.get("developer", "N/A"),
                    v.get("platform", "N/A"),
                    v.get("localization", "N/A"),
                )

    console.print(table)


if __name__ == "__main__":
    main()
