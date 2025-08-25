def reverseWords(s: str) -> str:
    words = s.split()
    words.reverse()
    return " ".join(words)


print(reverseWords("the sky is blue"))
print(reverseWords("  hello world  "))
print(reverseWords("a good   example"))
print(reverseWords("    "))
print(reverseWords("word"))