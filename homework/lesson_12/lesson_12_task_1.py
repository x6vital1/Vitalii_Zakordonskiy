from colour_for_lesson import mcolour as mc

poem = '''
Вечірній туман,
На горизонті рожевий фон,
Зірки яскраво сяють,
Спокій заполонює мій розум.

У кожному мрійливому погляді,
Таємничий блиск,
Слова красною ниткою сплітають,
Мов вірші, що весною цвітуть.

І в нічній тиші я чую,
Щось особливе в цих словах,
Вони струнко линуть у серце,
Таємниця краси розкривають.
'''

poem = poem.replace(",", "").replace('.', '')

target_words = ['туман', 'погляді', 'розкривають']

lines = poem.split('\n')

styled_lines = []

for line in lines:
    words = line.split()
    styled_line = ""
    for word in words:
        if word in target_words:
            styled_word = mc.universal_text_stile(word, text_color="red", bg_color="bg_purpure", text_style="1")
            styled_line += styled_word + " "
        else:
            styled_line += mc.universal_text_stile(word + " ", "black", "bg_purpure", "3")
    styled_lines.append(styled_line)

styled_poem = '\n'.join(styled_lines)


print(styled_poem)
