import random


def parse_template(raw_template, unique=True):
    # проверка корректности входных данных
    if not isinstance(raw_template, list):
        raise TypeError(f"Шаблон должен быть списком, не {type(raw_template)}")

    if not all(isinstance(oct_, list) for oct_ in raw_template):
        raise TypeError("Шаблон должен включать в себя только списки")

    if len(raw_template) != 4:
        raise ValueError("Шаблон должен быть длины 4!")

    template = []
    for oct_ in raw_template:
        octet_list = []
        if not oct_:
            octet_list.extend(range(256))
        else:
            for item in oct_:
                if isinstance(item, int):
                    octet_list.append(item)
                elif isinstance(item, tuple):
                    octet_list.extend(range(*item))
                    # octet_list.extend(range(item[0], item[1))
                # далее через elif можно продолжать обрабатывать различные типы

        template.append(octet_list)

    if unique:
        unique_template = map(set, template)
        return list(map(list, unique_template))
    else:
        return template


def gen_ip(template):
    template = parse_template(template)  # распарсили шаблон и получили список уникальных значений

    while True:  # сделать корутину, чтобы принимать новый шаблон
        ip_random = map(random.choice, template)
        print(list(ip_random))
        yield ".".join(map(str, ip_random))


def main():
    COUNT = 20
    template = [[192], [168], [1, 5, (100, 150), 200, 240], []]
    gen = gen_ip(template)

    for _ in range(COUNT):
        print(next(gen))


if __name__ == "__main__":
    main()
