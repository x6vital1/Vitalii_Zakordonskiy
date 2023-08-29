text = '''Любіть Україну, як сонце любіть,

як вітер, і трави, і води...

В годину щасливу і в радості мить,

любіть у годину негоди.

Любіть Україну у сні й наяву,

вишневу свою Україну,

красу її, вічно живу і нову,

і мову її солов'їну.

Без неї — ніщо ми, як порох і дим,

розвіяний в полі вітрами...

Любіть Україну всім серцем своїм

і всіми своїми ділами.'''

text = text.replace(',', '').replace('.', '').replace('\n', ' ').replace('—', '').lower()

words = text.split()

word_count = {}

for word in words:
    if len(word) > 1:
        word_count[word] = word_count.get(word, 0) + 1

most_common_word = max(word_count, key=word_count.get)
least_common_word = min(word_count, key=word_count.get)

print(word_count)
print("Слово которое встречается больше всего раз:", most_common_word, "({} раз)".format(word_count[most_common_word]))
print("Слово, которое встречается меньше всего раз:", least_common_word, "({} раз)".format(word_count[least_common_word]))
