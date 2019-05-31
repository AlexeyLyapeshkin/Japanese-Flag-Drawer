from flag import flag
import argparse as argprs

if __name__ == '__main__':

    parser = argprs.ArgumentParser(description='Drawing japanese flag!:)')
    right_arg = parser.add_argument('n', type=int, help='Size of flag.')
    args = parser.parse_args()

    fl = flag(args.n)

    print(fl)


