from pathlib import Path

base_dir = Path("C:/emul/pc98/game_data_checked")

folders = list(base_dir.glob("*"))


pass_list = ["ELLE", "Jack", "Shangrlia 1", "Shangrlia 2", "하급생", "Seiki (성귀)"]


for folder in folders:
    if folder.name in pass_list:
        continue

    files = list((base_dir / folder).glob("*"))

    is_doxbox_x = False
    for file in files:
        if "KOR-dosbox-x" in file.name:
            is_doxbox_x = True
            break
    if not is_doxbox_x:
        print(folder.name)
