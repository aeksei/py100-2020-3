import re
FILENAME = 'regular.txt'


def ipv4():
    ipv4_pattern = re.compile(r"""(?:(?:25[0-5]|  # 250-255
                                    2[0-4][0-9]|  # 200-249
                                    [01]?[0-9]?[0-9])\.){3}  # 0-199
                                    (?:25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])  # fourth octet
                                    """, re.VERBOSE)

    count = 0
    with open(FILENAME) as f:
        for line in f:
            if ipv4_pattern.match(line) is not None:
                count += 1
            else:
                print(line)
    print(count)


def replace():
    string = "aba accca azzza wwwwa"

    str_pattern = re.compile(r"\ba[^a]*?a\b")
    # print(str_pattern.sub(lambda x: , string))
    pass


def remove():
    list_ = [
        '<strong>Наши</strong> <em>ховерборды</em> лучшие в <u>мире</u>!',
        '<EM>Световой меч</EM> в <strong>каждый</strong> дом!'
    ]
    tag = re.compile(r"<\/?.+?>")


    #
    # output = ""
    # for line in list_:
    #     output += tag.sub("", line)
    #     output += '\n'

    output = "\n".join(map(lambda x: tag.sub("", x), list_))
    print(output)

    # найти теги
    # удалить (заменить) теги
    # склеить строку (join)

    # print()


if __name__ == "__main__":
    # ipv4()
    # replace()
    # remove()
    eval()