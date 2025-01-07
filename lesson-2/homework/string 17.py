text = input("Matn kiriting: ")
symbol = input("Unli harflarni almashtirish uchun belgi kiriting: ")
result = text
for vowel in "aeiouAEIOU":
    result = result.replace(vowel, symbol)
print(f"Natija: {result}")
