from colour_for_lesson import mcolour as mc

if __name__ == "__main__":
    poem = """
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
    """

    # Виокремлюємо ключові слова і надаємо їм стиль
    styled_poem = custom_style_text(poem, background='red', style='3;1')
    styled_poem = styled_poem.replace("рожевий фон", custom_style_text("рожевий фон", color='blue'))
    styled_poem = styled_poem.replace("слова красною", custom_style_text("слова красною", color='green'))

    print(styled_poem)
