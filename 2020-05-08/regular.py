import re
FILENAME = 'regular.txt'

def ipv4():
    ipv4_pattern = re.compile(r"""(?:(?:25[0-5]|  # 250-255
                                    2[0-4][0-9]|  # 200-249
                                    [01]?[0-9]?[0-9])\.){3}  # 0-199
                                    (?:25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])  # fourth octet
                                    """, re.VERBOSE)

    with open(FILENAME) as f:
        for line in f:
            pass
