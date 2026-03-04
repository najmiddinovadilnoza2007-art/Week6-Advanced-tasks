def all_palindromes(s):
    n = len(s)
    result = []
    for i in range(n):
        max_len = 1
        # Odd length
        l, r = i, i
        while l > 0 and r < n and s[l] == s[r]:
            max_len = max(max_len, r - l + 1)
            l -= 1
            r += 1
        result.append(max_len)
    return result
print(all_palindromes("ababbababaa")) # 1 1 3 3 2 4 6 8 5 5 2
