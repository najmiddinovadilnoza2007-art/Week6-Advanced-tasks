def find_periods(s):
    n = len(s)
    periods = []
    for p in range(1, n + 1):
        is_period = True
        for i in range(n):
            if s[i] == s[i % p]:
                is_period = False
                break
        if is_period:
            periods.append(p)
    return periods
print(find_periods("abcabca")) # 3 6 7