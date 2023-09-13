def update_hero(**kwargs):
    with open('hero.ini', 'r') as file:
        lines = file.readlines()

    data = {}
    for line in lines:
        key, value = line.strip().split('=')
        data[key.strip()] = value.strip()

    for key, value in kwargs.items():
        if key in data:
            data[key] = str(value)

    with open('hero.ini', 'w') as file:
        for key, value in data.items():
            file.write(f"{key}={value}\n")


update_hero(hero="Halk", power=450, Y=2.3, speed=1000)
