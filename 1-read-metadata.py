import pandas as pd
import time


def get_metadata():
    return pd.read_csv("data/metadata-300k.tsv", sep='\t')


def get_counts_per_region(metadata):
    time.sleep(1)
    return metadata.groupby("region").size()


if __name__ == "__main__":
    metadata = get_metadata()
    print("Metadata:")
    print(metadata)
    counts_per_region = get_counts_per_region(metadata)
    print("Counts per region:")
    print(counts_per_region)
