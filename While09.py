def main(s):
    """
    A string of numbers is given. Find the sum of all the numbers and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    c = 0
    while i < len(s):
        if int(s[i]):
            c += int(s[i])
        i += 1
    return c
print(main("8234"))