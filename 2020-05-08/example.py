import re
import operator

FILENAME = "example.txt"

oper = {"+": operator.add}

example_pattern = re.compile(r"(?P<first>\d+\.?\d*)(?: *)(?P<operator>[-+*/])(?: *)"
                             r"(?P<second>\d+\.?\d*)(?: *)=(?: *)(?P<result>\d+\.?\d*)")

with open(FILENAME, 'r') as f:
    for line in f:
        out = example_pattern.fullmatch(line.rstrip())
        if out is not None:
            print(oper[out['operator']](float(out['first']), float(out['second'])) ==
                  float(out['result']))
