sentence = input("Введите предложение больше чем с двумя словами: ")

words_list = sentence.split(" ")

words_list = [word for word in words_list if word != ""]

words_list.sort()

for index, word in enumerate(words_list):
    print(f"{index}: {word}")

print("Кол-во слов:", len(words_list))