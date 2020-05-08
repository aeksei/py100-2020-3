import re
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


# def filter_ip(fn):
#     def wrapper(*args, **kwargs):
#         # дейсвие перед вызовом функции
#
#         result = fn(*args, **kwargs)
#
#         # дейсвие после вызова функции
#         return result
#     return wrapper

def filter_ip(pattern):
    def filter_ip_decorator(fn):
        def wrapper(*args, **kwargs):
            filter_pattern = re.compile(pattern)

            local_gen = fn(*args, **kwargs)

            for item in local_gen:  # здесь теперь возвращаются случаные ip адреса
                # дейсвие перед вызовом нового шага генератора
                if filter_pattern.fullmatch(item) is not None:  # а здесь мы их фильтруем на каждом шаге генератора
                    input_ = yield item

                    if input_ is not None:  # это для корутины, для цикла for работать не будет
                        local_gen.send(input_)

                # дейсвие после вызова нового шага генератора

        return wrapper
    return filter_ip_decorator


# @filter_ip(r"192\.168(?:\.\d{1,3}){2}")
@filter_ip(r"10(?:\.\d{1,3}){3}")
def gen_ip(template):
    template = parse_template(template)  # распарсили шаблон и получили список уникальных значений

    while True:  # сделать корутину, чтобы принимать новый шаблон
        ip_random = map(random.choice, template)
        # print(list(ip_random))

        input_ = yield ".".join(map(str, ip_random))
        if input_ is not None:
            pass


def main():
    COUNT = 20
    template = [[], [], [], []]
    gen = gen_ip(template)

    for _ in range(COUNT):
        print(next(gen))


if __name__ == "__main__":
    main()
