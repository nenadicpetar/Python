s = "Hello"
i = 3

if len(s) == 0: #umjesto len(s) može biti i not s
    print("Empty string")
elif i < len(s):
    print(s[i])
else:
    print("i out of range")