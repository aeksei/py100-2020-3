import random


def parse_template(template):
    if not isinstance(template, list):
        raise TypeError("Неверный формат ввода. Должен быть список")

    if not all(isinstance(oct_, list) for oct_ in template):
        raise TypeError("Неверный формат ввода. Список должен содерждать только списки")

    list_octet = []
    for octet in template:

        if octet:
            for item in octet:
                if isinstance(item, int):
                    list_octet.append(item)
                elif isinstance(item, tuple):
                    if len(item) != 2:
                        raise ValueError("Tuple должен быть длины 2")
                    list_octet.append(list(range(item[0], item[1])))  # раскрываем tuple
                # здесь через elif можно продолжать обработку остальных типов
        else:  # []
            list_octet.append(list(range(256)))

    # убираем все дублирующиеся значения
    # и возвращвем список, потому что будем много раз обращаться к этим значениям
    # и брать из них случайным образом
    print(list(map(set, template)))
    return list(map(set, template))  # [[], [], [], []]


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
