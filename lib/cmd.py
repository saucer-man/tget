import argparse


# metavar参数的名字

def cmdparse():
    parser = argparse.ArgumentParser(description='Search target by fofa, zoomeye...')

    parser.add_argument(dest='api_name', metavar='api_name')

    parser.add_argument('-d', '--dork', metavar='dork', type=str,
                        dest='dork', required=True,
                        help='dork pattern to search for')
    parser.add_argument('--type', metavar='type', type=str,
                        dest='type', default="host",
                        help='dork pattern to search for')
    parser.add_argument('-o', '--output', metavar='output', type=str,
                        dest='output', default="tget_res.txt",
                        help='output for result')
    parser.add_argument('-v', dest='verbose', action='store_true',
                        help='verbose mode')
    parser.add_argument('--limit', metavar='limit', type=int, default=100,
                        help='limit to search')
    args = parser.parse_args()
    return args
