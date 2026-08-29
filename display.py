def print_with_separators(lines: list[str], sep_char: str = "="):
    max_length = max(len(line) for line in lines if line)
    separator = sep_char * max_length

    print(f"\n{separator}")
    for line in lines:
        print(line)
    print(separator)
