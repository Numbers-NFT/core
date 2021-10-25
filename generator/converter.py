def to_bin(number_as_str):
    number = int(number_as_str)
    return f'{number:016b}'


def to_hex(number_as_str):
    number = int(number_as_str)
    return f'{hex(number)}'


if __name__ == "__main__":
    print(to_bin('1174'))
    print(to_hex('1174'))

