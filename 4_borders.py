def find_borders(s):
    n = len(s)
    borders = []
    for length in range(1, n):
        if s[:length] == s[n - length:]:
            borders.append(length)
    return borders
print(find_borders("abcababcab")) # 2 5