CRED = '\033[91m'
CEND = '\033[0m'


class ArgumentError(Exception):
    def __init__(self, text):
        self.txt = text


def flag(n):
    """
    Function that accept a single input parameter N and output a string with an ASCII art of the japanese flag.
    :param n: size of flag.
    :return: ASCII-string - art of japanese flag
    """
    if n % 2 == 0 and n != 0:

        width = n * 3
        height = n * 2

        output_str = ''

        # The range in which the circle will be drawn (by y)
        band = range(int(n / 2) + 1, height - int(n / 2) + 1)

        error = 0
        count_of_inner_parts = 0

        # including borders
        for i in range(height + 2):

            # draw border
            if i == 0 or i == height + 1:
                output_str += '#' + '#' * width + '#' + '\n'

            # draw circle
            elif i in band:

                output_str += '#' + ' ' * int(width / 2 - 1 - error) \
                              + '*' + 'o' * count_of_inner_parts + '*' \
                              + ' ' * int(width / 2 - 1 - error) + '#' + '\n'

                if i < int(height / 2):
                    count_of_inner_parts += 2
                    error += 1

                elif i == int(height / 2):
                    pass

                elif i > int(height / 2):
                    count_of_inner_parts -= 2
                    error -= 1

            # draw default line
            elif not (i in band):
                output_str += '#' + ' ' * width + '#' + '\n'

        return output_str
    else:
        raise ArgumentError(CRED + 'ArgumentError: This argument can only be even and != 0 !' + CEND)
