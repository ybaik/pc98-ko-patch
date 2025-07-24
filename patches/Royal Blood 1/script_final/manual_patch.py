# MAIN.EXE
patch_info = {
    "2D28C=2D28D": "0x8DBB",  # 춘 -> 봄
    "2D290=2D291": "0x9581",  # 하 -> 여름
    "2D294=2D295": "0x9582",  # 추 -> 가을
    "2D298=2D299": "0x9583",  # 동 -> 겨울
    "2F6D2=2F6D3": "0x957E",  # 조 -> 아침
    "2F6DA=2F6DB": "0x957F",  # 석 -> 저녁
}


def main():
    src_data_path = "../workspace/rb1-PC98-KOR/MAIN.EXE"
    dst_data_path = "../workspace/rb1-PC98-KOR/MAIN_.EXE"
    with open(src_data_path, "rb") as f:
        data = f.read()
    data = bytearray(data)

    for address, code_hex in patch_info.items():
        code_hex_start = address.split("=")[0]
        pos = int(code_hex_start, 16)
        code_int = int(code_hex, 16)
        data[pos] = (code_int & 0xFF00) >> 8
        data[pos + 1] = code_int & 0x00FF

    with open(dst_data_path, "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
