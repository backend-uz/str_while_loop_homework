def main(s):
    """
    A string of numbers is given. Find how many even numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    c = 0
    # l = len(s)
    while i < len(s):
        if int(s[i])%2 == 0:
            c += 1
        i += 1
    return c
print(main("1234"))