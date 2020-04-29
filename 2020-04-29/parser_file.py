import argparse


def create_save_subparser(subparsers):
    save_subparser = subparsers.add_parser('save', help="Режим вывода в файл")
    save_subparser.add_argument('-i',
                                type=str,  # argparse.FileType
                                required=True,
                                dest='filename',
                                help='Файл, в который будет идти запись')


def create_show_subparser(subparsers):
    subparsers.add_parser('show', help="Режим вывода в консоль")


def create_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('start',
                        type=int,
                        help="Начальное значение для арифметической прогресии")

    parser.add_argument('step',
                        type=int,
                        help="Шаг арифметической прогресии")

    parser.add_argument('-c', '--count',
                        default=5,
                        type=int,
                        help="Количество членов арифметической прогресии")

    subparsers = parser.add_subparsers(dest='command',
                                       description="Выберите режим вывода")

    create_show_subparser(subparsers)
    create_save_subparser(subparsers)

    return parser
