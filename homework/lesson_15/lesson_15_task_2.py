def longest_words(file):
    with open(file, 'r', encoding='utf-8') as f:
        words = f.read().split()

    longest = []
    max_length = 0

    for word in words:
        word = word.strip('.,!?":;')

        if len(word) > max_length:
            max_length = len(word)
            longest = [word]
        elif len(word) == max_length:
            longest.append(word)

    return ', '.join(longest)


file_name = "article.txt"
result = longest_words(file_name)
if result:
    print("Самое сдлинное слово (слова):", result)
else:
    print("Файл пустой или не существует.")
