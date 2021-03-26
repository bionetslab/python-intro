import argparse
import pandas as pd
import numpy as np


def log_transform(path_to_input, path_to_output, sep, drop):
    df = pd.read_csv(path_to_input, sep=sep, index_col=0)
    df = df.drop(columns=drop)
    df = df.apply(np.log2)
    df.to_csv(path_to_output, sep=sep)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Compute factorial')
    parser.add_argument('input', help='Path to input file.')
    parser.add_argument('output', help='Path to output file.')
    parser.add_argument('--sep', default='\t', help='Seperator in files.')
    parser.add_argument('--drop', nargs='+', help='Column to drop.')
    args = parser.parse_args()
    log_transform(args.input, args.output, args.sep, args.drop)