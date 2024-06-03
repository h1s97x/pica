def replace_spaces(str: str) -> str:
    return str.replace(' ', '-')

if __name__ == "__main__":
    import sys
    input_str = sys.argv[1]
    result = replace_spaces(input_str)
    print(result)
