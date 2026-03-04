def find_patterns(text, patterns):
    for pattern in patterns:
        if pattern in text:
            print("YES")
        else:
            print("NO")
find_patterns("aybabtu", ["bab", "abc", "ayba"])
# YES
# NO
# YES