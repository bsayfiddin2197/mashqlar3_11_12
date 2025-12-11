# 1
sozlar = ["apple", "banana", "orange", "ice", "umbrella", "code", "olma"]

unlilar = "aeiouAEIOU"

unli_bilan_boshlanuvchilar = tuple(s for s in sozlar if s[0] in unlilar)
print(unli_bilan_boshlanuvchilar)

# 2
palindromlar = tuple(
    n for n in range(1, 51) if str(n) == str(n)[::-1]
)
print(palindromlar)

# 3
matn = "Hello!"

unicode_qiymatlar = tuple(ord(ch) for ch in matn)
print(unicode_qiymatlar)

# 4
kublar = tuple((n**3) for n in range(1, 21) if n % 5 == 0)
print(kublar)

# 5
sozlar = ["python", "set", "loop", "data", "science", "ai"]

katta_sozlar = tuple(s for s in sozlar if len(s) > 4)
print(katta_sozlar)
