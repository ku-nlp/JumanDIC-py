def is_valid_line(line: str) -> bool:
    if line.strip() == "":
        return False
    if line.startswith(";"):
        return False
    return True
