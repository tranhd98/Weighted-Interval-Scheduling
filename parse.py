import argparse


def parse():
    parser = argparse.ArgumentParser(description="pass file")
    parser.add_argument('filename', metavar="FILE", nargs=1, help="csv file")
    args = parser.parse_args()

    return args
