import csv

import pandas as pd


def main():
    titles = pd.read_csv(
        'data/title.basics.tsv',
        sep='\t',
        quoting=csv.QUOTE_NONE,
        index_col=0,
        dtype={'isAdult': bool},
        na_values='\\N',
    )
    print(titles.head())


if __name__ == '__main__':
    main()
