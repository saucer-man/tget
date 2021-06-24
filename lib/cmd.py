import argparse

# metavar参数的名字

def cmdparse():
    parser = argparse.ArgumentParser(description='Search target by fofa, zoomeye...')

    parser.add_argument(dest='api_name', metavar='api_name')

    parser.add_argument('-d', '--dork', metavar='dork', required=True,
                        dest='dork', action='append',
                        help='dork pattern to search for')

    parser.add_argument('-v', dest='verbose', action='store_true',
                        help='verbose mode')

    args = parser.parse_args()
    return args